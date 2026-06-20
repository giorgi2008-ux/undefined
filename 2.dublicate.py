# def duplicate_count(text):
#     text = text.lower()
#     res = 0
#     for i in text:
#         # x = text.count(i)
#         if text.count(i) > 1: 
#             res += 1
#         else:
#             pass
#     return  res 
    
# print(duplicate_count("giorgi"))

# ვარიანტი 1

# def duplicate_count(text):
#     text = text.lower()
#     res = 0
#     arr = []
#     arr2 =[]
#     for i in text:
#         # x = text.count(i)
#         if text.count(i) > 1: 
#             arr.append(str(i))
#         else:
#             pass
#     for char in arr:
#         if char not in arr2:
#             arr2.append(char)
#         else:
#             pass
#     for i in arr2:
#         if i:
#             res += 1       
#         else:
#             pass
        
#     return res
    
# print(duplicate_count("giorgi")) 

# ვარიანტი 2

# def duplicate_count(text):
#     text = text.lower()
#     count = 0

#     for char in set(text):
#         if text.count(char) > 1:
#             count += 1

#     return count

# print(duplicate_count("giorgi")) 


print("-------------------------------")


def count(text):
    text = text.lower()
    res = 0
    for i in set(text):
        if text.count(i) > 1:
            res += 1
    return res

        
print(count("ggioo"))
