import requests

# Endpoint of the microservice
MICROSERVICE_URL = "http://127.0.0.1:5000/random_character_image"

def test_microservice():
    try:
        # Send a request to the microservice
        print("Calling Microservice A...")
        response = requests.get(MICROSERVICE_URL)

        # Check response
        if response.status_code == 200:
            data = response.json()
            print(f"Microservice Response: {data}")
        else:
            print(f"Error: Microservice returned status code {response.status_code}")
    except Exception as e:
        print(f"Error while calling microservice: {e}")

if __name__ == "__main__":
    test_microservice()
