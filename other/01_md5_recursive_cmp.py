# import hashlib
import os
# import shutil
import sys
import zzzutils


def print_help():
    script_name = os.path.basename(sys.argv[0])
    print(
        'Checking integrity of data in directories (recursively) by md5-hashes\n'
        '\nUsage:\n'
        '{name} -create <directory> [filter file]\n'
        '       create md5-hashes of all files in directory (recursively)\n'
        '       if filter file is given, only files from filter file are used to create hashes\n'
        '{name} -compare <md5-file for temporary directory> <md5-file for main backup directory>\n'
        '       compare 2 files with md5-hashes. '
        'all files in temporary directory must exist in main backup directory\n'
        .format(name=script_name))


def get_files_base_names(file_with_hashes):
    ret = []
    if file_with_hashes:
        with open(file_with_hashes, "r") as f:
            for buf_list in [line.rstrip().split('\t') for line in f]:
                if len(buf_list) > 0:
                    file_name = buf_list[1]
                    ret = ret + [os.path.basename(file_name)]

    return ret


def print_hash_recursive(path, filter_set):
    for root, dirs, files in os.walk(path):
        for file_name in files:
            if not filter_set or file_name in filter_set:
                file_path = os.path.join(root, file_name)
                md5 = zzzutils.calc_hash_md5(file_path)
                print('\t'.join([md5, file_path]))


def create_md5_hashes(path, filter_file=''):
    filter_set = set(get_files_base_names(filter_file))
    print_hash_recursive(path, filter_set)


def get_md5_set(file_name, allow_dupes=True):
    ret_lines = set()
    with open(file_name, "r") as f1:
        for buf_list in [line.strip().split(None, 1) for line in f1]:
            if len(buf_list) >= 2:
                res_line = buf_list[0] + "###" + os.path.split(buf_list[-1])[-1]
                if not allow_dupes and res_line in ret_lines:
                    print("!!!Duplicate in", file_name, res_line)
                    sys.exit()
                ret_lines.add(res_line)
            else:
                print("Problem in get_md5_set()" + str(buf_list))

    return ret_lines


def compare_md5_hashes(hashes_file_1, hashes_file_2):
    if not os.path.exists(hashes_file_1) or not os.path.exists(hashes_file_2):
        print("File doesn't exist")
        return

    lines_set_1 = get_md5_set(hashes_file_1)
    lines_set_2 = get_md5_set(hashes_file_2)

    if lines_set_1 == lines_set_2:
        print("All OK, sets are equal, size is %d" % len(lines_set_2))
        return

    cnt = 0
    new_in_set1 = 0
    new_in_set2 = 0

    for line in lines_set_1:
        cnt += 1
        if not (line in lines_set_2):
            new_in_set1 += 1
            print("{}. !new in set 1: {}".format(new_in_set1, line))

    for line in lines_set_2:
        cnt += 1
        if not (line in lines_set_1):
            new_in_set2 += 1
            print("{}. !new in set 2: {}".format(new_in_set2, line))

    if new_in_set1 + new_in_set2 == 0:
        print("All OK, compared {}".format(cnt // 2))
    else:
        print("{} files equal, {} new files in set 1, {} new files in set 2".format((cnt - new_in_set1 - new_in_set2) // 2, new_in_set1, new_in_set2))


def main():
    if len(sys.argv) < 3:
        print_help()
        sys.exit()

    all_ok = True
    cmd = sys.argv[1]

    if cmd == "-create":
        if len(sys.argv) == 3:
            create_md5_hashes(sys.argv[2])
        elif len(sys.argv) == 4:
            create_md5_hashes(sys.argv[2], sys.argv[3])
        else:
            all_ok = False
    elif cmd == "-compare":
        if len(sys.argv) == 4:
            compare_md5_hashes(sys.argv[2], sys.argv[3])
        else:
            all_ok = False
    else:
        all_ok = False

    if not all_ok:
        print_help()
        sys.exit()


if __name__ == '__main__':
    main()
