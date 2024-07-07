# repo_A/client.py
from config_reader import read_config

config = read_config()

run_localhost = config.get('run_localhost', False)
client_timeout = config.get('client_timeout', 30)

if run_localhost:
    print("Running on localhost")
    # Your code to handle localhost logic

print(f"Client timeout is set to {client_timeout} seconds")
# Your client logic here
