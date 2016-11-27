import module

def getProcuctMetrics(m):
    '''
    count code line without linr "¥n" only
    param m -> module
    '''
    if type (m) !=  module.Module:
        return
    filename = m.filename
    f = open(filename, 'r')

    loc = 0     # number of total line
    cl = 0      # number of  code line
    tchar = 0   # number of total characters
    tcomm = 0   # number of comment line
    mchar = 0   # number of comment characters
    dchar = 0   # number of code characters
    isCommenting = False

    for line in f:
        if len(line)>0:
            loc += 1
            tchar += len(line)

            # check code status
            code = confirm_comment_line(line)
            if code == 20 and not isCommenting:
                cl += 1
                dchar += len(line)
            else:
                mchar += len(line)
                tcomm += 1
                if code == 1:
                    isCommenting = True
                elif code == 2:
                    isCommenting = False

    #  put class variable
    f.close()
    m.LOC = loc
    m.TChar = tchar
    m.CL = cl
    m.TComm = tcomm
    m.MChar = mchar
    m.DChar = dchar
    return m

def confirm_comment_line(line):
    '''
    return 0  -> single comment line like //
    return 1  -> beginning of comment block like /**
    return 2  -> end of comment block like */
    return 20 -> not comment line
    '''

    if '*/' in line:
        return 2
    if '/*' in line:
        return 1
    if '//' in line:
        return 0
    return 20
