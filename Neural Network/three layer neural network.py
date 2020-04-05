import sys
import numpy as np
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
        
    w1 = np.load('w1.npy')
    w2 = np.load('w2.npy')
    x  = np.array(pixels).reshape(1536,1)
    z2 = np.matmul(w1,x)
    a2 = expit(z2)
    z3 = np.matmul(w2,a2)
    a3 = expit(z3)
    hafxy=['H','A','F','X','Y']
    maxvalue=np.argmax(a3)
    print('Predicted Letter :',hafxy[maxvalue])
    print(np.round(a3,9))
    