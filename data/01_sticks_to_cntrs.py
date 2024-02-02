import sys, os

def print_help():
    scriptname = os.path.basename(sys.argv[0])
    print(
        'This script converts fault sticks files to contour files.\n'
        'It recursively processes all FFASCI files (fault sticks) in a directory and '
        'creates new contour file for every sticks file.\n'
        'The resulting contour file contains all top points of the sticks.\n'
        'Usage: {name} <directory>\n'
        'Example:\n'
        '  {name} /home/data/sticks \n'.format(name = scriptname))

def process_stick_file(file_path):
    all_lines = []
    with open(file_path) as f:
        all_lines = f.read().splitlines()
        
    if len(all_lines) < 3:
        return
    
    if all_lines[0].find("FFASCI") == -1:
        return
    
    res_file_path = file_path + ".cntr"

    #print("converting " + file_path + " to " + res_file_path)
    print(file_path)

    f_res = open(res_file_path, 'w')
    
    f_res.write('FFASCI 0 1 "LINES" 0 1e+10\n')
    f_res.write("FFATTR 0 1\n")
    f_res.write("->1\n")
    
    t = 0
    
    for line in all_lines:
        if line.find("->") == 0:
            t = 1
            continue
        if t == 0:
            continue
        t += 1
        if t == 2:
            f_res.write(line + "\n")
        
    f_res.close()

def process_dir(dirname):
    if not os.path.exists(dirname):
        print("Directory %s doesn't exist" % dirname)
        sys.exit()

    for root, dirs, files in os.walk(dirname):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            process_stick_file(file_path)

def main():
    if sys.argv.__len__() != 2:
        print_help()
        sys.exit()

    process_dir(sys.argv[1])

if __name__ == '__main__':
    main()
