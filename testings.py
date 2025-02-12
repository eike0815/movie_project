from movie_app import MovieApp
from storage.storage_json import StorageJson

storage = StorageJson('movie_data.json')
movie_app = MovieApp(storage)
#print(storage.list_movies())
#print(movie_app._command_add_movie())
#print(movie_app._command_list_movies())
#print(movie_app._command_delete_movie())
#print(movie_app._command_movie_stats())
#print(movie_app._command_random_movie())
#print(movie_app._command_search_movie())
movie_app.run()
#storage = StorageJson("movie_data.json")
#print(storage.list_movies())
#storage.add_movie( "A",2014, 3.5, None)
#print(storage.list_movies())
#sample = ( "AAAAAAAAAAAAAAAAAAAAAAAAAAAAA",2014, 3.5)
#storage.add_movie( "BBBBBBBBBBB",2014, 3.5)
#print(storage.list_movies())
#storage.delete_movie('AAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
#storage.update_movie("BBBBBBBBBBB",10000)
#print(storage.list_movies())

