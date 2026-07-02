S1 = "Make a lot of money"
S2 = "buy now"
S3 = "subscribe this"
S4 = "click this"

message = input("Enter your message:")

if((S1 in message)or(S2 in message)or(S3 in message)or(S4 in message)):
    print("This is Spam message")
else:
    print("This is not Spam message")