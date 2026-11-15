# Ubuntu 24.04 VPS Deployment

Initial rollout is diagnostic-only:
1. Record OS, kernel, sing-box/Xray versions, listeners, firewall rules, and certificate paths.
2. Back up service and firewall configuration.
3. Install NSE in an isolated Python environment.
4. Validate the policy and run read-only diagnostics.
5. Keep management interfaces bound to loopback or a protected management network.

Do not expose a new public management API in the bootstrap release. Private keys must remain outside the policy repository and have restrictive filesystem permissions.
