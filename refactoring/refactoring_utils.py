import subprocess


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
