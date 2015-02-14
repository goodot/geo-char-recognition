from PIL import Image
from numpy import array
import sqlite3
import tkMessageBox

from pybrain.tools.shortcuts import buildNetwork


global dimage, image, db,alphabet

def main():
    db = sqlite3.connect('data.db')



    




        
class Sample:
    def __init__(self,ID,Input,Target):
        self.ID = ID
        self.Input = Input
        self.Target = Target
    def __eq__(self,other):
        return isinstance(other, self.__class__) and self.Input == other.Input and self.Target == other.Target

    def __ne__(self,other):
        return not self.__eq__(other)


    def getInput(self):
        inp = self.Input.split(',')
        return [int(i) for i in inp]
    def getTarget(self):
        tar = self.Target.split(',')
        return [int(i) for i in tar]

class Params:
    def __init__(self,ID,Weights):
        self.ID = ID
        self.Weights = Weights
    def __eq__(self,other):
        return isinstance(other,self.__class__) and self.Weights == other.Weights

    def __ne__(self,other):
        return not self.__eq__(other)


    def getWeights(self):
        w = self.Weights.split(',')
        return [float(i) for i in w]
    

    
def close():
    db.close()

def average(numlist):
    return sum(numlist)/len(numlist)

def blackwhite(dim):
    imrow = []
    im = []
    for i in dim:
        for j in i:
            imrow.append(average(j))
        im.append(imrow)
        imrow = []

    dim = array(im)
    return dim

            
	
def addSample(img):
	image = img
	dimage = array(img)
	dimage = blackwhite(dimage)


def getUpRow(dimage):
    x = dimage.shape[0]
    y = dimage.shape[1]

    for i in range(x):
        for j in range(y):
            if average(dimage[i][j]) < 255:
                return i


            
def getLeftCol(dimage):
    x = dimage.shape[0]
    y = dimage.shape[1]


    for j in range(y):
        for i in range(x):
            if average(dimage[i][j]) < 255:
                return j



def getDownRow(dimage):
    x  = dimage.shape[0]
    y = dimage.shape[1]

    for i in range(x-1,-1,-1):
        for j in range(y-1,-1,-1):
            if average(dimage[i][j]) < 255:
                return i

def getRightCol(dimage):
    x = dimage.shape[0]
    y = dimage.shape[1]

    for j in range(y-1,-1,-1):
        for i in range(x-1,-1,-1):
            if average(dimage[i][j]) < 255:
                return j
            

def getBox(dimage):
    rowUp = getUpRow(dimage)
    colLeft = getLeftCol(dimage)
    rowDown = getDownRow(dimage)
    colRight = getRightCol(dimage)

    
    

    
    return (colLeft,rowUp,colRight,rowDown)
    
    


	
	

	
	





if __name__ == "__main__":
	main()
	
