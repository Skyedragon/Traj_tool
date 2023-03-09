#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pydoocs

class Magnet:
    def __init__(self, name):
        self.name = name
        self.alias = pydoocs.read(self.name +'/ALIAS')['data']#returns dictionary
        
    #changes the address if the steerer is rotating. According to the RPC tool
    #returns tuple with (X, Y) currents. No further calculation needed.
    #if the steerer is not rotating, then returns only one current
    def get_current(self): 
        if self.alias == 'ROT':
            self.name=self.name.replace('MAGNETS', 'STEEROT')
            self.name=self.name.replace('.CA', '.MAGNETS')
            I_x =  pydoocs.read(self.name +'/IX.ACT')['data'] 
            I_y =  pydoocs.read(self.name +'/IY.ACT')['data'] 
            return I_x, I_y
        else:
            I = pydoocs.read(self.name +'/RDBK')['data']
            return I
    
    def get_Z(self):
        Z = pydoocs.read(self.name +'/Z_POS')['data'] #returns pos from RPC tool
        return Z
    
if __name__ == "__main__":
    M = Magnet("PITZ.CA/MAGNETS/LOW.ST1")
    #M = Magnet("PITZ.MAGNETS/STEEROT/LOW.ST1")
    
    print(M.alias)
    print(M.name[16:], "current = ", round(M.get_current()[0],3), "Amps")
    print(M.name[16:], "position = ", round(M.get_Z(),3), "m")