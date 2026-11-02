import copy
import json
import unittest
from pathlib import Path

from tools.policy_engine import evaluate

ROOT = Path(__file__).resolve().parents[1]
POLICY = json.loads((ROOT / "examples/policy.json").read_text(encoding="utf-8"))
REQUEST = json.loads((ROOT / "examples/allow-request.json").read_text(encoding="utf-8"))


class PolicyEngineTests(unittest.TestCase):
    def test_matching_allow(self):
        self.assertEqual(evaluate(POLICY, REQUEST)["effect"], "allow")

    def test_default_deny_unknown_principal(self):
        request = dict(REQUEST, principal_id="agent://unknown")
        self.assertEqual(evaluate(POLICY, request)["decision_id"], "default-deny")

    def test_missing_scope_denies(self):
        request = dict(REQUEST, scopes=[])
        self.assertEqual(evaluate(POLICY, request)["effect"], "deny")

    def test_explicit_deny_overrides_allow(self):
        policy = copy.deepcopy(POLICY)
        policy["rules"].append({"id":"deny-public","effect":"deny","principals":["*"],"actions":["resource.read"],"resources":["public:*"],"required_scopes":[]})
        self.assertEqual(evaluate(policy, REQUEST)["decision_id"], "explicit-deny")

    def test_restricted_resource_denied(self):
        request = dict(REQUEST, resource="restricted:document-1")
        self.assertEqual(evaluate(POLICY, request)["decision_id"], "explicit-deny")

    def test_invalid_request_fails_closed(self):
        request = dict(REQUEST, unexpected="field")
        result = evaluate(POLICY, request)
        self.assertEqual(result["effect"], "deny")
        self.assertEqual(result["decision_id"], "invalid-input")

    def test_non_object_policy_fails_closed(self):
        self.assertEqual(evaluate([], REQUEST)["decision_id"], "invalid-input")

    def test_invalid_scopes_fails_closed(self):
        request = dict(REQUEST, scopes=[{"bad":"type"}])
        self.assertEqual(evaluate(POLICY, request)["effect"], "deny")

    def test_policy_default_must_be_deny(self):
        policy = dict(POLICY, default_effect="allow")
        self.assertEqual(evaluate(policy, REQUEST)["decision_id"], "invalid-input")


if __name__ == "__main__":
    unittest.main()
