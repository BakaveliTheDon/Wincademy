# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line

def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport = {
    'name' : name,
    'date_of_birth' : date_of_birth,
    'place_of_birth' : place_of_birth,
    'height' : height,
    'nationality' : nationality,
     }

    return passport





def add_stamp(passport, country):
    
    if 'stamps' not in passport:

        passport['stamps'] = [country]
    
    if country not in passport['stamps']:
        if country is not passport['nationality']:
            passport['stamps'].append(country)
            return passport

    if country in passport['stamps']:
        return passport

    return passport['stamps'] 

Babak = create_passport(name='Babak', date_of_birth='27-03-1983', place_of_birth='Tehran', height=1.70, nationality='Iran')
add_stamp(Babak, 'Zimbabwe')
add_stamp(Babak, 'Turkey')
print(Babak['stamps'])


def add_biometric_data(passport, type, value, date):

    first_biometric = {'biometric':{type: {'date': date, 'value': value}}}

    if 'biometric' not in passport:

        passport.update(first_biometric)

   
        return passport    



    if 'biometric' in passport:
        
        new_biometric = {type: {'date': date, 'value': value}}
        passport['biometric'].update(new_biometric)

        return passport

omari = create_passport("Omari Muchumba", "1995-07-16", "Kampala", 184.31, "Uganda")
omari = add_biometric_data(omari, "eye_color_left", "blue", "2020-05-05")
omari = add_biometric_data(omari, "eye_color_right", "blue", "2020-05-05")
print(omari)
fingerprint_data = {
    "left_pinky": "2378945",
    "left_ring": "2349081",
    "left_middle": "132890",
    "left_index": "9823234",
    "left_thumb": "0924131",
    "right_thumb": "6234923",
    "right_index": "13249734",
    "right_middle": "34023784",
    "right_ring": "12332538",
    "right_pinky": "32458970",}

omari = add_biometric_data(omari, "finger_prints", fingerprint_data, "2022-01-12")
print(omari)    