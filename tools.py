#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pandas import DataFrame
import matplotlib.pyplot as plt
import matplotlib
from BPM import BPM
from Magnet import Magnet

matplotlib.rcParams['figure.figsize'] = [16, 4]

def read_trajectory(filename):
    x=[]
    y=[]
    pos=[]
    
    with open(filename, 'r') as bpms:
        for line in bpms:
            MyBPM = BPM(line.replace('\n', ''))
            x.append(MyBPM.read_bpm_X())
            y.append(MyBPM.read_bpm_Y())
            pos.append(MyBPM.read_bpm_Z()) 
            del MyBPM
    return x, y, pos

def read_currents(filename):
    I_x = []
    I_y = []
    I_q = []
    pos = []
    name = []
    with open(filename, 'r') as magnets:
        for line in magnets:
            MyMagnet = Magnet(line.replace('\n', ''))
            
            if MyMagnet.alias == 'HOR': 
                I_x.append(round(MyMagnet.get_current(),4))
                I_y.append(0)
                I_q.append(0)
                pos.append(round(MyMagnet.get_Z(),3)) 
                name.append(MyMagnet.name.replace('PITZ.CA/MAGNETS/',''))
                continue
            
            if MyMagnet.alias == 'VERT':
                I_x.append(0)
                I_y.append(round(MyMagnet.get_current(),4))
                I_q.append(0)
                pos.append(round(MyMagnet.get_Z(),3)) 
                name.append(MyMagnet.name.replace('PITZ.CA/MAGNETS/',''))
                continue
            
            if MyMagnet.alias == 'ROT':
                x,y = MyMagnet.get_current() 
                I_x.append(round(x,4))
                I_y.append(round(y,4))
                I_q.append(0)
                pos.append(round(MyMagnet.get_Z(),3)) 
                name.append(MyMagnet.name.replace('PITZ.MAGNETS/STEEROT/',''))
                continue
            
            if MyMagnet.alias == '':
                I_x.append(0)
                I_y.append(0)
                I_q.append(round(MyMagnet.get_current(),4))
                pos.append(round(MyMagnet.get_Z(),3)) 
                name.append(MyMagnet.name.replace('PITZ.CA/MAGNETS/',''))
                continue
            
            del MyMagnet            
    return name, I_x, I_y, I_q, pos

def fill_excel(name, I_x, I_y, I_q, pos):
    #df = DataFrame({'Name': name, 'X current ': round(I_x,4), 'Y current': round(I_y,4), 'Quad current': round(I_q,4), 
                    #'Position': round(pos,3)})
    df = DataFrame( {'Name': name, 
                    'X current ': I_x, 
                    'Y current': I_y, 
                    'Quad current': I_q, 
                    'Position': pos,} )
    df.to_excel('test.xls', sheet_name='sheet1', index=False)
    
def draw_trajectory(filename):
    x,y,BPMpos = read_trajectory(filename)
    plt.vlines(x = BPMpos, ymin = min(min(x),min(y)), ymax = max(max(x),max(y)), colors = 'purple', linestyle='dashed',linewidth=2)
    plt.plot(BPMpos,x)
    plt.plot(BPMpos,y)    
     
def draw_currents(filename):
    curr,Mpos = read_currents(filename)
    plt.plot(Mpos,curr, 'go')

def 
if __name__ == "__main__":

    BPM_file = 'BPMnames.txt'
    Magnets_file = 'Magnets_names.txt'
    
    #plt.grid(visible=True, which='major', axis='both')
    #plt.xlabel("Path length, a.u.")
    #plt.ylabel("Transversal position, a.u.")
    n,x,y,q,z = read_currents(Magnets_file)
    fill_excel(n,x,y,q,z)
    #draw_trajectory(BPM_file)
    #draw_currents(Magnets_file)
    
    #plt.tight_layout()
    #plt.show()   