
"""
alien_0={'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
"""
alien_0={'x_pos': 0, 'y_pos': 25, 'speed': 'medium'}
print(f"original position is {alien_0['x_pos']}")
alien_0['speed']='fast'
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3

# the new pos is old pos + x_increment

alien_0['x_pos']=alien_0['x_pos']+x_increment
print(f"new position is {alien_0['x_pos']}")
