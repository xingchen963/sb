"""YAML policy loader."""
from pathlib import Path
from typing import Any
import yaml
from .validator import validate_policy

def load_policy(path: str | Path) -> dict[str, Any]:
    """Load and validate a policy YAML file."""
    with Path(path).open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError("policy document must contain a YAML mapping")
    validate_policy(data)
    return data
