import sys, os

folders_to_ignore = ['OpenSceneGraph/include', 'OpenSceneGraph/include_linux', 'OpenSceneGraph/include_win', 'OpenSceneGraph/lib']
extensions_to_ignore = set(['.png'])

def print_help():
    scriptname = os.path.basename(sys.argv[0])
    print(
        'Finding files with same names in two directories to ensure that all files were renamed during refactoring\n'
        'Usage: {name} <old directory> <new directory>\n'
        'Example:\n'
        '  {name} /home/dev/Viewer3D /home/dev/Map3D \n'.format(name = scriptname))

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
            if not from_ignored_folder(file_path) and not ext in extensions_to_ignore:
                ret = ret + [file_name]

    return set(ret)

def compare_dirs(dir1, dir2):
    files1 = dir_to_dict(dir1)
    files2 = dir_to_dict(dir2)

    for file_name in files2:
        if file_name in files1:
            print("Duplicate file: %s" % file_name)

def main():
    if sys.argv.__len__() != 3:
        print_help()
        sys.exit()

    compare_dirs(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
