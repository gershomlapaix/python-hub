from random import shuffle

theList = [1, 4, 5, 6, 3, 6, 64]

# for
for num in theList:
    if(num % 2 == 0):
        print(f'{num} is even')

# traverse the strings
theString = "Hey there"
for _ in theString:
    print("for string")

# tuple unpacking
tupList = [(1, 2), (3, 4)]

for (a, b) in tupList:
    print(a)
    print(b)

# dictionaries
ex_mixed = {'k1': 425, 'k2': ["Gersh", "Nesta", 499], 'k3': {'insideKey': 100}}

print("\n\n dic keys")
for item in ex_mixed:
    print(item)

print("\n\n")
for k, v in ex_mixed.items():
    print(f"{k}-> {v}")

for vals in ex_mixed.values():
    print(vals)

# while loops

x = 0
while x < 3:
    print(f'current value : {x}')

    x = x+1

else:
    print(f'{x} is not less than 3')

# ... break, continue, pass
print("\n\n")
for item in ex_mixed:
    # comment
    pass

print("end the script, if any")

name = 'Sammy'
for letter in name:
    if letter == 'a':   # go back top to the enclosing loop
        continue
        # break
    print(letter)

# other operators
for num in range(10):
    # or for num in range(3,10)   starting from 3
    # or for num in range(0,10,2):  // always skip 2
    print(num)

print(list(range(0, 11, 2)))

# ...
word = 'abcde'

for item in enumerate(word):
    print(item)  # tuple

for index, letter in enumerate(word):
    print(f'{index} -> {letter}')

# zip,...
print(f"{'a' in 'a world'}")
print(f"{'theKey' in {'theKey':453}} or \n {453 in {'theKey':453}.values()}")

# ...

print(max(theList))


# using the imports
print("\n\n shuffled list")
shuffle(theList)
print(theList)
print(type(shuffle(theList)))  # none bcz returns nothing


# inputs
favorite = input("What is your fav number:")
# print(favorite)

print(float(favorite)) # casting

favorite2 = int(input("What is your fav number:")) # casting 2