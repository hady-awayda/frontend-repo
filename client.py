import requests
import yaml

def read_config():
    url = 'https://raw.githubusercontent.com/hady-awayda/fullstack-repo/main/config.yaml'

    response = requests.get(url)

    if response.status_code == 200:
        try:
            config = yaml.safe_load(response.content)
            print("YAML content successfully loaded:", config)
            # Accessing nested 'run_localhost' key inside 'config'
            variable = config.get('config', {}).get('run_localhost')
            if variable is True:
                print("Running on localhost")
            else:
                print("Not running on localhost")
        except yaml.YAMLError as e:
            print("Error parsing YAML:", e)
        except AttributeError as e:
            print("Error accessing 'run_localhost' key. Is the YAML content a dictionary?", e)
    else:
        print(f"Failed to fetch the file. Status code: {response.status_code}")

if __name__ == "__main__":
    read_config()
