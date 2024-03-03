'''
alien_0 = {
    'color': 'green', 
    'points': 5
    }
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0['x_pos'] = 0
alien_0['y_pos'] = 25

print(alien_0)

# change 
alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 7

print (alien_1)

print(f"The alien is {alien_1['color']}.")

alien_1['color'] = 'yellow'
print(f"The alien is {alien_1['color']}.")

#  increment
alien_2 = {'x_pos': 0, 'y_pos': 25, 'speed': 'medium'}

print(f"Original position: {alien_2['x_pos']}.")

if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_2['x_pos'] = alien_2['x_pos'] + x_increment
print(f"New position: {alien_2['x_pos']}.")

# del
alien_3 = {'x_pos': 0, 'y_pos': 25, 'speed': 'slow'}
print(alien_3)
del alien_3['speed']
print(alien_3) 

# get
favorite_languages = {
    'Jen': 'python',
    'Sarah': 'C',
    'Edward': 'ruby',
    'phil': 'python',
}

print(favorite_languages.get('Jen', 'No such user.'))

favorite_number = {
    'Peter': '7',
    'Bob': '3',
    'John': '5',
    'Lisa': '9',
}

for k, n in favorite_number.items():
    print(f"{k}'s favorite number is: {n}")
'''
# glossary
glossary = {
    'string': 'sequence of characters wrapped in quotes',
    'boolean': 'truth values - either True or False',
    'list': 'mutable, ordered sequence of elements',
    'tuple': 'immutable, ordered sequence of values',
    'dictionary': 'collection of a key-value pairs',
}

for key in glossary:
    print(f"{key.capitalize()}: {glossary[key]}.\n")

for name in sorted(glossary.keys()):
    print(name.title())
