from collections import Counter

my_list = [1, 3, 5352, 52, 1, 4, 52, 56, 2, 5, 63, 63, 5, 6, 3]
countResult = Counter(my_list)
# print(Counter(my_list))

print(countResult.most_common())
# limit the result
print(countResult.most_common(3))
