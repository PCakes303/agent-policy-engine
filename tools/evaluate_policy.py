#!/usr/bin/env python3
"""Evaluate one policy decision request; exit 0 only for an allow decision."""
import argparse
import json
import sys
from pathlib import Path

from policy_engine import evaluate


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--policy", type=Path, required=True)
    parser.add_argument("--request", type=Path, required=True)
    args = parser.parse_args()
    try:
        policy = json.loads(args.policy.read_text(encoding="utf-8"))
        request = json.loads(args.request.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"effect": "deny", "decision_id": "input-error", "reason": str(exc)}))
        return 2
    result = evaluate(policy, request)
    print(json.dumps(result, indent=2))
    return 0 if result["effect"] == "allow" else 1


if __name__ == "__main__":
    raise SystemExit(main())
