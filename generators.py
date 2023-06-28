def create_cubes(n):

    for x in range(n):
        yield x**3


# call the function with the generator
print(list(create_cubes(3)))


# Example 2-----------------------
def gen_fibon(n):
    a = 1
    b = 1
    output = []

    for i in range(n):
        # output.append(a)
        yield a
        a, b = b, a+b


# call the function
for number in gen_fibon(10):
    print(number)

# MORE(using the next())-------------------------------
print("\n\t Using next()")
def simple_gen():
    for x in range(3):
        yield x

g = simple_gen()
print(next(g))
print(next(g))
