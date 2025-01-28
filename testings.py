from storage_json import StorageJson

storage = StorageJson("movie_data.json")
#print(storage.list_movies())
#storage.add_movie( "A",2014, 3.5, None)
#print(storage.list_movies())
sample = ( "AAAAAAAAAAAAAAAAAAAAAAAAAAAAA",2014, 3.5)
storage.add_movie( "BBBBBBBBBBB",2014, 3.5)
print(storage.list_movies())
#storage.delete_movie('AAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
storage.update_movie("BBBBBBBBBBB",10000)
print(storage.list_movies())

"""
def list_movies(self):
    with open(f'{self.file_path}', 'r') as file:
        return json.load(file)
def get_all_products(self):
    """

  #
#
#this function checks the status of each product and
 #   prints afterward the active products of the store.
  #  to do so it communicates with the "quantitative" functions of the product class
"""
    print("------")
    counter = 1
    for index in range(len(self.product_list)):
        if self.product_list[index].is_active():
            print(f"{counter}.", end=" ")
            print(f"{self.product_list[index].show()},")
            #   f" Price: ${self.product_list[index].price}, "
            #    f"Quantity: {self.product_list[index].quantity}")
            counter += 1
    print("------")

"""