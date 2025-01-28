import csv
from istorage import IStorage
import json

class StorageCSV(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        try:
            # Prüfen, ob die Datei existiert, ansonsten erstellen
            with open(self.file_path, 'r') as file:
                pass
        except FileNotFoundError:
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['title', 'year', 'rating'])  # Kopfzeile für CSV-Datei

    def write_movies(self, movies):
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['title', 'year', 'rating'])
            for title, details in movies.items():
                writer.writerow([title, details['year'], details['rating']])

    def list_movies(self):
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(f"{row['title']}: {row['rating']} {row['year']}")

    @property
    def movies(self):
        movies = {}
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                movies[row['title']] = {'year': row['year'], 'rating': row['rating']}
        return movies

    @movies.setter
    def movies(self, new_movie):
        self.write_movies(new_movie)

    def add_movie(self, movie_dict):
        movies = self.movies
        movies.update(movie_dict)
        self.movies = movies

    def delete_movie(self, title):
        movies = self.movies
        if title in movies:
            del movies[title]
        self.movies = movies

    def update_movie(self, title, rating):
        movies = self.movies
        if title in movies:
            movies[title]['rating'] = rating
        self.movies = movies

    def import_json(self, json_path):
        """Importiert Filme aus einer JSON-Datei und speichert sie als CSV."""
        with open(json_path, 'r') as file:
            movies = json.load(file)
        self.write_movies(movies)

# Beispiel der Nutzung:
# storage = StorageCSV('movies.csv')
# storage.add_movie({'Inception': {'year': '2010', 'rating': '8.8'}})
# storage.list_movies()
# storage.import_json('movies.json')
