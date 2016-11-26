class Module(object):
    def __init__(self, filename):
        self.filename = filename

        ''' Product Metrics'''
        self.LOC = int()
        self.TChar = int()
        self.CL = int()
        self.TComm = int()
        self.MChar = int()
        self.DChar = int()

        ''' Process Metrics'''
        self.M1 = float()
        self.M2 = float()
        self.M3 = float()
        self.M4 = float()
        self.M5 = float()
        self.M6 = float()
        self.M7 = float()
        self.M8 = float()

    def printfilename():
        print(self.filenme)

    def print_metrics():
        print(self.LOC)
        print(self.TChar)
        print(self.CL)
        print(self.TComm)
        print(self.MChar)
        print(self.DChar)
        print(self.M1)
        print(self.M2)
        print(self.M3)
        print(self.M4)
        print(self.M5)
        print(self.M6)
        print(self.M7)
        print(self.M8)
