import requests

def call_api(base_url, payload):
    try:
        response = requests.get(base_url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        return None

if __name__ == "__main__":
    url = "http://127.0.0.1:8081/roll_dice"

    data = {
        "probabilities": [0.1, 0.2, 0.3, 0.1, 0.2, 0.1],
        "number_of_random": 10
    }

    print("Calling the API with the following payload:")
    print(data)

    result = call_api(url, data)
    if result:
        print("\nResponse from server:")
        print(f"Status     : {result.get('status')}")
        print(f"Rolls      : {result.get('number_of_random')}")
        print(f"Results    : {result.get('results')}")
