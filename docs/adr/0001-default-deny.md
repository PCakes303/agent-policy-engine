# ADR 0001: Default-deny policy decision semantics

- **Status:** accepted for initial experimental contract
- **Context:** agent actions need explicit authorization decisions that are predictable under overlapping rules.
- **Decision:** policy bundles must set `default_effect: deny`; invalid inputs deny; explicit deny overrides all allows; absent matching allow denies; evaluation is deterministic and side-effect free.
- **Consequences:** policy evaluation is separate from principal authentication and resource enforcement. A returned allow is not a proof of identity and must be enforced by a protected resource.
