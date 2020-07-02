import requests 

with open("../myapi.key", "r") as secretkey:
    myapikey = secretkey.read()

def main():
    search_date_input = input("What date are you searching for? YYYY-MM-DD Format only.\n")
    
    asteroid_url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date=" \
        f"{search_date_input}&end_date={search_date_input}&api_key={myapikey}" 
    
    mars_url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=" \
            f"{search_date_input}&api_key={myapikey}"
    
    asteroid_api_request = requests.get(asteroid_url)
    mars_api_request = requests.get(mars_url)

    if asteroid_api_request.status_code != 200:
        sys.exit("API Status Code Error, check API Provider.")

    asteroid_api_data = asteroid_api_request.json()
    mars_api_data = mars_api_request.json()

    number_of_asteroids = asteroid_api_data['element_count']
    mars_photo_json_pull = mars_api_data['photos']
    mars_photo = mars_photo_json_pull[0]["img_src"]

    print(f"There were {number_of_asteroids} asteroids monitored on this date by NASA.")
    print(f"Image of Mars URL: {mars_photo}")


main()