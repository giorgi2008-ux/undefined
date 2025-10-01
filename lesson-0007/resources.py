number=20
isEven="is number even? " + str(number % 2 == 0)
isOdd="is number odd? " + str(number % 2 == 1)

print(isEven)
print(isOdd)



# logical operators
# and,or,    not



print(False and False) #false         
print(3==3 and 3!=0) #true
print(False or False) #false
print(True or True) #true
print(True or False) #true
print(False or True) #true

print(True and True) #true
print(True and False) #false
print(False and True) #false
print(False and False) #false


#condition/მდგომარეობა 

# if else
if False:
    print("swoira")
else:
    print("arasworia")
    
#(-------------------------)

if 35>27:
    print("yochag")
else:
    print("meti ara ia kide")


 #---indentaion error/კედლიდან დაშორება---
x=5
kenti="ricxvi kentia?" + str(x % 2 ==1)
luwi="ricxvi luwia?" + str(x % 2 ==0)
print(kenti)
print(luwi)


z=12
a=17
T=(z + x == 2)
G=(z + x != 29)
print(T and G)
print(T or G)
