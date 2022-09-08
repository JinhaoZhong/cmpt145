##Nmae:Jinhao Zhong NSID:jiz263  student#:11204178 Cmpt145  L05

import numpy as np
def square():
##set up the 4*4 square
    numbers=input('Type 16 integers(no comma or space):')
    a=[int(i) for i in numbers]
    lat_square=np.array(a).reshape(4,4)

##sum up every columns
    y=lat_square.sum(axis=0)
##sum up every rows
    x=lat_square.sum(axis=1)

## check if the sum of every colums and rows are equal
    if x.min()==x.max() == y.min()==x.max() :
        ##print yes if it is latiin square
        print('yes')
        ##print no if it is not latin square
    else:
        print('No')

##run the program
square()