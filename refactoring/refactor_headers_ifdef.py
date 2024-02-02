import sys, os

folders_to_ignore = ['OpenSceneGraph/include', 'OpenSceneGraph/include_linux', 'OpenSceneGraph/include_win', 'OpenSceneGraph/lib']
extensions_to_ignore = set(['.png'])

def print_help():
    scriptname = os.path.basename(sys.argv[0])
    print(
        '!!!Never run this script on a main copy of the sources!!!\n'
        'This script recursively processes all headers (.h or .hpp) in a directory.\n'
        'It checks header guard and changes it if it\'s not appropriate.\n'
        'Usage: {name} <directory>\n'
        'Example:\n'
        '  {name} /home/dev/Map3D \n'.format(name = scriptname))

def from_ignored_folder(file_path):
    for folder in folders_to_ignore:
        if file_path.find(folder) != -1:
            return True
    return False

def get_define_str_for_header(file_path):
    name = os.path.basename(file_path)
    name = os.path.splitext(name)[-2]
    return name.upper() + "_H"

def process_header(file_path):
    all_lines = []
    with open(file_path) as f:
        all_lines = f.read().splitlines()

    no_ifdef = True

    needed_def_str = get_define_str_for_header(file_path)
    cur_def_str = ""

    cur_line = 0
    for line in all_lines:
        if cur_line > 3:    #checking first 4 lines
            break
        line = line.rstrip()
        if line.find("#ifndef") == 0:
            no_ifdef = False
            cur_def_str = line[7:].strip()
            break

    if no_ifdef:
        print("!!!File {fname} has no #ifndef at the beginning!".format(fname = file_path))
        return

    if needed_def_str == cur_def_str:
        return

    print(file_path)

    f_res = open(file_path, 'w')
    for line in all_lines:
        line = line.replace(cur_def_str, needed_def_str)
        f_res.write(line + "\n")
    f_res.close()

def process_dir(dirname):
    if not os.path.exists(dirname):
        print("Directory %s doesn't exist" % dirname)
        sys.exit()

    for root, dirs, files in os.walk(dirname):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            ext = os.path.splitext(file_name)[-1].lower()
            if not from_ignored_folder(file_path) and (ext == '.h' or ext == '.hpp'):
                process_header(file_path)

def main():
    if sys.argv.__len__() != 2:
        print_help()
        sys.exit()

    process_dir(sys.argv[1])

if __name__ == '__main__':
    main()
