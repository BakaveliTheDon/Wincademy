# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line
import this
import time
import math
import sys
import datetime
from greet import supergreeting

def wait(seconds):
    time.sleep(seconds)
    return None


def my_sin(number):
    a = math.sin(number)
    return a


def iso_now():
    datetimetoday = datetime.datetime.now()
    return datetimetoday.strftime('%Y-%m-%dT%H:%M')


def platform():
    os = sys.platform
    return os

def supergreeting_wrapper(name):
    return supergreeting(name)



