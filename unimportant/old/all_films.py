
folder = '/media/xxxpt62/w/various/030/films/data/'
res_folder = '/media/xxxpt62/w/various/030/films/'


def process(year):
    
    src_file = folder + str(year)+ '.txt'
    f = open(src_file, 'r')
    res_file = res_folder + str(year) + '.txt'
    f_res = open(res_file, 'w')
    
    #num = 0
    name = ""
    cnt = 0
    gross = ""
    for line in f:
        words = line.split('\t')
        if len(words) == 0:
            continue
    
        if line[0] == ';':
            continue
    
        b = True
        try:
            tt = int(words[0])
            #num = tt
        except:
            b = False
        
    
        #line with title
        if b:
            name = words[1]
    
            #search for word with '$'
            for w in words:
                if w.find('$') != -1:
                    gross = w
                    break
    
        #print(words)
            
        lastw = words[-1].strip()
        if not lastw:
            lastw = words[-2].strip()
    
        #line with date date
        #if lastw.find('/') != -1:
        if True:
            #year = lastw.strip()[-2:]
    
            line2 = "%d\t%s\t%s\n" % (cnt+1, name, gross)
    
            #print(name)
            #print(year)
    #         nyear = int(year)
    #         if nyear < 90 and nyear > 50:
    #             year = '80x'
    #         elif nyear >= 90 and nyear <= 94:
    #             year = '90-94'
    #         elif nyear >= 95 and nyear <= 99:
    #             year = '95-99'
    #  
    #         if nyear > 30 and nyear < 90:
    #             continue
    
            f_res.write(line2)
            cnt = cnt+1
    
            name = ""
            gross = ""
        #print(words)
        #if cnt == 4:
        #    break
        else:
            print(line, '\n')
    
    print("year = ", year, "cnt = ", cnt)

    f.close()
    f_res.close()


def main():
    for i in range(2000, 2015):
        process(i)
        
main()
        