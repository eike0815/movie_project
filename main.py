import random
import movie_storage
from statistics import median, mean

def list_of_movies():
    """
    the function takes a dictionary with films and lists them.
    the function loads the data from a json file and handles it in a
    movie_dict: that looks like this {'title':{'rating':float , 'year' : int}, ...}
    """
    movie_dict = movie_storage.get_movies()
    print(f"{len(movie_dict)} movies in total")
    for movie in movie_dict:
        print(movie,":",movie_dict[movie]['rating'],":",movie_dict[movie]['year'])
    return

#2 Add a movie
def add_movie():
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


#3 Delete a movie
def delete_movie():
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


#4 Update a movie
def update_movie():
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


#5 statistics about the movies in the databas
def all_stats():
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
    for i in range(0,len(res)):
        print(f" Best movie(s):{res[i]}, with {round(temp, 2)} rating, from the year {movie_dict[res[i]]['year']}")
    temp = min(rating_dict.values())
    res = [key for key in rating_dict if rating_dict[key] == temp]
    for i in range(0,len(res)):
        print(f" Worst movie(s): {res[i]}, with  {round(temp, 2)} rating, from the year {movie_dict[res[i]]['year']}")


#6 random movie
def random_movie():
    """
    the function pics a random entry of the given json-file ({'title':{'rating':float , 'year' : int}, ...})
    and prints the title plus its rating
    """
    movie_dict = movie_storage.get_movies()
    film = random.choice(list(movie_dict))
    rating = movie_dict[film]['rating']
    print(f"Your movie for tonight: {film}, it's rated {rating}")
    return


#7 search a movie
def search_movie():
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
            print(key , dict_movies[key]['rating'])


#8 movies sorted by rating
def movie_rating():
    """
    the function lists the films of the
    json-file ({'title':{'rating':float , 'year' : int}, ...})
    and prints from top rating to lowest rating.
    """
    movie_dict = movie_storage.get_movies()
    rating_dict = {}
    print("Films sorted by rating")
    for movie in movie_dict:
        rating_dict[movie] = movie_dict[movie]['rating']
    for index in range(0,len(rating_dict)):
        highest_rating = 0
        for key, value  in rating_dict.items():
            if value > highest_rating:
                highest_rating = value
                movie_with_highest_rating = key
        print(movie_with_highest_rating, ":", highest_rating, ":", movie_dict[movie_with_highest_rating]['year'])
        del rating_dict[movie_with_highest_rating]


def menu():
    """
    this function prints the menu the user is choosing from.
    """
    print("Menu: \n"
          " 0. Exit \n 1. List movies \n 2. Add movie \n 3. Delete movie \n 4. Update movie"
          "\n 5. Stats \n 6. Random movie \n 7. Search movie \n 8. Movies sorted by rating")
    return

#main function
def main():

    go_on =""
    print("********** My Movies Database **********")
    while True:
        menu()
        text = int(input(" Enter choice (0-8): "))
        if text == 0:
            print("Bye!")
            break
        if text == 1:
            list_of_movies()
        elif text == 2:
            add_movie()
        elif text == 3:
            delete_movie()
        elif text == 4:
            update_movie()
        elif text == 5:
            all_stats()
        elif text == 6:
            random_movie()
        elif text == 7:
            search_movie()
        elif text == 8:
            movie_rating()
            go_on= input("press enter to continue")


if __name__ == "__main__":
    main()
