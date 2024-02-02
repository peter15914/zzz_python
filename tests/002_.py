import sys

def main():

    if sys.argv.__len__() != 2:
        print("need params")
        sys.exit()

    file_path = sys.argv[1]

    try:
        with open(file_path, encoding = 'utf-8') as ff:
            fromlines = ff.readlines()
    except:
        print("error with encoding in {file_name}".format(file_name = file_path))
        return

    print(', '.join(str.strip() for str in fromlines))

if __name__ == '__main__':
    main()
