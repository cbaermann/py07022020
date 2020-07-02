import requests 
# get_api_request = requests.get("https://api.nasa.gov/planetary/apod?api_key=MiXU3cFZ63yO9b4xcRiLEYsgBbl6nxhuwSawKcRC")
get_api_request = requests.get("https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY#")

response_data = get_api_request.json()

print(response_data["near_earth_objects"]["name"])