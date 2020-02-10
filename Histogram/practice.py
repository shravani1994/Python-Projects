import sys
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

if __name__=="__main__":
    with open("E:/Indiana State University/Data Science 2/Assignments/Assignment 1/ages2.txt") as fd:
        age=[]
        for line in fd.readlines():
            tmp=line.rstrip().split('\n')
            age.append(float(tmp[0]))
        age=list(map(int,age))
        x=[i for i in range(5,100,5)]
        y=[i for i in range(0,25000,5000)]
        plt.style.use('ggplot')
        plt.figure(figsize=(16,9),dpi=100)
        a,b,_=plt.hist(age,bins=x,histtype='bar',edgecolor='black',linewidth=3)
        largest_group=int(a.max())
        for i in range(len(a)):
            if(a[i]==largest_group):
                index=i
        for i in range(len(b)):
            lower_bound=b[index]
            upper_bound=b[index+1]-1
        plt.title('Ages of Python Programmers',color='blue',fontsize=30)
        plt.xlabel('Age Range',color='blue',fontsize=15)
        plt.ylabel('Number of People',color='blue',fontsize=15)
        plt.xticks(x)
        maxage=max(age)
        minage=min(age)
        mean=round(sum(age)/len(age),2)
        text1 = 'Maximum Age : '+str(maxage)
        text2 = 'Minimum Age : '+str(minage)
        text3 = 'Mean Age : '+str(mean)
        text4 = 'Largest group : ages '+str(lower_bound)+' to '+str(upper_bound)+' , '+str(largest_group)+' people'
        extra = Rectangle((0, 0),1,1,fc="w", fill=False, edgecolor='none', linewidth=2)
        plt.annotate(text4, xy=(upper_bound+1,largest_group-5000), xytext=(upper_bound+5,largest_group-5000),color='red',fontsize='large',va='center',arrowprops=dict(facecolor='black', width=5,shrink=0.1))
        legend=plt.legend([extra,extra,extra],[text1, text2,text3], loc='center',fontsize='large')
        plt.setp(legend.get_texts(), color='red')
        plt.rcParams["legend.fancybox"] = True
        plt.rcParams["legend.edgecolor"] = 'black'
        plt.show()

