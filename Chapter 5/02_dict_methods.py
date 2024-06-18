marks = {
    "Devesh" : 100,
    "Shagun" : 75,
    "Raunak" : 55,
    "Seema" : 98
}

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Dev":98, "Shagun":85})
print(marks)

print(marks.get("Dev"))
print(marks["Raunak"])