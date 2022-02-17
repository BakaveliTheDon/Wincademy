# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

from ntpath import join
import re


NL_goal1 = 'Ruud Gullit'
NL_goal2 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = NL_goal1 + " " + str(goal_0) +', ' + NL_goal2 +  " " + str(goal_1)
print(scorers)

report = f'{NL_goal1} scored in the {goal_0}nd minute\n{NL_goal2} scored in the {goal_1}th minute'
print(report)

player = 'Marco van Basten'
first_name = player[:player.find(' ')]
print(first_name)

# last_name = player[len(first_name):]
last_name = player[player.find(' ')+1:]
print(last_name)
last_name_len = len(last_name)
name_short = first_name[0] + '. ' + last_name
print(f'{first_name[0]}. {last_name}')

chant = (len(first_name) * (first_name +'!'+' '))[:-1]
print(chant)

good_chant = (chant[-1] != ' ')
print(good_chant)
# good_chant = (chant[:-1] != ' ')
# print(len(good_chant))

