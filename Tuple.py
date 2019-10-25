tt = 12, "hello!", 32
print(tt)
print(type(tt))
print(id(tt))
var = tt[0]
print(var)
x, y, z = tt
print(y, x, z)
print(x)
print(y)
print(z)
tt = (25, ) + tt[0:]
print(tt)

ll = []
print(ll, id(ll))

for i in tt:
    print(i)