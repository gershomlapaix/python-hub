# Lists
theList = ['one', 300, "Kalim"]

print(theList[1:])
print(f"The list has {len(theList)} elements.")

theList3 = ["inner", "study", 42.52]

# combine two lists
new_list = theList+theList3
print(new_list)

new_list[0] = 'changing'
print(new_list)

new_list.append(3994)
print(new_list)

print(f'{new_list.pop()} removed')

deletedItem = new_list.pop(2)

#sorting
characters = ['a','e','x','b']
characters.sort()
print(f'Sorted list {characters}')

#reversal
characters.reverse()
print(f'reversed list {characters}')