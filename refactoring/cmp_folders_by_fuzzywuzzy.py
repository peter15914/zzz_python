import sys, os, hashlib, time, refactoring_utils
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

folders_to_ignore = ['OpenSceneGraph/include', 'OpenSceneGraph/include_linux', 'OpenSceneGraph/include_win', 'OpenSceneGraph/lib', '/zlib', '/RescueSource', '/libs/', '/GsTL', 'Map2D/pal']
#extensions_to_compare = set(['.cpp', '.h'])
extensions_to_compare = set(['.cpp'])

def print_help():
    scriptname = os.path.basename(sys.argv[0])
    print(
        'Comparison of two source directories with fuzzywuzzy (Fuzzy string matching library)\n'
        'Usage: {name} <old directory> <new directory>\n'
        'Example:\n'
        '  {name} /home/dev/Viewer3D /home/dev/Map3D \n'.format(name = scriptname))

def from_ignored_folder(file_path):
    for folder in folders_to_ignore:
        if file_path.find(folder) != -1:
            return True
    return False


def dir_to_list(dirname):
    if not os.path.exists(dirname):
        print("Directory %s doesn't exist" % dirname)
        sys.exit()

    ret = []

    for root, dirs, files in os.walk(dirname):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            ext = os.path.splitext(file_name)[-1].lower()
            if not from_ignored_folder(file_path) and ext in extensions_to_compare:
                ret = ret + [file_path]

    return ret

def compare_dirs(dir_old, dir_new):
    files_list_1 = dir_to_list(dir_old)
    files_list_2 = dir_to_list(dir_new)
    #print(files1)
    #print(files2)

    sz = len(files_list_2)
    ind = 0
    for file_path2 in files_list_2:
        with open(file_path2) as f2:
            lines2 = f2.read().splitlines()
        lines_cut_2 = lines2[:30]
        
        ind += 1
        #print("---%s (%d/%d)" % (os.path.basename(file_path2), ind, sz))
            
        ext2 = os.path.splitext(file_path2)[-1].lower()
        
        for file_path1 in files_list_1:
            ext1 = os.path.splitext(file_path1)[-1].lower()
            
            if ext1 != ext2:
                continue
            
            if os.path.basename(file_path2) == os.path.basename(file_path1):
                continue
            
            size1 = os.path.getsize(file_path1)
            size2 = os.path.getsize(file_path2)
            
            if size1 == 0 or size2 == 0:
                continue
            
            k = size1 / size2;
            if k < 0.8 or k > (1/0.8):
                continue;
            
            with open(file_path1) as f1:
                lines1 = f1.read().splitlines()
            lines_cut_1 = lines1[:30]
            
            r = fuzz.ratio(lines_cut_1, lines_cut_2)
            if r < 80:
                continue;
            
            r = fuzz.ratio(lines1, lines2)
            if r >= 80:
                author = refactoring_utils.get_hg_author(file_path2)
                print("%f %s %s %s" % (r, os.path.basename(file_path2), os.path.basename(file_path1), author))

def main():
    if sys.argv.__len__() != 3:
        print_help()
        sys.exit()

    start = time.time()

    origWD = os.getcwd()
    newDir = sys.argv[2]
    
    os.chdir(newDir)
    compare_dirs(sys.argv[1], sys.argv[2])
    os.chdir(origWD)

    end = time.time()
    print('total time:', end - start)

if __name__ == '__main__':
    main()
