# def greetings(person):
#     print(f'hello Sweet {person}')



# greetings('Babak')

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")
x = 1.1 + 2.2
print(x)
print(abs(x))
x = abs(x)
print(x)

len('test')


def double(x):
    doubled_x = x * 2
    return doubled_x


double(8)
double(9)
double('hey')    

def initials(name):
    first = name[0].upper()
    last = name[name.find(' ')+1:].upper()
    return f'{first}. {last}.'

initials('babak mirjalili')    