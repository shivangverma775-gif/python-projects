Set = {1, 3, 5, 6, 6, 7, 7} #In set elements does not repeit.
Set.add(9)
print(Set, type(Set))

S1 = {1, 3, 5, 8}
S2 = {3, 7, 8, 9}

print(S1.union(S2))

print(S1.intersection(S2))

print(S1.issubset(S2))

print(S1.isdisjoint(S2))
