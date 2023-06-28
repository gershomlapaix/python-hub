# strings slicing
print('\nStrings slicing')

x = 'computer'
print(x[1:4])  # index 4 is exclusive
print(x[1:6:2])  # with step 2
print(x[3:])  # till the last
print(x[:5])  # stop at the last index but exclusively
print(x[-1])  # the last item in the string
print(x[-3:])  # from -3 to the end of the string
print(x[:-2])  # except the last two elements

# concatenating sequences of the same type
x = 'horse' + 'shoe'  # strings
print(x)

# list
y = ['pig', 'cow'] + ['horse']
print(y)

# tuple
z = ('kevin', 'Niklas')+('craig',)  # note the comma on the 2nd tuple
print(z)


# checking membership
print('\nCheck membership')
# strings
print('h' in x)

# list
print('cow' not in y)

# looping through ds
x = [7, 8, 3]

for item in x:
    print(item)

# index and item
for index, item in enumerate(x):
    print(index, item)

# sum
print(sum(x[-2:]))  # 11
print(min(x))
print(sorted(x))

# sorting
x = 'computer'
print(sorted(x))  # returns the list

z = ('kevin', 'Niklas', 'craig')
# sort by the third letter
print(sorted(z, key=lambda k: k[3]))
