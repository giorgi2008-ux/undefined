people = [
    {"name": "Giorgi"},
    {"name": "giorg"},
    {"name": "gior"},
    {"name": "gio"}
]

for i in people:
    print(i["name"])


new_set = { 1,-2,2,2,3,4,6,7,5, "gio", "gio", "auy", "oai"}
print(new_set)

new_set.add(-7)
new_set.add("giooo")
new_set.remove(7)
print(new_set)