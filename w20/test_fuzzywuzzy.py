import sys
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def process(file1, file2):
    with open(file1) as f1:
        lines1 = f1.read().splitlines()

    with open(file2) as f2:
        lines2 = f2.read().splitlines()

    r = fuzz.ratio(lines1, lines2)
    print(r)


def main():
    if sys.argv.__len__() != 3:
        print_help()
        sys.exit()

    process(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
