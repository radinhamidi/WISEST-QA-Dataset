import json
import requests

def fetch_json(task, version='latest'):
    if task not in ['qa', 'dpr']:
        raise ValueError("task must be one of 'qa' or 'dpr'")
    elif task == 'qa':
        url = 'https://wisest-data.ls3.rnet.torontomu.ca/qa_data/'
    elif task == 'dpr':
        url = 'https://wisest-data.ls3.rnet.torontomu.ca/dpr_data/'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None
