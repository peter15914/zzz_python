import sys, os
from random import randint

folders_to_ignore = ['node_modules', 'bin', 'obj', '.git']
extensions_to_include = set(['.sql', '.txt', '.cs', '.py'])


def print_help():
    scriptname = os.path.basename(sys.argv[0])
    print(
        'Combine random sources from directory\n'
        'Usage: {name} <directory> <needed files count> <result file name>\n'
        'Example:\n'
        '  {name} /home/dev/Ois.IA.Loader 10 result.txt \n'.format(name = scriptname))


def from_ignored_folder(file_path):
    for folder in folders_to_ignore:
        if file_path.find(folder) != -1:
            return True
    return False


def dir_to_dict(dirname):
    if not os.path.exists(dirname):
        print("Directory %s doesn't exist" % dirname)
        sys.exit()

    ret = []
    for root, dirs, files in os.walk(dirname):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            ext = os.path.splitext(file_name)[-1].lower()
            if not from_ignored_folder(file_path) and ext in extensions_to_include:
                ret = ret + [file_path]

    return ret


def make_sources(dir1, need_files_cnt, res_file_name):

    files1 = dir_to_dict(dir1)

    cnt = len(files1)
    print(f'Files found: {cnt}')

    if need_files_cnt > cnt:
        need_files_cnt = cnt

    res = []
    while need_files_cnt > 0 and len(files1) > 0:
        need_files_cnt -= 1

        ind = randint(0, len(files1) - 1)
        res = res + [files1[ind]]

        del files1[ind]

    f2 = open(res_file_name, 'w', encoding = 'utf-8')

    for file_name in res:
        print("File to output: %s" % file_name)

        try:
            with open(file_name, 'r', encoding = 'utf-8') as f1:
                all_lines = f1.readlines()
        except:
            continue

        for line in all_lines:
            # line = line.rstrip()
            f2.write(line)

        f2.write('\n\n')


def main():
    if sys.argv.__len__() != 4:
        print_help()
        sys.exit()

    make_sources(sys.argv[1], int(sys.argv[2]), sys.argv[3])

if __name__ == '__main__':
    main()
