import sys

class Node:
    def __init__(self,index,data):
        self.index,self.data=index,data
        self.next=None

limit=10000
array=[None]*limit


def hashedFunction(s):
    hash_val = 0
    for position in range(len(s)):
        hash_val = hash_val + (ord(s[position]) * position+1)
    hash_val = hash_val % limit
    return hash_val

def insertNode(index,node,a):
    num=index
    while(True):
        if(a[num] == None):
            a[num]=node
            return
        else:
            curr= a[num]
            while(curr.next!= None):
                curr=curr.next
            curr.next=node
            return
        if(num >= limit):
            num=0
def deleteNode(index,ori,a):
    num = index
    curr=a[num]
    prev=None
    if(curr is not None):
        if(curr.index == ori):
            a[num]=curr.next
            curr=None
    while(curr is not None):
        if(curr.index == ori):
            break
        prev=curr
        curr=curr.next
    if(curr==None):
        return
    prev.next=curr.next
    curr=None
    if(num >= limit):
        num=0

def searchArray(index,ori,a):
    num = index
    while(True):
        if(a[num]== None):
            return "Not Present"
        curr=a[num]
        while(curr!=None):
            if(curr.index == ori):
                return curr.data
            curr=curr.next
        if(num >= limit):
            num=0
        if(num == index):
            return "Nope"

if(len(sys.argv)!=5):
    print("no")
    exit()

inputFile=sys.argv[1]
command=sys.argv[2]
readFile=sys.argv[3]
outFile=sys.argv[4]

f=open(inputFile,"r")

for line in f:
    inputArray = line.strip().split(":")
    hashedIndex = hashedFunction(inputArray[0])
    newNode=Node(inputArray[0],inputArray[1])
    insertNode(hashedIndex,newNode,array)
        #print("inserted" + inputArray[0])
    #else:
        #print("not enough room" +inputArray[0])


f.close()

if(str(command)=='search'):
    f= open(readFile,"r")
    w=open(outFile,"w")

    for line in f:
        search = line.strip()
        s_hash = hashedFunction(search)
        data = searchArray(s_hash,search,array)
        w.write(search + ":" + data+"\n")

    f.close()
    w.close()

if(str(command)=='delete'):
    f= open(readFile,"r")

    for line in f:
        delete = line.strip()
        s_hash = hashedFunction(delete)
        deleteNode(s_hash,delete,array)

    f.close()

    w=open(outFile,"w")
    curr=array[0]

    i=0
    while i < (len(array)):
        if(array[i]!=None):
            w.write(array[i].index+":"+array[i].data+"\n")
            while(array[i].next):
                w.write(array[i].next.index + ":" + array[i].next.data+"\n")
        i=i+1

    w.close()
