num=[1,2,3]
print(num)
num[0]=3
num[1]=4
num[2]=5
print(num)

print("-----------")

name="giorgi"
for i in range(0,len(name),2): # შეგვიძლია slicing გამოვიყენოთ for ციკლთან ერთდ. ამ შემთხვევში , ასრულებს :-ს ფუნქციას და გამოგვიტანს name-ს ყოველ მე-2 ასოს. 
    print(name[i])