import sys, os, time, refactoring_utils

folders_to_ignore = ['OpenSceneGraph/include', 'OpenSceneGraph/include_linux', 'OpenSceneGraph/include_win', 'OpenSceneGraph/lib', '/zlib', '/RescueSource', '/libs/', '/GsTL']
#extensions_to_ignore = set(['.png'])
extensions_to_ignore = set([])

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

    ret_list = []
    ret_set = set()
    for root, dirs, files in os.walk(dirname):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            ext = os.path.splitext(file_name)[-1].lower()
            if not from_ignored_folder(file_path) and not ext in extensions_to_ignore:
                ret_list = ret_list + [(file_name, root)]
                ret_set.add(file_name)

    return ret_list, ret_set

"""
def get_hg_author(file_path):
   
    cmd_line = ['hg', 'log', '-r', 'file("%s")' % file_path]
    
    try:
        #print(cmd_line)
        output = subprocess.check_output(cmd_line, stderr=subprocess.STDOUT)
    except:
        output = b'Error'
        
    output = output.decode('utf8')
        
    users = {}
    #ret = []
    for line in output.splitlines():
        if line.find('user') == 0:
            user = line[5:].strip()
            #ret += [user]
            if not user in users:
                users[user] = 1
            else:
                users[user] = users[user] + 1
        
    return users
"""
    
def compare_dirs(dir_old, dir_new):
    files_list_1, files_set_1 = dir_to_dict(dir_old)
    files_list_2, files_set_2 = dir_to_dict(dir_new)

    exts = set()

    print("---------Duplicate files:")
    
    #for file_name in files_set_2:
        #if file_name in files_set_1:
            #print("%s" % file_name)
            #ext = os.path.splitext(file_name)[-1].lower()
            #exts.add(ext)
            
    prev_root = ""
    dirs_cnt = 0
    
    for root, dirs, files in os.walk(dir_new):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            ext = os.path.splitext(file_name)[-1].lower()
            if not from_ignored_folder(file_path) and not ext in extensions_to_ignore:
                if file_name in files_set_1:
                    if prev_root != root:
                        dirs_cnt += 1
                        print("---%s (%d)" % (root, dirs_cnt))
                    prev_root = root
                    autor = refactoring_utils.get_hg_author(file_path)
                    print("%s %s" % (file_name, autor))
                    exts.add(ext)
                
            
    print("Extensions: ", exts)

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
