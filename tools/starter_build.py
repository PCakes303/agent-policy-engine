#!/usr/bin/env python3
"""Run the local policy-engine starter checks."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for command in ([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"], [sys.executable, "tools/evaluate_policy.py", "--policy", "examples/policy.json", "--request", "examples/allow-request.json"]):
    result = subprocess.run(command, cwd=ROOT)
    if result.returncode:
        raise SystemExit(result.returncode)
print("Policy engine starter build passed.")
