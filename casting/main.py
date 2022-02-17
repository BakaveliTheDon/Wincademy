# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

leek_price = 2
print('Leek is ' + str(leek_price) + ' euro per kilo.')

order = 'leek 4'
order.find('4')
order_amount = int(order[5])
sum_total = order_amount * leek_price
print(sum_total)

broccoli_price = 2.34
order_2 = 'broccoli 1.6'
order_2.find('1.6')
order2_amount = float(order_2[9:12])
sum_total_broccoli = float(broccoli_price) * order2_amount
rounded_sum = round(sum_total_broccoli, 2)
print(str(order2_amount) + 'kg broccoli costs ' + str(rounded_sum) + 'e' )