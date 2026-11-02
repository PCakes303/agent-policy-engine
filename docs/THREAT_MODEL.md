# Threat Model

## Assets
Policy bundles, decision requests, decision results, policy version identifiers, and downstream authorization decisions.

## Threats and controls
- **Forged principal ID:** identifiers are caller-supplied strings; authentication is explicitly outside this component. A trusted caller must bind them to authenticated identity.
- **Policy tampering:** the initial evaluator reads local policy files and does not authenticate their origin. Signed distribution is a planned feature.
- **Rule shadowing:** explicit deny overrides allows regardless of order; negative precedence tests protect this invariant.
- **Malformed input:** strict JSON Schemas, bounded collections/strings, and fail-closed validation reject invalid documents.
- **Wildcard overreach:** wildcard behavior is explicit and tested; policy authors must review patterns carefully.
- **Decision bypass:** this component does not enforce decisions. Protected resources must independently require and enforce a decision.
- **Stale/revoked identity:** no revocation or freshness integration exists in this scaffold.

## Residual risk
No principal authentication, signed policy bundle, remote policy distribution, protected resource middleware, revocation, or production hardening is implemented.
