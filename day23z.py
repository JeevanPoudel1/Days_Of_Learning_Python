students = ["a", "b"]

for i in range(len(students)):
    print(i +1, students[i])


stds = [
    {"name": "harry", "house": "gryffindor", "patronus": "stag"},
    {"name": "hermione", "house": "gryffindor", "patronus": "otter"},
    {"name": "ron", "house": "gryffindor", "patronus": "jack russell terrier"},
    {"name": "luna", "house": "ravenclaw", "patronus": "hare"},
    {"name": "cho", "house": "ravenclaw", "patronus": "swan"},
    {"name": "draco", "house": "slytherin", "patronus": "none"},
    {"name": "cedric", "house": "hufflepuff", "patronus": "none"},
    {"name": "ginny", "house": "gryffindor", "patronus": "horse"}
]

for s in stds:
    print(s["name"], s["house"], s["patronus"], sep=", ")




