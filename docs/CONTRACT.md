# Policy Contract 1.0.0

## Decision request
A request contains a principal identifier, action, resource, and explicit scope list. Optional context is limited to scalar values. The evaluator treats all request fields as untrusted and validates them before matching.

## Policy bundle
A policy bundle has a stable policy ID, version, mandatory `default_effect: deny`, and bounded list of rules. Each rule specifies an effect, principals, actions, resources, and required scopes. Wildcards use Python `fnmatchcase` matching; consumers must not assume shell expansion or regular-expression semantics.

## Evaluation semantics
1. Validate the complete policy and request against the versioned schemas.
2. Invalid input produces a deny result with decision ID `invalid-input`.
3. Match principal, action, resource, and required scopes.
4. Any matching explicit deny overrides all matching allows.
5. If at least one allow matches and no deny matches, return allow.
6. If no allow matches, return default deny.

The result includes stable decision ID, matched rule IDs, and a concise reason. Rule order does not affect precedence.

## Security boundary
This component is a decision evaluator only. It does not authenticate principal identifiers, protect policy files, distribute policies, or enforce a decision at a resource boundary. A caller must authenticate independently and enforce the result at the protected resource. Never treat an allow result as an identity assertion.
