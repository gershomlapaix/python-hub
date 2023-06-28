
name = "Gershom"

# slice
print(name[1:])

# concatenate
print(name+" is studing python")
print('2'+'3')

# multiplication
letter = 'k'
print(letter * 4)


# methods
print("my name in uppercase: "+name.upper())

sentence = "If I was ..., I would"
print(sentence.split(',')[0])


# format strings
print("let me '{}' a string here".format('insert'))
print("The {2} {0} {1}".format('brown', 'fox', 'quick'))
print("The {q} {b} {f}".format(b='brown', f='fox', q='quick'))

# float formatting        (value:width.precision f)
theResult = 100/777
print("The result was {r:1.3f}".format(r=theResult))

# addition to string formatting
print(f'remember my name is {name}')