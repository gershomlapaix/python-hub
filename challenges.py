
def spy_game(num_list):
    '''
    DOCSTRING: a function that takes a list of integers and checks the order of 007
    '''
    code = [0, 0, 7, 'x']
    for num in num_list:
        # [0,7,'x']
        # [7,'x']
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

print(spy_game([1, 2, 4, 0, 0, 7, 5]))

# ksd = [2, 4, 2]
