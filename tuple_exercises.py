counts = {"a":1,"b":12,"c":22}

lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)

print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )
print( [ (k,v) for k,v in counts.items().sorted() ] )
print( sorted( [ (v,k) for k,v in counts.keys() ] ) )
print( [ (k,v) for k,v in counts.values().sort() ] )