# Proxy System Network Security Engine (NSE)

NSE is a standalone project for security policy management and diagnostics across OpenWrt x86_64 and Ubuntu 24.04.

## Scope
- Shared, versioned security policy.
- DNS privacy and DNSSEC status validation.
- TLS certificate and hostname verification diagnostics.
- Secure transport configuration checks using maintained protocol implementations.
- Privacy and metadata exposure reporting.
- Health monitoring, audit events, and safe rollback.

NSE does not implement custom cryptography, disable certificate validation, or claim traffic is undetectable. It does not include DPI-evasion, active-probe deception, or traffic-fingerprint spoofing.

## Current status
This clean repository starts as a standalone project. The bootstrap release provides documentation, a policy schema, a validator, and tests. Host networking changes and runtime adapters are intentionally not enabled until platform integration tests exist.

## Development
Python 3.10+.

```bash
python -m pip install -e '.[dev]'
pytest
```

See [architecture](docs/architecture.md), [security policy](docs/security-policy.md), and [testing](docs/testing.md).
