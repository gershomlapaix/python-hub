# logic
def square_num(num):
    return num**2


theList = [1, 2, 3, 4, 5]
squaredNums = map(square_num, theList)  # apply that function to the given list

print(f'\n {squaredNums}')
print(f'\n {list(squaredNums)}')

# using lambda functions
even_nums = filter(lambda num: num % 2 == 0, theList)
print(f'\n even numbers: {list(even_nums)}')
