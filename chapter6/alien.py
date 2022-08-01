alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)
print(" ")

alien_0['x_position'] = 0          # adding new key value pairs
alien_0['y_position'] = 25
print(alien_0)
print(" ")

alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)
print(" ")

print(f"The alien is {alien_0['color']}")
alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']}")
print(" ")

alien_2 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print(f"original position: {alien_2['x_position']}")
# move the alien to the right
# determine how far to move the alien based on its current speed
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment
alien_2['x_position'] = alien_2['x_position'] + x_increment
print(f"New position: {alien_2['x_position']}")
print(" ")

del alien_0['points']
print(alien_0)
print(" ")

point_value = alien_0.get('points', 'No point value assigned')
print(point_value)

print(" ")

alien_3 = {'color': 'green', 'points': 5}
alien_4 = {'color': 'yellow', 'points': 10}
alien_5 = {'color': 'red', 'points': 15}

aliens = [alien_3, alien_4, alien_5]

for alien in aliens:
    print(alien)

print(" ")

# Make an emoty list for storing aliens
aliens = []

# make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed' : 'slow'}
    aliens.append(new_alien)

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens are created
print(f"Total number of aliens: {len(aliens)}")
print(" ")

# make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed' : 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens are created
print(f"Total number of aliens: {len(aliens)}")
print(" ")

# make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed' : 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens are created
print(f"Total number of aliens: {len(aliens)}")