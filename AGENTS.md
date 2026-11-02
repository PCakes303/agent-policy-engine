# Agent Instructions — Policy Engine

## First reads
1. `README.md`
2. `docs/CONTRACT.md`
3. `docs/THREAT_MODEL.md`
4. `manifest.json`, `capabilities.json`, and `compatibility.json`
5. Master registry: https://github.com/PCakes303/agent-intelligence-ecosystem

## Authority and safety
- This repository owns policy document/request contracts and deterministic decision semantics.
- The master repository owns portfolio identity, visibility, and dependency graph.
- A policy decision is not proof that a principal was authenticated.
- The policy engine is not a resource enforcement point unless a protected resource independently enforces its result.
- Invalid, missing, stale, or unverifiable policy input must fail closed.
- Explicit deny overrides any matching allow.
- Do not silently broaden wildcard semantics or default effects.
- Do not include private operational policy, credentials, tokens, or personal data in public examples.
- Treat policy bundles and requests as untrusted input.

## Engineering rules
- Keep evaluation deterministic, bounded, and side-effect free.
- Validate the complete policy and request before evaluating.
- Never use Python `eval`, dynamic code execution, shell commands, or network retrieval in the evaluator.
- Return stable decision identifiers and matched rule IDs; do not leak secret policy internals.
- Add tests for malformed input, wildcard boundaries, deny precedence, scope mismatch, and unknown principals.
- Do not claim production authorization or standards conformance without separate implementation and evidence.

## Verification
```bash
python -m unittest discover -s tests -v
python tools/evaluate_policy.py --policy examples/policy.json --request examples/allow-request.json
```
