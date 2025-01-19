import requests
import time

def make_api_call():
    url = "https://fake-mall-traffic-api.onrender.com/malls"
    try:
        response = requests.post(url)
        if response.status_code == 200:
            print("API call successful:", response.json())
        else:
            print(f"API call failed with status code {response.status_code}: {response.text}")
    except Exception as e:
        print(f"Error during API call: {e}")

if __name__ == "__main__":
    while True:
        make_api_call()
        time.sleep(40)


