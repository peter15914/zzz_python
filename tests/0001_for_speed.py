import sys
import time

int_max = sys.maxsize // 256
print('maxsize = %d' % int_max)

start_time = time.clock()

res = 0
r = range(0, int_max)
for i in r:
	res += 1

end_time = time.clock()

print('res = %d' % res)

print('total time:')
print(end_time - start_time)
