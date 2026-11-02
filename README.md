# Agent Policy Engine

**Repository:** `PCakes303/agent-policy-engine`  
**Portfolio position:** 09 / 31 public repositories  
**Maturity:** scaffolding  
**License:** [Scoped mixed-license policy](LICENSE.md).

## Purpose

Provide a deterministic, default-deny policy decision component for agent principals, actions, resources, and scopes. The policy engine defines portable policy and request contracts and produces explainable decisions with matched rule identifiers.

## Initial implementation

The first scaffold includes:
- Versioned JSON Schemas for policy bundles and decision requests.
- A small Python decision evaluator with explicit-deny-overrides semantics.
- Fail-closed behavior for invalid policy/request data.
- Positive, negative, precedence, wildcard, and scope tests.
- CLI and least-privilege CI.

This is a **policy decision prototype**, not a production security boundary. It does not authenticate principals, distribute or sign policy bundles, enforce decisions at a protected resource, or protect itself from a compromised host. Callers must authenticate identity independently and enforce the decision at the resource boundary.

## Quick start

Requires Python 3.10+.

```bash
python -m pip install -r requirements-dev.txt
python tools/evaluate_policy.py --policy examples/policy.json --request examples/allow-request.json
python -m unittest discover -s tests -v
```

## License status

This repository applies a scoped mixed-license policy: original source code and machine-readable contracts are licensed under Apache-2.0; original human-readable documentation is licensed under CC BY 4.0. Third-party material retains upstream terms. Datasets, evidence, fixtures, sample payloads, media, and material with uncertain provenance are not blanket-licensed and require separate review. See [LICENSE.md](LICENSE.md).

## Roadmap

1. **Developer:** stable policy bundle versioning, decision explanation codes, and adapters for protected resource boundaries.
2. **Verification:** signed policy bundles, identity binding, revocation-aware authorization, and cross-component conformance tests.
3. **Production:** authenticated distribution, rollout/rollback, audit integration, resource-server enforcement, rate limits, independent security review.

No production authorization, identity verification, or compliance claim is made.
