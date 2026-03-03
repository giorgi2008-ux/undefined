a = [x*10 for x in range( 5, 9)]
print (a)

def func(n):
    if n % 2 == 0:
        return n
    else:
        pass

x = list(map(func,[1,2,3,4,5,6,6,7,8,9,9,9,0,99,9,9,9,9,9,9,9,12312123,123,123,123,5,123,4,5,5,4]))
print(x)