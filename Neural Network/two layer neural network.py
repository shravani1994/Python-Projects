import sys
import numpy as np
from random import randrange
from matplotlib import pyplot as plt
from scipy.special import expit 

if __name__ == "__main__":
    
    with open(sys.argv[1],'r') as fd:
        magic = fd.readline()
        if magic[0:2] != "P1":
            print("not a pbm file", file=sys.stderr)
            sys.exit(0)
        dims = fd.readline().strip().split()
        cols = int(dims[0])
        rows = int(dims[1])
        pixels = []
        for line in fd.readlines():
            pixels += map(int, line.strip().split())
    n = len(pixels)
    if len(pixels) != rows*cols:
        print("wrong number of pixels: {0:d} != {1:d}".format(n, rows*cols), file=sys.stderr)
        sys.exit(0)
    
    
    w = np.load('twolevel.npy')
    x  = np.array(pixels).reshape(1536,1)
    z = np.matmul(w,x)
    a = expit(z)
    hafxy=['H','A','F','X','Y']
    maxvalue=np.argmax(a)
    print('Predicted Letter :',hafxy[maxvalue])
    print(np.round(a,9))

