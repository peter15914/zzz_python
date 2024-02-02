import sys, os

def print_help():
    scriptname = os.path.basename(sys.argv[0])
    print(
        'Calculating some statistics from _DB.txt\n'
        'Usage: {name} <path to _DB.txt> <line prefix>\n'
        #'Example:\n'
        #'  {name} /home/dev/ "&*" \n'
        .format(name = scriptname))

def process_file(file_path):
    try:
        with open(file_path, encoding = 'cp1251') as ff:
            fromlines = ff.readlines()
    except:
        print("error with encoding in {file_name}".format(file_name = file_path))
        return
    
    
    words_ao = set()
    words_end_un = set()
    
    cur_freq = 0

    for line in fromlines:
        line = line.strip()
        if not line:
            continue
        if line[0] == '#':
            cur_freq = int(line[1:])
            continue
        
        if cur_freq < 400:
            continue
        
        if line.find('-') != -1:
            continue
        if line.find('а') == -1 and line.find('о') == -1:
            continue
        words_ao.add(line);
        if line[-2:] == "ун" and line.find('а') != -1:
            words_end_un.add(line);
            
    #for word_ao in words_ao:
        #print(word_ao)
            
    for word_un in words_end_un:
        word_un_cut = word_un[:-2]
        #print(word_un_cut, word_un)
        
        if word_un_cut.find('а') != -1:
            word_un_cut2 = word_un_cut.replace('а', 'о');
            #print(word_un, word_un_cut, word_un_cut2)
            if word_un_cut == word_un_cut2:
                continue
            
            if word_un_cut2 in words_ao:
                print(word_un_cut2, word_un)
                
def main():
    if sys.argv.__len__() != 2:
        print_help()
        sys.exit()

    process_file(sys.argv[1])

if __name__ == '__main__':
    main()
