# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, greeting_template='Hello, <name>!'):
    
    greetings = greeting_template.replace('<name>', name)
   
    return greetings


greet('Doc')    
greet('Bob', "What's up, <name>!")


def force(mass, planet='earth'):
    body = {'sun': 274,
	'jupiter' : 24.9,
    'neptune' : 11.2,
	'saturn' : 10.4,
    'earth'	: 9.8,
    'uranus' : 8.9,
	'venus' : 8.9,
	'mars' : 3.7,
	'mercury' : 3.7,
	'moon' : 1.6,
	'pluto'	: 0.6}
    calculation = mass * body[planet]
    return calculation


force(19889944454, planet='neptune')


def pull(m1, m2, d):
    force = (6.674 * 10**-11) * float((m1 * m2)/d**2)
    return force

pull(800, 1500, 3)