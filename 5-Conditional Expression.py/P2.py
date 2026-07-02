Sub1 = int(input("Please Enter The marks: "))
Sub2 = int(input("Please Enter The marks: "))
Sub3 = int(input("Please Enter The marks: "))

Total = (Sub1 + Sub2 + Sub3)/3

if Total >= 40 and Sub1>=33 and Sub2 >=33 and Sub3>=33:
    print("Student is Passed in all subjects.")
else:
    print("Student is failed", Total, Sub1, Sub2, Sub3)

    