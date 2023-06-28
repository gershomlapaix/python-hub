# it will retain the order in which the items were inserted
from collections import OrderedDict
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5
d['f'] = 6

print(d)

for k, v in d.items():
    print(k, v)

my_dict = OrderedDict()
my_dict['a'] = 1
my_dict['b'] = 2
my_dict['c'] = 3
my_dict['d'] = 4
my_dict['e'] = 5
my_dict['f'] = 6

print("\n ordered dictionary")
for k,v in my_dict.items():
    print (k,v)

