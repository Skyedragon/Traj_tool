#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pydoocs as pd

class BPM:
    def __init__(self, name):
        self.name = name
        
    def read_bpm_X(self):
        x_raw = pd.read(self.name +'/X.TD') #returns dictionary
        x = x_raw['data'][0][1] # [number of trigger][beam position at this trigger]
        return x
    
    def read_bpm_Y(self):
        y_raw = pd.read(self.name+'/Y.TD')    
        y = y_raw['data'][0][1]
        return y
     
    def read_bpm_Z(self):
        z_raw = pd.read(self.name+'/Z_POS')
        z = z_raw['data']
        return z
    
if __name__ == "__main__":
    LOBPM1 = BPM("PITZ.DIAG/BPM/LOBPM1")
    print ("X,Y,Z = ",
           round(LOBPM1.read_bpm_X(),4), 
           round(LOBPM1.read_bpm_Y(),4), 
           round(LOBPM1.read_bpm_Z(),4))
    del LOBPM1 #delete the instance after its job is done. No mercy