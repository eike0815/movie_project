from istorage import IStorage
import json


class StorageJson(IStorage):
    def __init__(self, file_path):
        """
        the function initiates the class.
        it rather checks if the filepath is already existing and,
        if not, writes a new one.
        """
        self.file_path = file_path
        try:
            with open(f'{self.file_path}', 'r') as file:
                return
        except FileNotFoundError:
            with open(f'{self.file_path}', 'w') as file:
                return

    def write_movies(self, movies):
        """
        this function writes movies  to actualise the existing json.
        """
        with open(f"{self.file_path}", 'w') as file:
            json.dump(movies, file)

    def list_movies(self):
        """
        this function lists all movies from the storage.
        """
        with open(f'{self.file_path}', 'r') as file:
            movie_dict =  json.load(file)
            for key, value in movie_dict.items():
                print(f"{key}: {value['rating']} {value['year']}")


    @property
    def movies(self):
        """
        this function loads the storage.
        """
        with open(f'{self.file_path}', 'r') as file:
            return json.load(file)

    @movies.setter
    def movies(self, new_movie):
        """
        this function writes a new movie into the existing storage by using the function write_movie
        """
        self.write_movies(new_movie)


    def add_movie(self, dict):
        movies = self.movies
        movies.update(dict)
        #movies[title] = {'year': year, 'rating': rating}
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



