# 1
def digitize(n):
    result = []
    for i in str(n):
        result.append(int(i))
    return result[::-1]
print(digitize(1245))


# 2


def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0:     # პირველი ლუწია
        if flower2 % 2 == 1: # მეორე კენტია
            return True
        else:
            return False
    else:                    # პირველი კენტია
        if flower2 % 2 == 0: # მეორე ლუწია
            return True
        else:
            return False
print(lovefunc(5,6))
        

# 3

# გვამრავლოთ ყველა ელემეტნი 2-ზე

a = [1,2,3,4,5] #ვქმნით რიცხვებუს მასივს
def func(a): #ვქმით ფუნქციას
    new_list = [] #ვქმნით ცარიელ მასივს
    for i in a: # for loop-ით უნდა გადავუაროთ რიცხვების მასივს a-ს.
        new_list.append(i * 2) # ცარიელ მასივში ვამატებთ 2-ზე გამრავლებულ a-ს ყველა ელემენტს
    return new_list #  ვაბრუნებთ უკვე შევსებულ ცარიელ მასისვ
print(func(a)) # გამოვითანოთ ტერმინალში


# 4

# შევქმნათ ფუნქცია რომელიც გქამოიტანს დიდი და პატარა ასოებით

def make_upper_case(s):
    return s.upper() # გამოიტანს დიდი ასოებით
print(make_upper_case("gio"))

def make_upper_case(d):
    return d.lower() #გამოიტანს პატარა ასოებით
print(make_upper_case("GIO"))

def make_upper_case(d):
    return d.capitalize() #გამოიტანს პატარა ასოებით
print(make_upper_case("gio"))


# 5 

def paperwork(n, m):
    if n < 0:
        return 0
    elif m < 0:
        return 0
    return n * m
print(paperwork(5,3))