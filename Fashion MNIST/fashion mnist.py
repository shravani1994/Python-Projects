import sys
import numpy as np
from matplotlib import pyplot as plt
from scipy.special import expit

if __name__=="__main__":
    with open("fashion.pgm","r")  as fd:
        magic=fd.readline()
        dims=fd.readline().strip().split()
        cols=int(dims[0])
        rows=int(dims[1])
        maxpixel=int(fd.readline())
        pixels=[]
        for line in fd.readlines():
            pixels+=map(int,line.strip().split())
        row=rows//30
        col=cols//30
        a=np.array(pixels).reshape(rows,cols)
        plt.imshow(a)
        b=a.reshape(30,row,30,col)
        c=b.transpose(0,2,1,3)
        d=c.reshape(900,row,col)
        avgint=d.sum(axis=0)
        avgint=avgint/900
        print('the average pixel intensity')
        print('Uncomment the below')
        #plt.imshow(avgint)
        print(np.mean(d))
        print('zero pixels are in the big picture')
        print('The number of zero pixels =',np.sum(a==0))
        print(np.argmax(np.sum(d==0,axis=(1,2))))
        print('Maximum number of zero pixels in any of the little pictures')
        print('Maximum number of zero pixels in any of the little pictures=',np.count_nonzero(d[519]==0))
        counts={}
        for i in range(0,255):
            counts[i]=0
        for i in pixels:
            val=counts.get(i,0)
            counts[i]=val+1
        keymax=max(counts,key=counts.get)
        print('pixel value occurs most often in the big picture')
        print('Pixel which occurs most often=',keymax)
        secmax=list(sorted(counts.values()))[-2]
        keylist=list(counts.keys())
        valist=list(counts.values())
        print('pixel value occurs the second most often in the big picture')
        print('Pixel which occurs second most often=',keylist[valist.index(secmax)])
        bags=d[720:810,:,:]
        tmp=bags.flatten()
        pix_in_bags=set(tmp)
        totalpix={0}
        for i in range(1,256):
            totalpix.add(i)
        print('pixel values do not appear at all in the little pictures of bags')
        print('The pixels not in bags=',sorted(totalpix-pix_in_bags))
        print('Plot the frequency of pixel values in all pictures of pants')
        labels=np.arange(len(pants_pixels))
        index=np.arange(len(pants_pixels))
        print('Uncomment the below')
        #plt.bar(index,pants_pixels)
        #plt.xlabel('Pixel Value')
        #plt.ylabel('Frequency')
        #plt.xticks(index, labels, fontsize=5, rotation=30)
        #plt.show()
        sandals=d[450:540,:,:]
        sneakers=d[(21*30):(24*30),:,:]
        boots=d[(27*30):(30*30)]
        footwear=np.concatenate([sandals,sneakers,boots])
        footwear_final=footwear.reshape(3,6,15,28,28)
        temp1=footwear_final.transpose(0,1,3,2,4)
        temp2=temp1.reshape(504,420)
        print('a new picture showing only the little pictures of footwear')
        #plt.imshow(temp2)
        #plt.show()
        pants=d[90:180,:,:]
        pants_flatten=pants.flatten()
        pants_pixels=np.bincount(pants_flatten)
        print('Problem 9')
        eucledian_distance=[]
        for i in range(0,90):
            eucledian_distance.append(np.sum((boots[0]-boots[i])**2))
        print('The image of the boot closest to the first image of the boot is =',np.argmin(eucledian_distance[1:])+1)
        print('Problem 10')
        e=np.transpose(a)
        plt.imshow(e)
        plt.show()
