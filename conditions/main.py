# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line




def farm_action(weather, time_of_day, cow_milking_status, location_of_the_cows, season, slurry_tank, grass_status):
    
    if weather == 'rainy':
        if time_of_day != 'day':
            if location_of_the_cows != 'cowshed':
                return 'take cows to cowshed'   

    
    # if location_of_the_cows != 'cowshed':
    #     if time_of_day != 'day' or weather == 'rainy':
    #         return 'take cows to cowshed'   
   
    if cow_milking_status:
        if location_of_the_cows == 'cowshed':
            return 'milk cows'
        elif location_of_the_cows == 'pasture':
            # return print("take cows to cowshed \nmilk cows \ntake cows back to pasture")
            result = ('take cows to cowshed\nmilk cows\ntake cows back to pasture')
            return result
             

    if slurry_tank:
        if location_of_the_cows != 'pasture':
            if weather != 'sunny' or 'windy':
                # return print('fertilize pasture \ntake cows back to pasture')
                return 'fertilize pasture'
            
   
    if grass_status:
        if season == 'spring':
            if weather == 'sunny':
                if location_of_the_cows != 'pasture':
                    # return print('mow grass \ntake cows back to pasture')
                    return 'mow grass\ntake cows back to pasture'
                    

    return 'wait'                

farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True)
farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True)
farm_action('windy', 'night', True, 'cowshed', 'winter', True, True)
print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))


