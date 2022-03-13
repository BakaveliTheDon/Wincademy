# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

from os import remove


def alphabetical_order(list_of_movies):
    list_of_movies.sort()
    return list_of_movies


movies = ['Die Hard', 'Scream', '8 mile', 'Ghost', 'A true Story', 'X-men']

alphabetical_order(movies)



list_of_wins = ['Fiddler on the Roof', 'Jaws', 'Star Wars', 'Memoirs of a Geisha']
lower_list = [name.lower() for name in list_of_wins]

def won_golden_globe(film_name):
    film_name = film_name.lower()
    if film_name in lower_list:
        return True
    return False    
won_golden_globe('Memoirs of a Geisha')


def remove_toto_albums(list):
    toto_album = ['Fahrenheit', 'The Seventh One', 'Toto XX', 'Falling in Between', '35th Anniversary – Live in Poland', 'Toto XIV,' 'Old Is New', 
                 'Old Is New', '40 Tours Around the Sun', 'With a Little Help from My Friends']
    toto_free_list = [x for x in list if x not in toto_album]
    return toto_free_list

list_of_albums = ['Early Years', 'Vertigo', 'The Seventh One', 'Tears']         
remove_toto_albums(list_of_albums)
    
         
