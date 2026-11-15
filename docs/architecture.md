# Architecture

## Deployment model

NSE is a standalone repository with two deployment roles:

- **OpenWrt x86_64 agent:** client-side DNS policy enforcement, local diagnostics, firewall integration, and local recovery.
- **Ubuntu 24.04 agent:** server-side certificate lifecycle, service validation, access control, audit, and health reporting.

Both agents consume the same versioned policy schema. They do not share private keys and must not grant the VPS unrestricted administrative control over the router.

## Logical components

1. Policy manager: schema, validation, versioning, signing, and rollback.
2. DNS security: encrypted resolver configuration, DNSSEC status, bootstrap dependencies, and leak diagnostics.
3. TLS security: protocol baseline, certificate-chain validation, hostname verification, and handshake diagnostics.
4. Transport security: configuration and runtime checks delegated to mature protocol implementations.
5. Privacy audit: report observable metadata and minimize retained logs.
6. Health monitor: resolver, connection, certificate, and service health.
7. Audit: structured security events with redaction.
8. Recovery: validate-before-apply and last-known-good rollback.
9. Platform adapters: OpenWrt/Firewall4 and Ubuntu/systemd integration.

## Trust boundaries

- The policy file is declarative input, not proof that a setting is active.
- Runtime adapters must verify generated configuration against the installed software version.
- Router and server credentials are distinct.
- Management endpoints are not exposed publicly by default.
- High-impact firewall changes require explicit local authorization and rollback protection.

## Security constraints

- Do not implement cryptographic primitives.
- Never silently downgrade certificate validation or DNS encryption.
- Do not log full URLs, credentials, DNS query names, or payloads by default.
- Report uncertainty explicitly; do not claim invisibility or guaranteed resistance to network filtering.
- ECH is a capability/compatibility assessment, not a guarantee that all metadata is hidden.

## Initial implementation boundary

Version 0.1.0 validates policy intent only. It does not modify DNS, firewall, proxy, TLS, or system services.
