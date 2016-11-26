import os, re
import module as m

def fild_all_files(directory):
    list = []
    for root, dirs, files in os.walk(directory):
        for file_ in files:
            full_path = os.path.join(root, file_)
            # isJava = re.search(full_path, r'(\.java)$')
            isJava = re.search("\.JAVA$",full_path.upper())
            if isJava is not None :
                list.append(m.Module(full_path))
    return list

def get_all_files_text(directory):
    list = []
    for root, dirs, files in os.walk(directory):
        for file_ in files:
            full_path = os.path.join(root, file_)
            # isJava = re.search(full_path, r'(\.java)$')
            isJava = re.search("\.JAVA$",full_path.upper())
            if isJava is not None :
                list.append(full_path)
    return list

def exchangea_files(files, frm, to):
    changed_files = []
    for file in files:
        changed_files.append( file.replace(frm, to) )
    return changed_files
# root = '/Users/phayate/src/ApacheDerby/'
# ver = '10.12'
# # get list about files under the repository
# list = fild_all_files(root + ver)
#
# ''' test to exist module class '''
# for module in list:
#     print module.filename
def readFile(filename):
    f = open(filename, 'r')
    list = []
    for line in f:
        list.append(line)
    f.close()
    return list
