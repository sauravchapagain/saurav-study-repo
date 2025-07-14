#!/usr/bin/env python
import os
import sys
from pathlib import Path

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django  # noqa
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )

        raise

    # This allows easy placement of apps within the interior
    # kash4me directory.
    current_path = Path(__file__).parent.resolve()
    sys.path.append(str(current_path / "kash4me"))

    execute_from_command_line(sys.argv)


import subprocess
import pickle
import os

# [B602] Subprocess with shell=True - potential command injection
def run_command(cmd):
    subprocess.call(cmd, shell=True)

# [B403] Pickle used to deserialize data - arbitrary code execution risk
def load_data_from_file(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data

# [B105] Hardcoded password
def connect_to_db():
    password = "supersecret123"
    print("Connecting with password:", password)

# [B108] Hardcoded AWS secret key
aws_secret_access_key = "AKIAIOSFODNN7EXAMPLE"

# [B324] Use of insecure MD5 hashing
import hashlib
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()
