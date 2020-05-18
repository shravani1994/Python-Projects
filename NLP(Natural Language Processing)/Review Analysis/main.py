from File_Parsing import parser
from twograms import sentdict

if __name__=="__main__":
    
    test_reviews=parser()
    pathlist = ["positive.dvd.xml", "negative.dvd.xml"]
    sentdictionary=sentdict(pathlist)
    slist = []
    score = 1.0
    newl=tuple(sentdictionary.keys())
    for i in range(len(test_reviews)):
        score=1.0
        for j in range(0,len(test_reviews[i])):
            if test_reviews[i][j] in newl:
                factors = sentdictionary[test_reviews[i][j]]
                f = factors[0] / factors[1]
                score *= f
        if score<1:
            slist.append((i,round(score,4),'negative'))
        else:
            slist.append((i,round(score,4),'positive'))
    
    for i in range(0,len(slist)):
        print(i,slist[i][1],slist[i][2])
    
                
            
    