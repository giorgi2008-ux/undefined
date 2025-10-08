array = [1,2,3,4,5,6,6,6,7,"gio","gio",6,9]
array_count=array.count(6)
array_index=array.index("gio")
print(array_count)
print(array_index)
print("-------------------")

def greeting(): #ასე ვქმნით ფუნქციას
    return"bobi"# რაც გვიწერია return ში იმას გადააქცევს ჩვენ შექმნილ ფუნქციად

greeting()#ფუნქციის გამოძახება
print(greeting())#ფუნქციის გამოძახება ტერმინალში


def real_greeting(name):
    return "hallo" + ( name)
print(real_greeting("gio"))
