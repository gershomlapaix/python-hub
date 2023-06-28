s = set()
s.add(1)
s.add(3)
print(s)
s.clear()  # clean the set

# copy
s2 = {1, 4, 5, 6}
sc = s2.copy()
s2.add(8)
print(sc)

print(sc.difference(s))

# intersection
print(s.intersection(s2))
s.intersection_update(s2)
print(s)  # updated now

# joint
s3 = {1, 2}
s4 = {1, 2, 4}
s5 = {5}

print(s3.isdisjoint(s4))
print(s3.issubset(s4))

# union
print(s3.union(s4))

# update
print(s3.update(s5))