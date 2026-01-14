a = ["1","2","#","4"]
new_a = []
for i in a:
    if i == "1":
        break
    else:
        new_a += str(i)
print(new_a)