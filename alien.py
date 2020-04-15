allien_0 = {'color': 'green', 'points': 5}

print(allien_0['color'])
print(allien_0['points'])

allien_0['x_position'] = 0
allien_0['y_position'] = 25
print(allien_0)

#emply dictionary
allien_0 = {}

allien_0['color'] = 'green'
allien_0['points'] = 5

print(allien_0)

#modifying values in dictionary
allien_0 = {'color': 'green'}
print(f"The alien is {allien_0['color']}.")

allien_0['color'] = 'yellow'
print(f"The alien is now {allien_0['color']}.")

#removing Key-Value Pairs
allien_0 = {'color': 'green', 'points': 5}
print(allien_0)

del allien_0['points']
print(allien_0)