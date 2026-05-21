def accum(st):
    res = []
    
    for i in range(len(st)):
        char = st[i]
        
        res2 = char.upper()
        
        for j in range(i):
            res2 += char.lower()
            
        res.append(res2)
    
    return "-".join(res)
            
print(accum("abcd"))