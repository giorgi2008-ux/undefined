
# 1) მოცემული ინფორმაციის მიხედვით გამოიყენეთ for loop და თითო ელემენტს მიწვედით ინდექსით ხოლო პრინტით კი გამოიტანეთ ტერმინალში <3

a = "lom ki ara lekvi kide!"
print(len(a))
for i in range (len(a)):
    print(a[i])

# ------------------------


#2) მოცემული კოდში შევქმანთ ახალი new_a ში შევინახოთ იგივე წინანადადება რაც გვქონდა a ში ოღონდ " " / სფეისების გარეშე
a = "lom ki ara lekvi kide!"
print(len(a))
new_a = ""
for i in range( len(a) ) :
    new_a += a[i]
print(new_a[:3]+new_a[4:6]+new_a[7:10]+new_a[11:16]+new_a[17:22])
#---------------------------
print(len(a))
new_a = ""
for i in range( len(a) ) : #თუ ა ს ინდექსი არ უდრის სფეისს მაშინ დაპრინტე
    if a[i] != " ": 
        new_a += a[i]
print(new_a)
