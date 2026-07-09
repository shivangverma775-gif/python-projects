f = open ("Poem.txt")
d = f.read()

if("twinkle" in d):
    print("Twinkle is present in the poem")
else:
    print("Twinkle is not present in the poem")

f.close()