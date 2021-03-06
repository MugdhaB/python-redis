import logging
from random import choice
import requests
import config

mars_rover_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?'

def get_mars_photo(day):
    params = {"earth_date": day, "api_key": config.nasa_demo_key}
    print("Fetching a mars image for the day: ", day)
    response = requests.get(mars_rover_url, params=params).json()
    photos = response['photos']
    #Choose random photo
    image_url = choice(photos)['img_src']
    print("Image Url is:", image_url)
    return image_url
