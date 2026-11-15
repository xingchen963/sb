# OpenWrt x86_64 Deployment

Target: OpenWrt x86_64 with Firewall4/nftables.

Initial rollout is diagnostic-only:
1. Back up configuration and record installed package/core versions.
2. Install NSE in an isolated Python environment appropriate to the device.
3. Validate the policy file.
4. Run read-only DNS/TLS diagnostics.
5. Review recommendations before enabling any adapter.

Do not replace existing firewall rules or DNS services in the bootstrap release. Any later firewall adapter must use Firewall4-compatible include mechanisms, validate the resulting ruleset, and provide timed rollback.
