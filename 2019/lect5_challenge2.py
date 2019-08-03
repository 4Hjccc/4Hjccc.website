# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:15:13 2019

@author: work
"""

tree_top_height = input("Please enter the height of tree top:")
tree_trunk_height =  input("please enter the height of the tree trunk:")
treetop = int(tree_top_height)
treetrunk = int(tree_trunk_height)

# print the tree top
for x in range(1, treetop+1):
    Astr="A"*(2*x-1)
    line=Astr.center(2*treetop+1)
    print(line)
    
# print the tree chunk
Hstr="H"
line = Hstr.rjust(treetop+1)

for x in range(treetrunk):
    print(line)
    
# print the tree base
line = ""
for x in range(2*treetop+1):
    line = line+"-"
print(line)