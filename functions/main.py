# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line


def greet(person):

    return f'Hello, {person}!'


greet('babak')    


def add(x,y,z):
    sum_float = float(x+y+z)
    # sum_int = int(x+y+z)
    return sum_float

add(5,6.6,7)

def positive(number):
    if number > 0:
        return True
    else: 
        return False    

positive(-5)        

def negative(number):
    if number < 0:
        return True
    else: 
        return False    
   
negative(-4)   