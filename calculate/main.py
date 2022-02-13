# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line
broccoli = 2
leek = 2
potato = 3
brussel_sprout = 7

grocery_list = {
    'broccoli' : 2,
    "leek" : 2,
    "potato" : 3,
    "brussel_sprout" : 7
}

# def total():
#     (sum_one_each) = broccoli + leek + potato + brussel_sprout
#     print(f'totale som is {sum_one_each}')
#     avg_price = sum_one_each /len(grocery_list)
#     print(f'average price per item is {avg_price}')

# total()

sum_one_each = broccoli + leek + potato + brussel_sprout
avg_price = sum_one_each /len(grocery_list)
num_potatoes = 7 
num_broccolis = 5 
num_leeks = 2 
num_brussel_sprouts = 10 

sum_total = float((num_potatoes * potato) + (num_broccolis * broccoli) + (num_leeks * leek) + (num_brussel_sprouts * brussel_sprout))
# print(sum_total)
discount_percentage = 30
discounted_sum_total = float(sum_total - (sum_total * (discount_percentage/100)))
print(discounted_sum_total)