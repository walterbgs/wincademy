# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
'''Part 1'''
# 1.Create a variable for every player
from os import remove
from xmlrpc.client import boolean


Player_1= "Ruud Gullit"
Player_2= "Marco van Basten"
# 2.Create a variable for each minute 
goal_0= 32
goal_1= 54
# 3.Create a string that reports on who scored when
scorers = Player_1 +' ' +str(goal_0)+', ' + Player_2 + ' '+str(goal_1)
print(scorers)
# 4.Create a single string
#report= f'{Player_1} scored in the {goal_0}nd  minute \n{Player_2} scored in the {goal_1}th minute'
report = Player_1+ ' scored in the '+str(goal_0)+'nd minute\n'+ Player_2+ ' scored in the '+str(goal_1)+'th minute'  
print(report)
'''Part 2'''
# 1.Choose a player
player="Ronald Koeman"
# 2. First name
find_space=player.find(" ")
first_name = player[0:find_space] 
#first_name_find = player.find(first_name)
print(first_name)
last_name = player[7: ]
print(last_name)
# 3. Last name 
#last_name_len_1= player[7: ],player.find (last_name), 
last_name_len = len(last_name)
print(last_name_len)
#  4. Name short
name_short = (player [:1]+". "+ last_name)
print (name_short)
# 5. Chant
chant = (first_name+"! ") * len(player[:5]) + (first_name+"!")
print(chant)
 #6. Goodchant
good_chant=chant[-1: ]
good_chant=boolean!=" "
print (good_chant)

