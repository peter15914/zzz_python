import os, sys


def print_help():
    print("Incorrect parameters!")


def rename_screens(dir_path):

    for root, dirs, files in os.walk(dir_path):
        for file_name in files:
            if not file_name.endswith(".png"):
                continue

            assert(file_name.find('photomode_') == 0)
            assert(len(file_name) == 29)
            
            #print(file_name)
            file_name_new = file_name[:10] + file_name[14:18] + file_name[12:14] + file_name[10:12] + file_name[18:]
            #print(file_name_new)

            os.rename(os.path.join(root, file_name), os.path.join(root, file_name_new))


def main():
    if sys.argv.__len__() != 2:
        print_help()
        sys.exit()
    
    rename_screens(sys.argv[1])


if __name__ == "__main__":
	main()
