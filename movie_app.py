import random
import movie_storage
from statistics import median, mean
from storage_json import StorageJson

class MovieApp:
    def __init__(self, storage):
        self._storage = storage



    def _command_list_movies(self):
        movie = self._storage.list_movies()
        ...
    def _command_add_movie(self):
        """
        the function adds a new entry to a dictionary (movie_dict ({'title':{'rating':float , 'year' : int}, ...}))
        by entering the title(key) and it´s rating (value),
        afterward it saves the data into a json-file.
        """
        movie_dict = {}
        movi_stats = {}
        key = input("enter the movies name: ")
        while len(key) == 0:
            print("the namen of the movie can´t be empty")
            key = input("enter the movies name: ")
        while key in movie_storage.get_movies():
            print("Movie already exists. Add another title.")
            key = input("enter the movies name: ")
        bad_input = True
        while bad_input:
            try:
                rating = float(input("enter the movies rating: "))
                while 0 > rating or rating > 10:
                    print("the rating is not valid. pleas enter a valid rating between 0 and 10")
                    rating = float(input("enter the movies rating: "))
                movi_stats["rating"] = rating
                bad_input = False
            except ValueError:
                print("this is not a valid number")
        bad_input = True
        while bad_input:
            try:
                year = int(input("enter the movies year: "))
                while 1888 > year or year > 2025:
                    print("the year is not valid. pleas enter a valid year")
                    year = int(input("enter the movies year: "))
                movi_stats["year"] = year
                movie_dict[key] = movi_stats
                movie_storage.add_movie(movie_dict)
                bad_input = False
            except ValueError:
                print("this is not a valid number")

    def _command_delete_movie(self):
        """
        with the function the user can delete an entry from a json-file
        by entering the name of the movie which shall be deleted.
        the function than handles the data in a
        movie_dict dictionary that looks like this {'title':{'rating':float , 'year' : int}, ...}
        """
        key = input("Enter movie name to delete: ")
        while key not in movie_storage.get_movies():
            print("Movie is not found, enter valid film-name")
            key = input("Enter movie name to delete: ")
        movie_storage.delete_movie(key)
        print(f" Movie {key} successfully deleted")
        return


    def _command_update_movie(self):
        """
        with the function the rating of an existing movie-entry (in the json-file ({'title':{'rating':float , 'year' : int}, ...})) can be updated
        by entering the name of the movie and afterward the new rating.
        """
        key = input("Enter movie name: ")
        while key not in movie_storage.get_movies():
            print("Movie is not found, enter valid film-name or add the film you want")
            key = input("Enter movie name: ")
        value = float(input("Enter new movie rating (0-10): "))
        movie_storage.update_movie(key, value)
        print(f" Movie {key} successfully updated")
        return


    def _command_movie_stats(self):
        """
        with this function you analyse statistics of the given json-file ({'title':{'rating':float , 'year' : int}, ...}).
        if there are multiple entries with the same lowest or highest rating,
        the function lists them all. the maximum and minimum rating
        """
        movie_dict = movie_storage.get_movies()
        rating_dict = {}
        for movie in movie_dict:
            rating_dict[movie] = movie_dict[movie]['rating']
        print(f" Avarage rating is: {round(mean(rating_dict.values()), 2)}")
        print(f" Median rating is: {round(median(rating_dict.values()), 2)}")
        temp = max(rating_dict.values())
        res = [key for key in rating_dict if rating_dict[key] == temp]
        for i in range(0, len(res)):
            print(f" Best movie(s):{res[i]}, with {round(temp, 2)} rating, from the year {movie_dict[res[i]]['year']}")
        temp = min(rating_dict.values())
        res = [key for key in rating_dict if rating_dict[key] == temp]
        for i in range(0, len(res)):
            print(
                f" Worst movie(s): {res[i]}, with  {round(temp, 2)} rating, from the year {movie_dict[res[i]]['year']}")


    def _command_random_movie(self):
        """
        the function pics a random entry of the given json-file ({'title':{'rating':float , 'year' : int}, ...})
        and prints the title plus its rating
        """
        movie_dict = movie_storage.get_movies()
        film = random.choice(list(movie_dict))
        rating = movie_dict[film]['rating']
        print(f"Your movie for tonight: {film}, it's rated {rating}")
        return


    def _command_search_movie(self):
        """
        the function allows to search for an entry in the
        json-file({'title':{'rating':float , 'year' : int}, ...}).
        it transforms the entered title (or part title)
        into lower caps and prints out
        all entries which includes the entry.
        """
        result = "None"
        title = input("Enter part of movie name: ").lower()
        dict_movies = movie_storage.get_movies()
        for key in dict_movies:
            if title in key.lower():
                result = key
                print(key, dict_movies[key]['rating'])


    def _generate_website(self):
        ...

    def run(self):
        pass
# Print menu
    # Get use command
    # Execute command
