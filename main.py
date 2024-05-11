# pylint: disable=line-too-long
"""Main module"""
import json
import requests

CREDS_PATH = 'creds.json'

def get_places(location, key):
    """Gets 5 restaurants given the location

    Args:
        location (string): location eg. New York, LA
        api_key (string): API key
    
    Returns:
        list: json response of restaurants
    """

    url = 'https://api.yelp.com/v3/businesses/search'

    headers = {'Authorization': f'Bearer {key}',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', 
           "Upgrade-Insecure-Requests": "1","DNT": "1",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}

    params = {
        'location': location,
        'limit': 25
    }

    response = requests.get(url, headers=headers, params=params, timeout=30)

    if response.status_code == 200:
        return response.json()
    return None


def main():
    """Run the program"""
    with open(CREDS_PATH, 'r', encoding='utf-8') as json_file:
        loaded_data = json.load(json_file)

    # Extracting api_key into variable
    api_key = loaded_data.get("API_KEY", "")

    # Starting query and storing into variable
    location = input("Enter a location (e.g., 'New York City, NY'): \n")
    results = get_places(location, api_key)

    businesses = results.get('businesses', [])

    print(f'-------- Restaurants in {location} --------')
    for index, hash_map in enumerate(businesses):
        print(f'{index}. {hash_map["name"]}')

if __name__ == "__main__":
    main()
