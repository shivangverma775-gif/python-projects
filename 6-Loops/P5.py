n = int(input("Enter a number: "))

i = 2

while(i < n):
    if(n%i) == 0:
        print("The Number Is Not A Prime.")
        break
    i += 1
else:
    print("The Number Is A Prime.")