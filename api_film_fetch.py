import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('API_KEY')
headers = {'X-Api-Key': API_KEY}
def fetch_data(film_title):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    },
    """
    url = f'http://www.omdbapi.com/?apikey={API_KEY}&t={film_title}'
    req =requests.get(url, headers = headers)
    return req.json()

print(fetch_data("the joker"))
print('hihi')
#fetch_data("the joker")['Search'][0]#this is here for testing

Title = fetch_data("the joker")['Title']
Year = fetch_data("the joker")['Year']
Rated = fetch_data("the joker")['Rated']
poster = fetch_data("the joker")['Poster']

