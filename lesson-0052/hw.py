def plus(num):
    total = 0
    for i in range(num + 1 ):
        total += i
    return total
print(plus(3)) 

def ps(n):
    t = 0
    for i in range(n):
        t += i
    return t
print(ps(4))


def capitals_first(text):
# 1 მჭირდება ფუნქქცია რომელითაც დავაბრუნებ დიდ და პატარა ასოებს.
    # l = text.lower()
    # u = text.upper()
    result = ""
    for i in text:
        result = (i.upper() + i.lower())
        # result += res
    return result 
print(capitals_first("giorgi"))