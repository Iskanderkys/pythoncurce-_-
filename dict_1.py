dd = {}
print(dd, "==>", type(dd))
# іван - ключ. За ключем присвоюється значення яке ми завдяки ключу витягаємо з словника
dd['ivan'] = "Galytss'ka str. 12"
print(dd)
dd[2] = "Nezalegnisti str. 1"
print(dd)

for key in dd:
    print(key, "===>", dd[key])
print('*'*20)
del dd[2]
print(dd)