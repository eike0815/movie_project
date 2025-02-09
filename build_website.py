import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def seralize_movie(obj):
    """here every fox gets an own card written """
    output = ''
    output += '<li class="cards__item">\n'
    try:
        output += f'<div class="card_title"><strong>Name:</strong> {obj[0]}</div>\n'
    except KeyError:
        pass
    output += '<p class="card__text">'
    try:
        output += f'<strong>Rating:</strong> {obj[1]["rating"]}<br/>\n'
    except KeyError:
        pass
    output += f'<img src ="{obj[1]["poster"]}">'
    output += '</p>'
    output += '</li>'
    return output


def building_all_cards(cards):
    """here we add together all film cards to on file"""
    output = ""
    for title in cards.items():
        output += seralize_movie(title)
    return output

def bring_movies_to_html(list_of_cards):
    """here the placeholder is replaced by the actual new animal list created in building_all_cards"""
    with open('_static/index_template.html',"r")as file:
      page = file.read()
    new_html=page.replace("__TEMPLATE_MOVIE_GRID__", list_of_cards)
    with open ("_static/movie_template.html", "w") as file:
        file.write(new_html)
        return "_static/movie_template.html"

def make_it_html():
    """
    this function coordinates the order of the function needed to bild the html
    """
    movie_list = load_data('movie_data.json')
    movie_on_card = building_all_cards(movie_list)
    bring_movies_to_html(movie_on_card)

