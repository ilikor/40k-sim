'''
Created on Nov 30, 2017

@author: Samuel
'''

class Defense(object):
    '''
    classdocs
    '''


    def __init__(self, Ti, Wi, SVi, ISVi, FnPi, morale_init = 7, Points_Init = 13):
        
        
        self.T = Ti
        self.W = Wi
        self.SV = SVi
        self.ISV = ISVi
        self.FnP = []
        self.Points = Points_Init
        self.moral = morale_init
        
        self.moral_rule = "None"