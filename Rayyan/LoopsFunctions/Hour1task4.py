for i in range(1,6):
    for j in range(1,6):
        z = i*j
        print(i, "X", j, "=",z)


for i in range(1,6):
    for j in range(i):
        print("*", end=(" "))
    print()

