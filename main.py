# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer1 ='Ruud Gullit'
scorer2 ='Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = scorer1 + ' ' + str(goal_0) + ',' + scorer2 + ' '  + str(goal_1)
print (scorers)

report = f'{scorer1} scored in the {goal_0}nd minute\n{scorer2} scored in the {goal_1}th minute'
print (report)

player = 'Hans van Breukelen'

first_name_loc = player.find('Hans')
last_name_loc = player.find('van')

first_name = player[first_name_loc:4]
last_name = player[last_name_loc:]


last_name_len =  len(last_name)
first_name_len = len(first_name)
print (first_name)
print (last_name)


initial = player[first_name_loc:1]

name_short = f'{initial}. {last_name}'

print (name_short)


chant = f'{first_name}! ' * len(first_name)

print (chant[:-1])

good_chant =chant[-0] != ' '

