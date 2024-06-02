bus = []


for i in range(10):
    bus.append([])

for i in range(len(bus)):
    for j in range(4):
        bus[i].append((j+1)+(4*i))

print(bus)