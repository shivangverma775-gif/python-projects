try:
    a = int(input("Enter a number: "))
    print("You entered:", a)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
    
print("Program continues...")   