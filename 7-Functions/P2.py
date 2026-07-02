def f_to_c(f):
    return 5*(f - 32)/9

f = int(input("Please enter the termperature in fahrenheit: "))
c = f_to_c(f)

print(f"{round (c, 2)} deg C")

def convert(c):
    return (9*c/5) + 32

c = int(input("Please enter the temperature in Celsius: "))
print(f"{round(convert(c), 2)} deg F")