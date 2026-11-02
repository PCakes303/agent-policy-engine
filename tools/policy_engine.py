"""Experimental deterministic policy decision evaluator; not an enforcement boundary."""
from __future__ import annotations

import fnmatch
from pathlib import Path
from typing import Any
import json

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
POLICY_SCHEMA = json.loads((ROOT / "schemas/policy.schema.json").read_text(encoding="utf-8"))
REQUEST_SCHEMA = json.loads((ROOT / "schemas/decision-request.schema.json").read_text(encoding="utf-8"))


def _matches(patterns: list[str], value: str) -> bool:
    return any(fnmatch.fnmatchcase(value, pattern) for pattern in patterns)


def validate_inputs(policy: Any, request: Any) -> list[str]:
    errors = []
    errors.extend(f"policy: {e.message}" for e in Draft202012Validator(POLICY_SCHEMA).iter_errors(policy))
    errors.extend(f"request: {e.message}" for e in Draft202012Validator(REQUEST_SCHEMA).iter_errors(request))
    return errors


def evaluate(policy: Any, request: Any) -> dict[str, Any]:
    errors = validate_inputs(policy, request)
    if errors:
        return {"effect": "deny", "decision_id": "invalid-input", "matched_rules": [], "reason": "policy or request failed schema validation", "validation_errors": errors}

    principal = request["principal_id"]
    action = request["action"]
    resource = request["resource"]
    scopes = set(request["scopes"])
    allows, denies = [], []

    for rule in policy["rules"]:
        if not _matches(rule["principals"], principal):
            continue
        if not _matches(rule["actions"], action):
            continue
        if not _matches(rule["resources"], resource):
            continue
        if not set(rule["required_scopes"]).issubset(scopes):
            continue
        (allows if rule["effect"] == "allow" else denies).append(rule["id"])

    if denies:
        return {"effect": "deny", "decision_id": "explicit-deny", "matched_rules": sorted(denies), "reason": "an explicit deny rule matched"}
    if allows:
        return {"effect": "allow", "decision_id": "explicit-allow", "matched_rules": sorted(allows), "reason": "one or more allow rules matched and no deny rule matched"}
    return {"effect": "deny", "decision_id": "default-deny", "matched_rules": [], "reason": "no allow rule matched"}
