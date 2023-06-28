from collections import defaultdict

my_dict = {'k1': 45}
print(my_dict['k1'])
# print(my_dict['k2'])  # keyError

# defaultdict to the rescue
# an object will be returned for inexisting key
my_dict2 = defaultdict(object)
print(my_dict2['one'])  # no error

# it will return the 0 for every key that doesn't exist
my_dict3 = defaultdict(lambda: 0)
print(my_dict3['key'])

my_dict3['two'] = 2
print(my_dict3['two'])
print(my_dict3)