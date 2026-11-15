"""Fail-closed validation for the initial NSE policy schema."""
from __future__ import annotations
from typing import Any

SUPPORTED_LEVELS = {"standard", "strict", "custom"}
SUPPORTED_DNS_PROTOCOLS = {"doh", "dot", "doq"}

class PolicyValidationError(ValueError):
    """Raised when policy input is malformed or unsafe."""

def validate_policy(policy: dict[str, Any]) -> list[str]:
    """Validate policy intent; this does not apply settings to the host."""
    if not isinstance(policy, dict):
        raise PolicyValidationError("policy must be a mapping")
    if policy.get("schema_version") != 1:
        raise PolicyValidationError("schema_version must be 1")
    security = policy.get("security")
    if not isinstance(security, dict):
        raise PolicyValidationError("security must be a mapping")
    if security.get("level") not in SUPPORTED_LEVELS:
        raise PolicyValidationError(f"security.level must be one of {sorted(SUPPORTED_LEVELS)}")
    dns = security.get("dns")
    if not isinstance(dns, dict):
        raise PolicyValidationError("security.dns must be a mapping")
    protocols = dns.get("protocols")
    if not isinstance(protocols, list) or not protocols:
        raise PolicyValidationError("security.dns.protocols must be a non-empty list")
    if len(protocols) != len(set(protocols)):
        raise PolicyValidationError("security.dns.protocols contains duplicates")
    unknown = set(protocols) - SUPPORTED_DNS_PROTOCOLS
    if unknown:
        raise PolicyValidationError(f"unsupported DNS protocols: {sorted(unknown)}")
    validation = dns.get("validation")
    if not isinstance(validation, dict) or validation.get("tls_certificate") != "strict":
        raise PolicyValidationError("DNS TLS certificate validation must be strict")
    if not isinstance(validation.get("dnssec"), bool):
        raise PolicyValidationError("security.dns.validation.dnssec must be boolean")
    fallback = dns.get("fallback")
    if not isinstance(fallback, dict):
        raise PolicyValidationError("security.dns.fallback must be a mapping")
    if fallback.get("allow_plaintext") is not False:
        raise PolicyValidationError("plaintext DNS fallback must be explicitly disabled")
    if fallback.get("mode") not in {"fail_closed", "explicit_user_override"}:
        raise PolicyValidationError("fallback.mode must be fail_closed or explicit_user_override")
    tls = security.get("tls")
    if not isinstance(tls, dict):
        raise PolicyValidationError("security.tls must be a mapping")
    if tls.get("minimum_version") not in {"1.2", "1.3"}:
        raise PolicyValidationError("TLS minimum_version must be 1.2 or 1.3")
    if tls.get("verify_certificates") is not True:
        raise PolicyValidationError("TLS certificate verification must be enabled")
    if tls.get("verify_hostname") is not True:
        raise PolicyValidationError("TLS hostname verification must be enabled")
    privacy = security.get("privacy")
    if not isinstance(privacy, dict) or not isinstance(privacy.get("minimize_logs"), bool):
        raise PolicyValidationError("security.privacy.minimize_logs must be boolean")
    return []
