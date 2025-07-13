# import subprocess
# import pickle
# import os

# # [B602] Subprocess with shell=True - potential command injection
# def run_command(cmd):
#     subprocess.call(cmd, shell=True)

# # [B403] Pickle used to deserialize data - arbitrary code execution risk
# def load_data_from_file(filename):
#     with open(filename, 'rb') as f:
#         data = pickle.load(f)
#     return data

# # [B105] Hardcoded password
# def connect_to_db():
#     password = "supersecret123"
#     print("Connecting with password:", password)

# # [B108] Hardcoded AWS secret key
# aws_secret_access_key = "AKIAIOSFODNN7EXAMPLE"

# # [B324] Use of insecure MD5 hashing
# import hashlib
# def hash_password(password):
#     return hashlib.md5(password.encode()).hexdigest()
