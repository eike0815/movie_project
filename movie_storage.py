import json

def get_movies():
    try:
        with open('movie_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("File does not exist")


def save_movies(movies):
    with open('movie_data.json', 'w') as file:
        json.dump(movies, file)


#sample = {'the thing' : {'year' : 2023, 'rating' :3.4}}
def add_movie(sample):
        """ Adds a movie to the movies database """
        movies = get_movies()
        movies.update(sample)
        save_movies(movies)
        # Add the movie and save the data to the JSON file

#add_movie(sample)
def delete_movie(title):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    del movies[title]
    save_movies(movies)

#delete_movie('the clown')
def update_movie(title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    movies[title]['rating'] = rating
    save_movies(movies)


