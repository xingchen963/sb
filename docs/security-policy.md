# Security Policy

## Baseline

- Prefer TLS 1.3; permit TLS 1.2 only where compatibility requires it.
- Require certificate-chain and hostname verification.
- Use DoH, DoT, or DoQ through maintained implementations with strict TLS verification.
- Treat DNSSEC as authenticity/integrity validation, not encryption.
- Disable plaintext DNS fallback by default; fail closed unless an operator explicitly chooses a documented exception.
- Use mature protocol stacks for AEAD, key exchange, key derivation, and replay protection.
- Keep client and server private keys separate.
- Minimize logs and redact secrets.

## Policy levels

- `standard`: secure defaults with documented compatibility allowances.
- `strict`: no silent security downgrade; fail closed for configured protected paths.
- `custom`: operator-defined settings, still subject to schema safety constraints.

## Change control

Every policy update should include a schema version, policy revision, validation result, and rollback reference. Runtime enforcement must be confirmed independently from policy validation.
