wysota = int(input("Введіть число>"))
for a in range(wysota):
    for b in range(wysota - a):
        print(" ", end="")
    for c in range(a):
        print ("#", end="")
    print (" ", end="")
    for c in range(a):
        print ("#", end="")
    print()