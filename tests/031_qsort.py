import random

def qsort(a, i1, i2):
    if i1 >= i2:
        return

    ind = (i1 + i2) // 2

    l = i1
    r = i2
    while l < r:
        while l < ind and a[l] <= a[ind]:
            l += 1
        while r > ind and a[r] >= a[ind]:
            r -= 1
        a[l], a[r] = a[r], a[l]
        if ind == l:
            ind = r
        elif ind == r:
            ind = l

    qsort(a, i1, ind-1)
    qsort(a, ind+1, i2)


def test_01():
    random.seed(8)
    arr = [random.randint(0, 9) for i in range(10)]

    print(arr)
    qsort(arr, 0, len(arr) - 1)
    print(arr)


def test_02():
    good_cnt = 0

    for _ in range(100):
        arr = [random.randint(0, 10) for i in range(100)]
        qsort(arr, 0, len(arr) - 1)

        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                print("!!!Error")
                break
        else:
            good_cnt += 1
            continue
        break

    print(f'{good_cnt = }')


if __name__ == "__main__":
    test_02()
