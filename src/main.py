from process_metrics import process_metrics as psm
from product_metrics import product_metrics as pdm
import file_operation as fo
import module as m
import sys

def main_func(root, ver, prev_ver):
    # files in previous version
    origin_files = fo.get_all_files_text(root + '/' + prev_ver)
    # due to find same file under previous version
    transed_files = fo.exchangea_files(origin_files, prev_ver, ver)

    # get list about files under current repository
    list = fo.fild_all_files(root + '/' + ver)

    for mod in list:
        # get product metrics
        mod = pdm.getProcuctMetrics(mod)

        # find same file from previous version
        if type (mod) ==  m.Module:
            if mod.filename in transed_files:
                # if exists, get diff
                transed_filename = mod.filename.replace(ver, prev_ver)
                prev_filename = origin_files[origin_files.index(transed_filename)]
                mod = psm.getProcessMetrics( mod, prev_filename )
                # mod = psm.getProcessMetrics(　mod, origin_files[ origin_files.index(transed_filename)　)
            else:
                # if not, isNew attribute = 1
                mod.isNew = 1
    return list

def printModules(mod):
    print(mod.filename)
    print(mod.LOC)
    print(mod.TChar)
    print(mod.CL)
    print(mod.TComm)
    print(mod.MChar)
    print(mod.DChar)
    print(mod.M1)
    print(mod.M2)
    print(mod.M3)
    print(mod.M4)
    print(mod.M5)
    print(mod.M6)
    print(mod.M7)
    print(mod.M8)

if __name__ == '__main__':
    args = sys.argv
    root = args[1]
    ver = args[2]
    prev_ver = args[3]
    # root = '../test-data/'
    # ver = 'curr'
    # prev_ver = 'prev'
    list = main_func(root, ver=ver, prev_ver=prev_ver)
    for l in list:
        printModules(l)
