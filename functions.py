def add(n2, n1=9):
    '''
    DOCTSTRING: infor about the function
    '''

    sum = n1+n2
    return sum


result = add(4)
print(result)

# args: for allowing


def myFunc(*args):  # receive many arguments
    print(args, type(args))
    # for item in args:
    return sum(args) * 0.05  # receives a tuple


print(myFunc(4, 63))

# kwargs: for allowing key arguments


def myFunc2(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print("The new fruit at the market is {}".format(kwargs['fruit']))
    else:
        print("Enjoy the existing fruits")


myFunc2(fruit='Mango', veggie="lettuce")
