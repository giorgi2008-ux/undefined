# 1) create 10 element size array / list
#   1. use len() function to get size of your list 
#   2. use len() function to iterate for loop

#     0  1  2   3      4        5       6       7     8  ინდექსები
#    -9 -8 -7  -6     -5       -4      -3      -2    -1  თუ გვინდა რომ სულ ბოლო დაგვიპრინტოს მაშინ -1 ს დავუწერთ, თუ ბოლოს წინა -2 ს და ასე გამოვყვებით.
array=[1,2,3,"lomi","vefxvi","spilo",[43,33],False,True]

print("----------")
# ---------------

for i in range(len(array)):
    print(array[i])
print("----------")
# ---------------

for i in range(len(array)):
    print(i)
print("----------")
# ---------------

for i in range(7):
    print(i)
print("----------")

i=0
while i < (len(array)):
    print(array[i])
    i+=1
print("----------")

slice_array=[1,2,3,4,5,6,7,8,9,0]
print(slice_array[0:5])
print(slice_array[5:])
print(slice_array[:8])
print(slice_array[::])
print(slice_array[::5])
print(slice_array[:8:2])
print(slice_array[::1]) # დაიწყე თავიდან ბოლომდე
print(slice_array[::-1]) #დაიწყე ბოლოდან თვამდე

