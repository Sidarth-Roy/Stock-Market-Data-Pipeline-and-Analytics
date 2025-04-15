import requests

API_KEY = 'de38ca7dd717eb0fb28cb4f3e3d7a393'
BASE_URL = 'https://api.stlouisfed.org/fred/series/search'
SEARCH_TEXT = 'economic'  # Adjust your search text as needed
LIMIT = 100  # Number of series to retrieve

params = {
    'api_key': API_KEY,
    'search_text': SEARCH_TEXT,
    'file_type': 'json'
}

response = requests.get(BASE_URL, params=params)
data = response.json()

series_list = [
    {"series_id": item['id'], "name": item['title']}
    for item in data.get('seriess', [])
]
print(series_list)

# Now, series_list contains dictionaries with 'series_id' and 'name' keys
