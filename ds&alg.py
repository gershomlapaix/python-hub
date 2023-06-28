# A Python 3 program to
# demonstrate working of
# recursion

def printFun(test):

    if (test < 1):
        return
    else:
        print(test, end=" ")
        printFun(test-1)  # statement 2
        print(f'i is {test}')
        return


# Driver Code
test = 3
printFun(test)
print('\n')