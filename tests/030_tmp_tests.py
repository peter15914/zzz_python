
"""
x = int(input())
y = int(input())
z = int(input())

if x < y:
	if y > z:
		if x < z:
			y, z = z, y
		else:
			x, y, z = z, x, y
else:
	if y > z:
		x, y, z = z, y, x
	else:
		if x < z:
			x, y, z = y, x, z
		else:
			x, y, z = y, z, x
			

print("%d %d %d" % (x, y, z))
"""

kk = 1000003

x1 = kk + 11
x2 = kk + 7

print((x1 + x2) % kk)
