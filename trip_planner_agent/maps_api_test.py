#%%
import requests
import json

def get_route_info():
    # Load API key from JSON file
    with open("google_maps_api.json", "r") as f:
        key_data = json.load(f)
        api_key = key_data["api_key"]

    # API endpoint and parameters
    url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": "H8MW+WP Kolkata India",
        "destination": "GCG2+3M Kolkata India",
        "key": api_key
    }

    # Send request
    response = requests.get(url, params=params)
    data = response.json()

    # Handle errors
    if data["status"] != "OK":
        print("Error:", data["status"])
        return

    # Extract distance and duration
    leg = data["routes"][0]["legs"][0]
    distance_text = leg["distance"]["text"]
    duration_text = leg["duration"]["text"]

    print(f"Distance: {distance_text}")
    print(f"Duration: {duration_text}")

if __name__ == "__main__":
    get_route_info()

# %%
