from process_metrics import process_metrics as psm
# import product_metrics as pdm
import module as m
def printModules(mod):
    print(mod.filename)
    print(mod.LOC)
    print(mod.TChar)
    print(mod.M1)
    print(mod.M2)
    print(mod.M3)
    print(mod.M4)
    print(mod.M5)
    print(mod.M6)
    print(mod.M7)
    print(mod.M8)


full_path = '../test-data/curr/curr_test.java'
prev_filename = '../test-data/prev/curr_test.java'
mod = m.Module(full_path)
# mod = pdm.getProcuctMetrics(mod)
mod = psm.getProcessMetrics(mod, prev_filename)
printModules(mod)
