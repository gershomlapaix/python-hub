import re

patterns = ['term1', 'term2']
text = 'This is a string with term1, but not the other form.'

print(re.search('hello', 'hello world!'))

for pattern in patterns:
    print('Searching for "%s" in: \n"%s"' % (pattern, text))

    # check for a match
    if re.search(pattern, text):
        print("\nMatch was found")

    else:
        print("\nNo match was found")

# More operations
match = re.search(patterns[0], text)
print(f'\nType of match is {type(match)}')

print(f'\n{match.start()}')
print(f'{match.end()}')

# splitting
print(re.findall('match', 'Here is one match, here is another match'))
