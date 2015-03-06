# -*- coding: utf-8 -*-
from PIL import Image
from numpy import array
import sqlite3
import tkMessageBox

from pybrain.tools.shortcuts import buildNetwork


#global db, x, dimage, image,alphabet

alphabet = {0:'ა',1:'ბ',2:'გ',3:'დ',4:'ე',5:'ვ',6:'ზ',7:'თ',8:'ი',9:'კ',
            10:'ლ',11:'მ',12:'ნ',13:'ო',14:'პ',15:'ჟ',16:'რ',17:'ს',18:'ტ',
            19:'უ',20:'ფ',21:'ქ',22:'ღ',23:'ყ',24:'შ',25:'ჩ',26:'ც',27:'ძ',
            28:'წ',29:'ჭ',30:'ხ',31:'ჯ',32:'ჰ'}





    




        
class Sample:
    def __init__(self,Input,Target,Id=None):
        self.Id = Id
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
    def __init__(self,Weights,ID = None):
        self.ID = ID
        self.Weights = Weights
    
    def __eq__(self,other):
        return isinstance(other,self.__class__) and self.Weights == other.Weights

    def __ne__(self,other):
        return not self.__eq__(other)


    def getWeights(self):
        w = self.Weights.split(',')
        return [float(i) for i in w]

def getcharkey(char):
    for key,ch in alphabet.iteritems():
        if ch.decode('utf-8') == char:
            return key


        
def init():

    
    global samples,db

    #caching samples
    
    samples = []
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    rows = cursor.execute('select *from samples')
    rows = rows.fetchall()


    for r in rows:
        sample = Sample(r[1],r[2])
        samples.append(sample)

    
    


    

        
    
def close():
    db.close()

def average(numlist):
    return sum(numlist)/len(numlist)

def blackwhite(dim):
    dim = dim.tolist()
    imrow = []
    im = []
    for i in dim:
        for j in i:
            imrow.append(average(j))
        im.append(imrow)
        imrow = []

    dim = array(im)
    return dim

def makestring(dim):
    string = [str(i) for i in dim]
    string = ','.join(string)
        
    return string

def makelist(dim):
    lst = []
    for i in dim:
        for j in i:
            lst.append(j)

    return lst


def addSample(sample):
    
    
    cursor = db.cursor()
    cursor.execute("insert into samples (Input,Target) values (?,?)",[sample.Input,sample.Target])
    db.commit()
    
    


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
    
    


    
    

    
init()   







    
