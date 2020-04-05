from random import randrange
import array
import gzip
import numpy as np
import struct
import sys
import torch
from matplotlib import pyplot as plt
import scipy as sp

dir = "EMNIST/"   

files = [
  "emnist-letters-test-images-idx3-ubyte.gz",
  "emnist-letters-test-labels-idx1-ubyte.gz",
  "emnist-letters-train-images-idx3-ubyte.gz",
  "emnist-letters-train-labels-idx1-ubyte.gz"]

def readset(imagefile, labelfile):
    global dir

    with gzip.open(dir + imagefile,"rb") as fd:
        magic, count, rows, cols = struct.unpack(">IIII", fd.read(16))
        tmp = array.array("B", fd.read(count*rows*cols))
    img=np.array(tmp)

    with gzip.open(dir + labelfile,"rb") as fd:
        magic, count = struct.unpack(">II", fd.read(8))
        tmp = array.array("B", fd.read(count))
        ans = np.array(tmp)

    return img, ans

if __name__ == "__main__":

    x2, testans  = readset(files[0], files[1])
    x2=x2.reshape(20800,28,28)
    x4=x2.transpose(0,2,1)
    x5=x4.reshape(26,800,28,28)
    x6=x5[0,:,:,:]
    means=np.sum(x2,axis=(1,2))/784
    print('The image with greatest pixel density =',np.argmax(means))
    pixel_density= x6.sum(axis=0)
    pd=pixel_density/800
    print('The average pixel value in row 3 column 5=',pd[2,4])
    distances=[]
    pixel_density= x5.sum(axis=(1))
    pd1=pixel_density/800
    for i in range(0,26):
        distances.append(np.sum((pd-pd1[i])**2))
    sd=sorted(distances)
    avg_req_value=sd[1]
    avg_index=distances.index(avg_req_value)
    print('The letter closest to D=',chr(65+avg_index))  
    listing=[]
    for i in range(0,800):
        for j in range(0,800):
            listing.append(784-(np.sum(x6[i]==x6[j])))
    maxdistance=[]
    a=0
    for x in range(0,800):
        maxdistance.append(max(listing[a:800+a]))
        a=a+800
    gd=max(maxdistance)
    firstpic=maxdistance.index(gd)
    secndpic=listing[(800*firstpic):(800*firstpic)+800]
    secpic=secndpic.index(gd)
    print('The two pictures which are at a greater distance are',firstpic,secpic)
    x7=x6.reshape(20,40,28,28)
    x8=x7.transpose(0,2,1,3)
    x9=x8.reshape(560,1120)
    #sp.misc.imsave('pictures.pgm',x9)