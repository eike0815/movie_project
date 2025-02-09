import random
import api_film_fetch as aff
from statistics import median, mean
import build_website
from storage_json import StorageJson

class MovieApp:
    def __init__(self, storage):
        self._storage = storage


    def _command_list_movies(self):
        movie = self._storage.list_movies()


    def _command_add_movie(self):
        """
        the function adds a new entry to a dictionary (movie_dict ({'title':{'rating':float , 'year' : int}, ...}))
        by entering the title(key) and it´s rating (value),
        afterward it saves the data into a json-file.
        """
        movie_dict = {}
        movi_stats = {}
        title = input("enter the movies name: ")
        key = aff.fetch_data(title)['Title']
        print(aff.fetch_data(title))
        while len(key) == 0:
            print("the name of the movie can´t be empty")
            key = input("enter the movies name: ")
        while key in self._storage.movies:
            print("Movie already exists. Add another title.")
            key = input("enter the movies name: ")
        bad_input = True
        while bad_input:
            try:
                rating = aff.fetch_data(key)['imdbRating']
                movi_stats["rating"] = rating
                bad_input = False
            except ValueError:
                print("this is not a valid number")
        bad_input = True
        while bad_input:
            try:
                year = aff.fetch_data(key)['Year']
                movi_stats["year"] = year
                movie_dict[key] = movi_stats
                self._storage.add_movie(movie_dict)
                bad_input = False
            except ValueError:
                print("this is not a valid number")
        bad_input = True
        while bad_input:
            try:
                poster = aff.fetch_data(key)['Poster']
                movi_stats["poster"] = poster
                movie_dict[key] = movi_stats
                self._storage.add_movie(movie_dict)
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
        while key not in self._storage.movies:
            print("Movie is not found, enter valid film-name")
            key = input("Enter movie name to delete: ")
        self._storage.delete_movie(key)
        print(f" Movie {key} successfully deleted")
        return


    def _command_update_movie(self):
        """
        with the function the rating of an existing movie-entry (in the json-file ({'title':{'rating':float , 'year' : int}, ...})) can be updated
        by entering the name of the movie and afterward the new rating.
        """
        key = input("Enter movie name: ")
        while key not in self._storage.movies:
            print("Movie is not found, enter valid film-name or add the film you want")
            key = input("Enter movie name: ")
        value = float(input("Enter new movie rating (0-10): "))
        self._storage.update_movie(key, value)
        print(f" Movie {key} successfully updated")
        return


    def _command_movie_stats(self):
        """
        with this function you analyse statistics of the given json-file ({'title':{'rating':float , 'year' : int}, ...}).
        if there are multiple entries with the same lowest or highest rating,
        the function lists them all. the maximum and minimum rating
        """
        movie_dict = self._storage.movies
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
        movie_dict = self._storage.movies
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
        dict_movies = self._storage.movies
        for key in dict_movies:
            if title in key.lower():
                result = key
                print(key, dict_movies[key]['rating'])


    def _generate_website(self):
        ...

    def menu(self):
        """
        this function prints the menu the user is choosing from.
        """
        print("Menu: \n"
              " 0. Exit \n 1. List movies \n 2. Add movie \n 3. Delete movie \n 4. Update movie"
              "\n 5. Stats \n 6. Random movie \n 7. Search movie \n 8. Movies sorted by rating \n 9. Make a website")
        return

    def run(self):
        print("********** My Movies Database **********")
        while True:
            self.menu()
            text = int(input(" Enter choice (0-8): "))
            if text == 0:
                print("Bye!")
                break
            if text == 1:
                self._command_list_movies()
            elif text == 2:
                self._command_add_movie()
            elif text == 3:
                self._command_delete_movie()
            elif text == 4:
                self._command_update_movie()
            elif text == 5:
                self._command_movie_stats()
            elif text == 6:
                self._command_random_movie()
            elif text == 7:
                self._command_search_movie()
            elif text == 8:
                self._command_search_movie()
            elif text == 9:
                build_website.make_it_html()
                go_on = input("press enter to continue")
# Print menu
    # Get use command
    # Execute command
