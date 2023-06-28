greeting = 'Hello'
theList = []

# old fashion
for letter in greeting:
    theList.append(letter)

# short notation
theList = [letter for letter in greeting]

# square the current given number from the range
theList2 = [num**2 for num in range(2, 5)]
print(theList2)

result = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
print(result)