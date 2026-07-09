word = "Donkey"

with open("word.txt", "r") as f:
    d = f.read()
    dnew = d.replace(word, "######")

with open("word.txt", "w") as f:
    f.write(dnew)