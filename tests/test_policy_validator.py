from pathlib import Path
import pytest
import yaml
from nse.policy.loader import load_policy
from nse.policy.validator import PolicyValidationError, validate_policy

POLICY_PATH = Path(__file__).parents[1] / "config" / "policy.yaml"

def test_default_policy_loads_and_validates():
    policy = load_policy(POLICY_PATH)
    assert policy["schema_version"] == 1
    assert validate_policy(policy) == []

@pytest.mark.parametrize("mutation", [
    lambda p: p.update(schema_version=2),
    lambda p: p["security"]["dns"]["fallback"].update(allow_plaintext=True),
    lambda p: p["security"]["dns"]["validation"].update(tls_certificate="insecure"),
    lambda p: p["security"]["tls"].update(verify_certificates=False),
    lambda p: p["security"]["tls"].update(verify_hostname=False),
    lambda p: p["security"]["dns"].update(protocols=["made-up"]),
])
def test_unsafe_or_unknown_policy_is_rejected(mutation):
    policy = yaml.safe_load(POLICY_PATH.read_text(encoding="utf-8"))
    mutation(policy)
    with pytest.raises(PolicyValidationError):
        validate_policy(policy)

def test_duplicate_dns_protocol_is_rejected():
    policy = yaml.safe_load(POLICY_PATH.read_text(encoding="utf-8"))
    policy["security"]["dns"]["protocols"] = ["doh", "doh"]
    with pytest.raises(PolicyValidationError):
        validate_policy(policy)
