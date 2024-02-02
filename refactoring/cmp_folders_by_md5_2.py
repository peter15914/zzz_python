import sys, os, hashlib, refactoring_utils

folders_to_ignore = ['OpenSceneGraph/include', 'OpenSceneGraph/include_linux', 'OpenSceneGraph/include_win', 'OpenSceneGraph/lib', '/zlib', '/RescueSource', '/libs/', '/GsTL']
extensions_to_ignore = set([])

def print_help():
    scriptname = os.path.basename(sys.argv[0])
    print(
        'Finding files with same md5-hashes in two directories\n'
        'Usage: {name} <old directory> <new directory>\n'
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
    ret3 = {}
    for root, dirs, files in os.walk(dirname):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            ext = os.path.splitext(file_name)[-1].lower()
            if not from_ignored_folder(file_path) and not ext in extensions_to_ignore:
                hasher = hashlib.md5()
                hash_str = hashfile(open(file_path, 'rb'), hasher)
                ret = ret + [hash_str]
                ret2[hash_str] = file_name #file_path
                ret3[file_path] = hash_str

    return set(ret), ret2, ret3

def compare_dirs(dir_old, dir_new):
    hashes_set_1, map_hash_to_file_1, map_file_to_hash_1  = dir_to_dict(dir_old)
    hashes_set_2, map_hash_to_file_2, map_file_to_hash_2 = dir_to_dict(dir_new)
    #print(files1)
    #print(files2)

    exts = set()

    print("---------Duplicate files:")

    #for file_hash in files2[0]:
        #if file_hash in files1[0]:
            #print("%s, %s" % (files1[1][file_hash], files2[1][file_hash]))
            
    prev_root = ""
    for root, dirs, files in os.walk(dir_new):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            ext = os.path.splitext(file_name)[-1].lower()
            if not from_ignored_folder(file_path) and not ext in extensions_to_ignore:
                file_hash = map_file_to_hash_2[file_path]
                if file_hash in hashes_set_1:
                    if prev_root != root:
                        print("---%s" % root)
                    prev_root = root
                    autor = refactoring_utils.get_hg_author(file_path)
                    file_name_old = map_hash_to_file_1[file_hash]
                    if file_name == file_name_old:
                        print("%s %s" % (file_name, autor))
                    else:
                        print("%s, old file - %s, %s" % (file_name, file_name_old, autor))
                    exts.add(ext)
                
            
    print("Extensions: ", exts)

def main():
    if sys.argv.__len__() != 3:
        print_help()
        sys.exit()

    origWD = os.getcwd()
    newDir = sys.argv[2]

    os.chdir(newDir)
    compare_dirs(sys.argv[1], sys.argv[2])
    os.chdir(origWD)

if __name__ == '__main__':
    main()
