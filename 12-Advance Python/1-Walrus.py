#using walrus operator
if (n := len("Hello World")) > 10:
    print(f"String is too long ({n} characters).")