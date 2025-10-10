#%%
import requests
import json

def get_route_for_mode(mode, origin, destination):
    """
    Get route information for a specific travel mode
    
    Args:
        mode (str): Travel mode (DRIVE, WALK, BICYCLE, TRANSIT)
        origin (str): Starting address
        destination (str): Destination address
    
    Returns:
        dict: Route information including distance, duration, and toll info
    """
    # Load API key from JSON file
    with open("/Users/vamseekrishna/Desktop/personal_projects/AI_agents/trip_planner_agent/google_maps_api.json", "r") as f:
        key_data = json.load(f)
        api_key = key_data["api_key"]

    # Routes API endpoint
    url = "https://routes.googleapis.com/directions/v2:computeRoutes"

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": api_key,
        "X-Goog-FieldMask": "routes.duration,routes.distanceMeters,routes.travelAdvisory.tollInfo"
    }

    body = {
        "origin": {
            "address": origin
        },
        "destination": {
            "address": destination
        },
        "travelMode": mode,
        # use real-time traffic
    }

    # Send request
    response = requests.post(url, headers=headers, json=body)
    data = response.json()

    if "routes" not in data:
        print(f"Error for {mode} mode:", data)
        return None

    # Extract distance and duration
    route = data["routes"][0]
    distance_km = route["distanceMeters"] / 1000
    duration_sec = int(route["duration"].replace("s", ""))

    duration_minutes = duration_sec / 60
    
    # Format duration based on length
    if duration_minutes < 60:
        duration_display = f"{duration_minutes:.1f} minutes"
    else:
        duration_hours = duration_minutes / 60
        duration_display = f"{duration_hours:.1f} hours"
    
    result = {
        "mode": mode,
        "distance_km": distance_km,
        "duration_minutes": duration_minutes,
        "duration_display": duration_display,
        "has_tolls": False
    }

    # Optional: toll info if available
    if "travelAdvisory" in route and "tollInfo" in route["travelAdvisory"]:
        result["has_tolls"] = True

    return result

#this is a tool that gets the directions for all available travel modes
def get_directions(origin:str, destination:str):
    """
    Get directions for all available travel modes
    
    Args:
        origin (str): Starting address
        destination (str): Destination address
    """
    # Available travel modes
    modes = ["DRIVE", "WALK", "BICYCLE", "TRANSIT"]
    
    print(f"Getting directions from: {origin}")
    print(f"To: {destination}")
    print("=" * 50)
    
    results = []
    
    for mode in modes:
        print(f"\n{mode} Mode:")
        print("-" * 20)
        
        result = get_route_for_mode(mode, origin, destination)
        
        if result:
            print(f"Distance: {result['distance_km']:.1f} km")
            print(f"Duration: {result['duration_display']}")
            
            if result['has_tolls']:
                print("This route includes tolls 💰")
            
            results.append(result)
        else:
            print(f"No route available for {mode} mode")
    
    return results



# %%
# if __name__ == "__main__":
#     get_directions("2726 phillips dr dallas", "dfw airport")

#add modes of transport
#add cost of transport
#search the web for popular modes of transport
