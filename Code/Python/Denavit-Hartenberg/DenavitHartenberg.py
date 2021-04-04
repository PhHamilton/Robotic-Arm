import xlrd 
import numpy as np

path = "/Users/Philip/Documents/GitHub/Robotic-Arm/Code/Python/Denavit-Hartenberg/Denavit-HartenbergMatrix.xls"
sheet = 0

class computeRotationMatrices():
    def __init__(self, path, sheet):
        self.path = path
        self.sheet = sheet
        self.decimals = None
        self.mat = None
        self.T = None
        self.nRows = None

        self.loadSheet()
        

    def loadSheet(self):
        # Load Worksheet
        wb = xlrd.open_workbook(self.path)
        excelSheet = wb.sheet_by_index(self.sheet) 

        # Pre-allocate memory for parameters
        self.mat = np.zeros((excelSheet.nrows-1, excelSheet.ncols-1))
        self.nRows = excelSheet.nrows - 1

        # Load data from excelsheet
        for i in range(excelSheet.ncols-1):
            for j in range(excelSheet.nrows-1):
                self.mat[i][j] = excelSheet.cell_value(i+1, j+1)

    def printInput(self):
        print(self.mat)            

    def DHMatrix(self, joint):
        if(joint >= self.nRows):
            print("Number of joints exceeded, number of avaliable joints: ", self.nRows - 1)
            return

        if(joint < 0 ): 
            print("Number of joints must be >= 0")
            return

        self.T = np.array([[np.cos(np.deg2rad(self.mat[joint][0])), -np.sin(np.deg2rad(self.mat[joint][0]))*np.cos(np.deg2rad(self.mat[joint][1])), np.sin(np.deg2rad(self.mat[joint][0]))*np.sin(np.deg2rad(self.mat[joint][1])), self.mat[joint][2]*np.cos(np.deg2rad(self.mat[joint][0]))],
                  [np.sin(np.deg2rad(self.mat[joint][0])), np.cos(np.deg2rad(self.mat[joint][0]))*np.cos(np.deg2rad(self.mat[joint][1])), -np.cos(np.deg2rad(self.mat[joint][0]))*np.sin(np.deg2rad(self.mat[joint][1])), self.mat[joint][2]*np.sin(np.deg2rad(self.mat[joint][0]))],
                  [0, np.sin(np.deg2rad(self.mat[joint][1])), np.cos(np.deg2rad(self.mat[joint][1])), self.mat[joint][3]],
                  [0, 0, 0, 1]])

        if(self.decimals is not None):
            return np.round(self.T, self.decimals)
        return self.T          


m = computeRotationMatrices(path, sheet)

m.printInput()
m.decimals = 2
print("")

print(m.DHMatrix(1))


