# Dictionaries in Python 

d = {'math' : 'algebra', 'chem' : 'experiment', 'phys': 'laws', 'stat' : 'variation'}
print(d['chem'])

# to check if a dictionary contains a specific key 
print('java' in d)

# add a new key in dictionary of Python 
d['bio'] = 'biology'
print(d['bio'])
print(d.get('bio', 'N/A')) # get an element with a default 

#delete an element from this dictionary 
del d['chem']
print(d.get('chem', 'N/A'))  # 'chem' is not longer a key, prints 'N/A'

# Looping over dictionaries for iteration

d = {'person' : 2, 'cat' : 4, 'spider' : 8}
for animal in d: 
    legs = d[animal]
    print('A %s has %d legs' % (animal, legs))
