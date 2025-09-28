# 1) create 10 element size array / list
#   1. use len() function to get size of your list 
#   2. use len() function to iterate for loop

#     0  1  2   3      4        5       6       7     8  ინდექსები
#    -9 -8 -7  -6     -5       -4      -3      -2    -1  თუ გვინდა რომ სულ ბოლო დაგვიპრინტოს მაშინ -1 ს დავუწერთ, თუ ბოლოს წინა -2 ს და ასე გამოვყვებით.
array=[1,2,3,"lomi","vefxvi","spilo",[43,33],False,True]

print("----------")
# ---------------

for i in range(len(array)): #გამოიტანს array-ს ყველა ელემენტას.
    print(array[i])
print("----------")
# ---------------

for i in range(len(array)):# გამოიტანს array-ს ელემენტების რაოდენობას.
    print(i)
print("----------")
# # ---------------

for i in range(7): # გამოიტანს ციფრებს 1-დან 7-მდე.
    print(i)
print("----------")

i=0
while i < (len(array)):# სანამ i არ გახდება array-ს ელემენტების ტოლი, მანამდე i  ყოვენ ბრუნვაზე დაემატება 1 ანუ i+=1
    print(array[i])
    i+=1
# print("----------")

slice_array=[1,2,3,4,5,6,7,8,9,0]
print(slice_array[0:5]) # გამოიტანს თვიდან დან მე-5-ე ინდექსამდე
print(slice_array[5:]) # გამოიტანს მე-5-ე ინდექსიდან ბოლომდე
print(slice_array[:8]) # გამოიტანს თვიდან მე-8-ე ინდექსამდე
print(slice_array[::]) # გამოიტანს მთლიანად
print(slice_array[::5]) # გამოიტანს ყოველ მე-5-ე ინდექსს
print(slice_array[:8:2]) # გამოიტანს თვიდან მე-8-ე ინდექსამდე, ყოველ მე-2-ე ინდექსს
print(slice_array[::1]) # დაიწყე თავიდან ბოლომდე
print(slice_array[::-1]) #დაიწყე ბოლოდან თვამდე
