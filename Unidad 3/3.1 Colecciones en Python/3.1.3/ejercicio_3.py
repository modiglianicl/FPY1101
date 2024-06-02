bus = [[(j+1+4*i) for j in range(4)] for i in range(10)]


for i in range(len(bus)):
    for j in range(len(bus[i])):
        if j == 1:
            if bus[i][j] < 10:
                print(f" ",end="")
            print(f"{bus[i][j]}",end="     | |     ")
        elif j == 3:
            if bus[i][j] < 10:
                print(f" ",end="")
            print(f"{bus[i][j]}")
        else:
            if bus[i][j] < 10:
                print(f" ",end="")
            print(f"{bus[i][j]}",end="  ")

print(bus)