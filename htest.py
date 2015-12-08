"""
Histogram

General purpose histogram classes. 
"""
import numpy as np
import math

# Histogramming classes
class histaxis:
    def __init__(self,nbin,low,high):
        self.low = low
        self.high = high
        self.nbin = nbin
        self.binsize = (high-low)/float(nbin)
    def bin(self,val):
        return int(math.floor((val-self.low)/self.binsize))
    def values(self):
        return np.linspace(self.low+0.5*self.binsize,self.high-0.5*self.binsize,self.nbin)

class hist1d:
    def __init__(self,nbinx,xlow,xhigh):
        self.data = np.zeros(nbinx)
        self.nbinx = nbinx
        self.xaxis = histaxis(nbinx,xlow,xhigh)
    def fill(self,xval,weight=1.0):
        xbin=self.xaxis.bin(xval)
        if xbin>=0 and xbin<self.xaxis.nbin:
            self.data[xbin] += weight
    def fillarr(self,xarr,weightarr):
        for x,w in zip(xarr,weightarr):
            self.fill(x,w)

class hist2d:
    def __init__(self,nbinx,xlow,xhigh,nbiny,ylow,yhigh):
        self.data = np.zeros((nbinx,nbiny))
        self.xaxis = histaxis(nbinx,xlow,xhigh)
        self.yaxis = histaxis(nbiny,ylow,yhigh)
    def fill(self,xval,yval,weight=1.0):
        xbin=self.xaxis.bin(xval)
        ybin=self.yaxis.bin(yval)
        if xbin>=0 and xbin<self.xaxis.nbin and ybin>=0 and ybin<self.yaxis.nbin:
            self.data[xbin,ybin] += weight

if __name__ == "__main__" :
    print('hello')
    h = hist1d(10,5,10)
    x = np.array([8,6.1,6.2])
    w = np.array([3,2,3])
    h.fillarr(x,w)
    print h.data
