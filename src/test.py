from process_metrics import process_metrics as psm
from product_metrics import product_metrics as pdm
import file_operation as fo
import module as m
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

def test_process_metrics():
    full_path = '../test-data/curr/curr_test.java'
    prev_filename = '../test-data/prev/curr_test.java'
    mod = m.Module(full_path)
    mod = psm.getProcessMetrics(mod, prev_filename)
    printModules(mod)

def test_product_metrics():
    full_path = '../test-data/curr/comment_test.java'
    prev_filename = '../test-data/prev/comment_test.java'
    mod = m.Module(full_path)
    mod = pdm.getProcuctMetrics(mod)
    # mod = psm.getProcessMetrics(mod, prev_filename)
    printModules(mod)

def test_trans_filename():
    root = '../test-data/'
    ver = 'curr'
    prev_ver = 'prev'
    # files in previous version
    origin_files = fo.get_all_files_text(root + prev_ver)
    # due to find same file under previous version
    transed_files = fo.exchangea_files(origin_files, prev_ver, ver)

    # get list about files under current repository
    list = fo.fild_all_files(root + ver)
    for mod in list:
        # find same file from previous version
        if type (mod) ==  m.Module:
            if mod.filename in transed_files:
                # if exists, get diff
                transed_filename = mod.filename.replace(ver, prev_ver)
                print(origin_files[ origin_files.index(transed_filename) ])
                print(mod.filename)

test_product_metrics()
