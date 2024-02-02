import math
import sys
import time

#---------------------------------------------------------------------------------------------------
ONLINE_JUDGE = False
#ONLINE_JUDGE = True

if not ONLINE_JUDGE:
	sys.stdin = open('_input.txt', 'r')
	sys.stdout = open('_output.txt', 'w')

#---------------------------------------------------------------------------------------------------
primes = [2]


#---------------------------------------------------------------------------------------------------
def gen_AllPrimes(n):
	global primes;
	for i in range(3, n, 2):
		lim = int(math.sqrt(i))+1;
		for x in range(2, lim):
			if(i % x == 0):
				break;
		else:
			primes = primes + [i];


#---------------------------------------------------------------------------------------------------
'''
def genPrimes(a, b):
	lim = int(math.sqrt(b))+1
	cnt = len(primes)

	for i in range(a, b+1, 2):
		for x in range(cnt):
			if(primes[x] > lim):
				print(i);
				break;
			if(i % primes[x] == 0):
				break;
		else:
			print(i);
'''

#---------------------------------------------------------------------------------------------------
def genPrimes(a, b):
	lim = int(math.sqrt(b))+1
	cnt = len(primes)

	test_primes = []
	for pp in primes:
		if pp >= lim:
			break;
		test_primes = test_primes + [pp];

	i = a
	for dd in primes:
		
		x = 0
		while x < cnt:
			if(primes[x] > lim):
				print(i)
				break
			if(i % primes[x] == 0):
				break
			x += 1
		else:
			print(i);
		i += 2


#---------------------------------------------------------------------------------------------------
def main():
	gen_AllPrimes(int(math.sqrt(1000000000)))
	#gen_AllPrimes(int(math.sqrt(100000)))
	#print(primes)

	n = int(input())

	bb = []
	for i in range(0, n):
		a, b = map(int,input().split())
		bb = bb + [[a , b]]


	first = True

	for i in bb:
		a = i[0]
		b = i[1]

		if a <= 1:
			a = 2;

		if a == 2:
			print(2);

		if a % 2 == 0:
			a = a + 1;

		if not first:
			print("")
		first = False

		genPrimes(a, b)

	#print(primes)

#---------------------------------------------------------------------------------------------------
if not ONLINE_JUDGE:
	start_time = time.clock()

main()

if not ONLINE_JUDGE:
	end_time = time.clock()
	print('total time:')
	print(end_time - start_time)
