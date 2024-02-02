import sys, os, hashlib

folders_to_ignore = ['OpenSceneGraph/include', 'OpenSceneGraph/include_linux', 'OpenSceneGraph/include_win', 'OpenSceneGraph/lib']
extensions_to_ignore = set([])

def print_help():
    scriptname = os.path.basename(sys.argv[0])
    print(
        'Finding files with same md5-hashes in two directories\n'
        'Usage: {name} <directory 1> <directory 2>\n'
        'Example:\n'
        '  {name} /home/dev/Viewer3D/Icons /home/dev/CommonRes/Icons \n'.format(name = scriptname))

def from_ignored_folder(file_path):
    for folder in folders_to_ignore:
        if file_path.find(folder) != -1:
            return True
    return False

def hashfile(afile, hasher, blocksize=65536):
	buf = afile.read(blocksize)
	while len(buf) > 0:
		hasher.update(buf)
		buf = afile.read(blocksize)
	return hasher.hexdigest()

def dir_to_dict(dirname):
    if not os.path.exists(dirname):
        print("Directory %s doesn't exist" % dirname)
        sys.exit()

    ret = []
    ret2 = {}
    for root, dirs, files in os.walk(dirname):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            ext = os.path.splitext(file_name)[-1].lower()
            if not from_ignored_folder(file_path) and not ext in extensions_to_ignore:
                hasher = hashlib.md5()
                hash_str = hashfile(open(file_path, 'rb'), hasher)
                ret = ret + [hash_str]
                ret2[hash_str] = file_path

    return set(ret), ret2

def compare_dirs(dir1, dir2):
    files1 = dir_to_dict(dir1)
    files2 = dir_to_dict(dir2)
    #print(files1)
    #print(files2)

    for file_hash in files2[0]:
        if file_hash in files1[0]:
            print("Duplicate files: %s, %s" % (files1[1][file_hash], files2[1][file_hash]))

def main():
    if sys.argv.__len__() != 3:
        print_help()
        sys.exit()

    compare_dirs(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
