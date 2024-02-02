import sys
import os
from random import shuffle


def print_help():
    scriptname = os.path.basename(sys.argv[0])
    print(
        'This script shuffles order of sticks stored in files.\n'
        'It recursively processes all FFASCI files (fault sticks) in a directory and '
        'creates new file for every sticks file.\n'
        'Usage: {name} <source directory> <destination directory2>\n'
        'Example:\n'
        '  {name} /home/data/sticks /home/data/sticks_shuffled\n'.format(name=scriptname))


def process_stick_file(file_path, dest_dirname):

    all_lines = []
    with open(file_path) as f:
        all_lines = f.read().splitlines()

    if len(all_lines) < 3:
        return

    if all_lines[0].find("FFASCI") == -1:
        return

    res_file_path = os.path.join(dest_dirname, os.path.basename(file_path))

    # print("converting " + file_path + " to " + res_file_path)
    # print(file_path)

    f_res = open(res_file_path, 'w')

    f_res.write('FFASCI 0 1 "LINES" 0 1e+10\n')
    f_res.write("FFATTR 0 1\n")

    t = 0

    sticks_data = []
    src_line = ""
    for line in all_lines:
        if line.find("->") == 0:
            t = 1
            src_line = ""
            continue
        if t == 0:
            continue
        t += 1
        if t == 2:
            src_line = line
        elif t == 3:
            sticks_data.append((src_line, line))

    shuffle(sticks_data)

    ind = 0
    for buf_stick in sticks_data:
        ind += 1
        f_res.write("->{}\n".format(ind))
        f_res.write(buf_stick[0] + "\n")
        f_res.write(buf_stick[1] + "\n")

    f_res.close()


def process_dir(src_dirname, dest_dirname):
    if src_dirname == dest_dirname:
        print("Directories must be different")
        sys.exit()

    if not os.path.exists(src_dirname):
        print("Directory %s doesn't exist" % src_dirname)
        sys.exit()

    if not os.path.exists(dest_dirname):
        print("Directory %s doesn't exist" % dest_dirname)
        sys.exit()

    for root, dirs, files in os.walk(src_dirname):
        for file_name in files:
            process_stick_file(os.path.join(root, file_name), dest_dirname)


def main():
    if sys.argv.__len__() != 3:
        print_help()
        sys.exit()

    process_dir(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
