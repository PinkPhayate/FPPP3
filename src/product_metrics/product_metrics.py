import module
def getProcuctMetrics(m):
    if type (m) !=  module.Module:
        return
    filename = m.filename
    f = open(filename, 'r')

    loc = 0
    tchar = 0
    for line in f:
        loc += 1
        tchar += len(line)
    f.close()
    m.LOC = loc
    m.TChar = tchar
    return m

''' test to get loc and tchar'''
def testGetProductMetrics():
    filename = '/Users/phayate/src/ApacheDerby/10.12/tools/release/jirasoap/src/main/java/org/apache/derbyBuild/jirasoap/FilteredIssueLister.java'
    f = open(filename, 'r')

    loc = 0
    tchar = 0
    for line in f:
        loc += 1
        tchar += len(line)
    print(loc)
    print(tchar)
    f.close()
