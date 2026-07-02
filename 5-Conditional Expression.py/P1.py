a = int(input("Please enter First number: "))
b = int(input("Please enter Second number: "))
c = int(input("Please enter Third number: "))
d = int(input("Please enter Fourth number: "))

if a>b and a>c and a>d :
    print("first is the greatest number.", a)
elif b>a and b>c and b>d :
    print("second is the greatest number.", b)
elif c>a and c>b and c>d :
    print("third is the greatest number.", c)
else:
    print("fourth is the greatest number.", d)