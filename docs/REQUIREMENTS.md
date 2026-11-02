# Requirements

| ID | Requirement | Initial status |
|---|---|---|
| POL-001 | Define a versioned policy bundle with mandatory default deny. | Scaffolded |
| POL-002 | Define a bounded decision request with principal, action, resource, and scopes. | Scaffolded |
| POL-003 | Validate policy and request documents before evaluation. | Scaffolded |
| POL-004 | Explicit deny overrides any matching allow. | Scaffolded |
| POL-005 | No matching allow results in deny. | Scaffolded |
| POL-006 | Return stable decision identifiers and matched rule IDs. | Scaffolded |
| POL-007 | Authenticate principals independently of policy evaluation. | Planned |
| POL-008 | Distribute signed, freshness-checked policy bundles. | Planned |
| POL-009 | Enforce decisions at protected resource boundaries. | Planned |
| POL-010 | Integrate revocation and audit evidence. | Planned |

A scaffolded requirement means an initial contract or test exists; it is not production authorization assurance.
