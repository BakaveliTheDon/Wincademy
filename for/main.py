# from operator import contains
# from numpy import full
from helpers import get_countries



""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

def shortest_names(countries):
    shortest_length = (len(min(countries, key=len)))
    shortest_names = []
    
    
    for x in countries:
        if len(x) <= shortest_length:
           shortest_names.append(x)
    return shortest_names


def most_vowels(countries):
    vows = 'aeiou'
    top_countries = []
    top = []
    for country in countries:
        vowels = 0
        for letter in country:
            if letter.lower() in vows:
                vowels += 1
                
        top_countries.append([vowels, country])
        top_countries.sort(reverse=True)
        new_list = top_countries[:3]
    for vowels, country in new_list:
        top.append(country)

    return top

def alphabet_set(countries):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alph_list = []
    alpha_countries = []
    special_characters = ',.() '
    sorted_on_len = list(sorted(countries, key=len, reverse=True))
    for country in sorted_on_len:
        for letter in country:
            if letter.lower() in alphabet:
                if letter.lower() not in alph_list:
                    alph_list.append(letter.lower())
                    if country not in alpha_countries:
                        alpha_countries.append(country)            
                
                
    
    return alpha_countries  
   

            



# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """

    shortest_names(countries)
    print(most_vowels(countries))
    alphabet_set(countries)

