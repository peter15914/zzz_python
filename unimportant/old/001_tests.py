import random


val = 100.0

cnt = 10
for i in range(0, cnt):
    # if bool(random.getrandbits(1)):
    # if i % 2 == 0:
    if i < cnt/2:
        val *= 1.5
    else:
        val *= 0.6
    print(i, val)


print(val)
