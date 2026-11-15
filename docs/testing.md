# Testing and Acceptance

## Unit tests
Run `pytest`. Policy parsing and validation must reject malformed input, unknown protocols, duplicate protocols, plaintext DNS fallback, and disabled certificate/hostname verification.

## Integration tests (later stages)
- DNS: DoH/DoT/DoQ operation, DNSSEC valid/invalid signatures, bootstrap behavior, timeout and upstream failure.
- TLS: valid chain, expired certificate, untrusted issuer, wrong hostname, protocol minimum, and ALPN negotiation.
- Transport: protocol-native tests for integrity, session resumption, replay handling, key lifecycle, and error behavior.
- OpenWrt: Firewall4/nftables coexistence, DNS interception, reboot persistence, and rollback.
- Ubuntu: systemd lifecycle, file permissions, firewall exposure, certificate renewal, and service recovery.
- Cross-platform: policy compatibility and generated configuration validation against exact installed versions.

## Acceptance gates
- All unit tests pass.
- No critical/high unresolved security findings.
- Generated configuration passes native validators.
- Invalid policy is rejected before any host mutation.
- Recovery returns to the last-known-good configuration in a controlled test.
- A 72-hour soak test completes without unexplained service failure.

A passing policy unit test is not evidence that runtime networking is secure. Each integration test must record environment and software versions.
