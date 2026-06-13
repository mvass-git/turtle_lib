import colors
from turtle import *

def spiral(r,col,d,k):
    color(col)
    for i in range(k):
        circle(r, 30)
        r+=d