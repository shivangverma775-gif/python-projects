def sum(n):
    if n == 1:
        return 1
    return sum(n-1) + n

print(sum(5))

print("\n")

def natural(n):
    return n * (n + 1)/2
a = int(input("Please enter a number: "))
print(f"The sum of first {a} natural numbers is: {natural(a)}")