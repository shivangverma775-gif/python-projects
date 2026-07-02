t = (1, 2, 3, 2, 2, 4)
print(t.count(2))   # Output: 3

t = (10, 20, 30, 20)
print(t.index(20))  # Output: 1

t1 = (1, 2) #Concatenation
t2 = (3, 4)
print(t1 + t2)  # (1, 2, 3, 4)

#Repetition
print((1, 2) * 3)  # (1, 2, 1, 2, 1, 2)

#Nested Tuple
t = (1, (2, 3), (4, 5))
print(t[1][0])  # 2
