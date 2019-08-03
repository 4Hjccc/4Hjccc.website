# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 09:22:37 2019

@author: study
"""

for x in range(1, 10):
    line = ""
    for y in range(1, x):
        if (y<4):
            line = line + "      "
        else:
            line = line + "       "
            
    for y in range(x, 10):
        if (x==1 and y>=4):
            line = line + str(x)+"X"+str(y)+"="+str(x*y)+"  "
        elif (x==2 and y==4):
            line = line + str(x)+"X"+str(y)+"="+str(x*y)+"  "
        else:                
            line = line + str(x)+"X"+str(y)+"="+str(x*y)+" "
    print(line)