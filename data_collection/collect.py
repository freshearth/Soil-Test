import requests
import json

def fetch_soil_test_data(api_url, params=None):
    """
    Fetch soil test data from an API.
    """
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {api_url}: {e}")
        return None

def fetch_land_management_data(api_url, params=None):
    """
    Fetch land management data from an API.
    """
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {api_url}: {e}")
        return None

def aggregate_data(soil_test_data, land_management_data):
    """
    Aggregate data from different sources into a unified format.
    """
    aggregated_data = {
        "soil_test_data": soil_test_data,
        "land_management_data": land_management_data
    }
    return aggregated_data

if __name__ == "__main__":
    # Example usage
    soil_test_api_url = "https://api.example.com/soil-tests"
    land_management_api_url = "https://api.example.com/land-management"
    
    soil_test_data = fetch_soil_test_data(soil_test_api_url)
    land_management_data = fetch_land_management_data(land_management_api_url)
    
    if soil_test_data and land_management_data:
        aggregated_data = aggregate_data(soil_test_data, land_management_data)
        print("Aggregated Data:", json.dumps(aggregated_data, indent=4))
    else:
        print("Failed to fetch data from one or more APIs.")
