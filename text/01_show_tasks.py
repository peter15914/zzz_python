import sys, os

folders_to_ignore = set(['.git'])
extensions_to_check = set(['.txt'])

def print_help():
    scriptname = os.path.basename(sys.argv[0])
    print(
        'Finding lines with given prefix in the text files of the given directory recursievly\n'
        'Usage: {name} <directory> <line prefix>\n'
        'Example:\n'
        '  {name} /home/dev/ "&*" \n'.format(name = scriptname))

def from_ignored_folder(file_path):
    for folder in folders_to_ignore:
        if file_path.find(folder) != -1:
            return True
    return False

def process_file(file_path, prefix, sections):
    try:
        with open(file_path, encoding = 'utf-8') as ff:
            fromlines = ff.readlines()
    except:
        try:
            with open(file_path, encoding = 'cp1251') as ff:
                fromlines = ff.readlines()
        except:
            print("error with encoding in {file_name}".format(file_name = file_path))
            return

    cur_section = ";--"
    
    for line in fromlines:
        line = line.strip()
        if line:
            if line.find(";--") == 0:
                cur_section = line
                if not cur_section in sections:
                    sections[cur_section] = []
            elif line.find(prefix) == 0:
                sections[cur_section].append(line[2:].strip())
                

def process_dir(dirname, prefix):
    if not os.path.exists(dirname):
        print("Directory %s doesn't exist" % dirname)
        sys.exit()

    sections = {}
    for root, dirs, files in os.walk(dirname):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            ext = os.path.splitext(file_name)[-1].lower()
            if not from_ignored_folder(file_path) and ext in extensions_to_check:
                process_file(file_path, prefix, sections)

    print("")
                
    num = 0
    for section in sections:
        tasks = sections[section]
        if tasks:
            print(section)
            for task in tasks:
                print(task)
                num += 1
            print("")
            
    print("total number of tasks - {num}".format(num = num))


def main():
    if sys.argv.__len__() != 3:
        print_help()
        sys.exit()

    process_dir(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
