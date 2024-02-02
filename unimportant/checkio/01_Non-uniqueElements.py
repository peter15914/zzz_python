from collections import Counter

def checkio_0(data):
	b = []
	for i in data:
		if data.count(i) > 1:
			b = b + [i]
	return b

checkio_1=lambda d:[x for x in d if d.count(x)>1]

def checkio_2(data):
    count = Counter(data)
    count.subtract(set(data))
    return [x for x in data if x in +count]

def checkio_3(data):
    bucket = {}
    for x in data:
        bucket[x] = bucket[x] + 1 if x in bucket else 1
    return list(filter(lambda x: bucket[x] > 1, data))

def checkio_4(data):
    counts = Counter(data)
    return  [x for x in data if counts[x] > 1]

def checkio(data):
    from collections import Counter
    nonunique = Counter(data) - Counter(set(data))
    return [x for x in data if x in nonunique]

if __name__ == "__main__":
	assert isinstance(checkio([1]), list), "The result must be a list"
	print(checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3])
	print(checkio([1, 2, 3, 4, 5]) == [])
	print(checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5])
	print(checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9])
