max_i = 8
for item in range(max_i):
    print(item)
    # if item > 2:
    for i in range(8):
        for k in range(i+1):
            print("#", end="")
        print()
        if i % 2 == 0:# парне
            for item in range(4):
                print("**  ", end="")
        else:
            for item in range(4):
                print("**  ", end="")
        print()

