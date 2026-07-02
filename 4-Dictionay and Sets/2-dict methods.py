marks = {
    "Shivang" : 25,
    "Sania" : 21,
    "Piyush" : 23
}

print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"Sania": 25})
print(marks.items())

print(marks.get("Shivang"))