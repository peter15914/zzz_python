
def weak_point_0(matr):
	N =  len(matr)

	r = 0
	c = 0
	_minr = 1000
	_minc = 1000

	for i in range(0, N):
		row = matr[i]
		val = sum(row)
		if val < _minr:
			_minr = val
			r = i

	for j in range(0, N):
		s = 0;
		for i in range(0, N):
			s = s + matr[i][j]
		if s < _minc:
			_minc = s
			c = j

	return [r, c]

def weak_point_1(matrix):
    def ms(rows):
        sums = tuple(map(sum, rows))
        return sums.index(min(sums))
    return ms(matrix), ms(zip(*matrix))

def weak_point_2(matrix):
	n = len(matrix)
	row = min(range(n), key=lambda r:sum(matrix[r][c] for c in range(n)))
	col = min(range(n), key=lambda c:sum(matrix[r][c] for r in range(n)))
	return row, col

def argmin(lines):
    sums = [sum(line) for line in lines]
    return sums.index(min(sums))
 
def weak_point(matrix):
    return argmin(matrix), argmin(zip(*matrix))

if __name__ == "__main__":
	print(weak_point([[7, 2, 7, 2, 8],
					[2, 9, 4, 1, 7],
					[3, 8, 6, 2, 4],
					[2, 5, 2, 9, 1],
					[6, 6, 5, 4, 5]]) == (3, 3))
	print(weak_point([[7, 2, 4, 2, 8],
            [2, 8, 1, 1, 7],
            [3, 8, 6, 2, 4],
            [2, 5, 2, 9, 1],
            [6, 6, 5, 4, 5]]) == (1, 2))
