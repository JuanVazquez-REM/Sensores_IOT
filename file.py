import pickle
from os import path
from Sensores import Sensores


class File(object):

    @staticmethod
    def saveData(data,filename="data.bin"):
        
        outfile = open(filename,'wb')
        my_pickled_object=pickle.dump(data,outfile)
        outfile.close()
        return True

    @staticmethod
    def readData(filename="data.bin"):
        new_dict=Sensores()
        if path.exists(filename):
            infile = open(filename,'rb')
            new_dict = pickle.load(infile)
            infile.close()
