from istorage import IStorage
import json


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        try:
            with open(f'{self.file_path}', 'r') as file:
                return
        except FileNotFoundError:
            with open(f'{self.file_path}', 'w') as file:
                return

    def write_movies(self, movies):
        with open(f"{self.file_path}", 'w') as file:
            json.dump(movies, file)

    def list_movies(self):
        with open(f'{self.file_path}', 'r') as file:
            movie_dict =  json.load(file)
            for key, value in movie_dict.items():
                print(f"{key}: {value['rating']} {value['year']}")


    @property
    def movies(self):
        with open(f'{self.file_path}', 'r') as file:
            return json.load(file)

    @movies.setter
    def movies(self, new_movie):
        self.write_movies(new_movie)


    def add_movie(self, title, year, rating):
        movies = self.movies
        movies[title] = {'year': year, 'rating': rating}
        self.movies = movies


    def delete_movie(self, title):
        movies = self.movies
        del movies[title]
        self.movies = movies

    def update_movie(self, title, rating):
        """
        Updates a movie from the movies database.
        Loads the information from the JSON file, updates the movie,
        and saves it. The function doesn't need to validate the input.
        """
        movies = self.movies
        movies[title]['rating'] = rating
        self.movies = movies



