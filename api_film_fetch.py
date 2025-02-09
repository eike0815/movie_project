import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('API_KEY')
headers = {'X-Api-Key': API_KEY}
def fetch_data(film_title):
    """
    Fetches the movie data.
    Returns: a list of movies, each animal is a dictionary
    """
    url = f'http://www.omdbapi.com/?apikey={API_KEY}&t={film_title}'
    req =requests.get(url, headers = headers)
    return req.json()

"""
this was just for testing:
Title = fetch_data("the joker")['Title']
Year = fetch_data("the joker")['Year']
Rated = fetch_data("the joker")['imdbRating']
poster = fetch_data("the joker")['Poster']
"""

