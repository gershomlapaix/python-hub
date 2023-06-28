try:
    f = open("testfile.txt", 'w')
    f.write('This is the text being put into the file.')

except TypeError:
    print("There is type error, check your code!")
except OSError:
    print("There is an os error, check your code!")
except:
    print("All other possible exceptions, check your code!")
finally:
    print("I always run")


# Another example

def ask_for_int():
    while True:
        try:
            result = int(input("Please provide an integer: "))
        except:
            print("Whoops! that is not a number!")
            continue
        # run if there is no exception
        else:
            print("Yes thank you.")  # if an integer was provided
            break
        # finally:
        #     print("May you do it again.")

# call the function
ask_for_int()