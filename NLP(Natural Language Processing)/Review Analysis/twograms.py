import re
from collections import defaultdict
import xml.etree.ElementTree as ET

sentence_pat = re.compile(r"[.?!][ \n\t]")
wordpat  = re.compile(r"[A-Za-z]+[A-Za-z']?[A-Za-z]+", re.IGNORECASE)

bos = "__BOS__"

stopwords = ["able", "about", "across", "after", "all", "almost", "also", "am", "among",
"an", "and", "any", "are", "as", "at", "be", "because", "been", "but", "by",
"can", "cannot", "could", "dear", "did", "do", "does", "either", "else",
"ever", "every", "for", "from", "get", "got", "had", "has", "have", "he",
"her", "hers", "him", "his", "how", "however", "if", "in", "into", "is", "it",
"its", "just", "least", "let", "like", "likely", "may", "me", "might", "most",
"must", "my", "neither", "no", "nor", "of", "off", "often", "on",
"only", "or", "other", "our", "own", "rather", "said", "say", "says", "she",
"should", "since", "so", "some", "than", "that", "the", "their", "them",
"then", "there", "these", "they", "this", "tis", "to", "too", "twas", "us",
"wants", "was", "we", "were", "what", "when", "where", "which", "while", "who",
"whom", "why", "will", "with", "would", "yet", "you", "your"]

stopdict = {}

def process(s, dict):
    global wordpat
    prev  = bos
    nwords = 0
    tmpdict = defaultdict(lambda: 0)  
    for w in wordpat.finditer(s):
        x,y = w.span()
        key = s[x:y].lower()
        if y - x > 1 and key not in stopdict and prev not in stopdict:
            nwords += 1
            tmpdict[prev,key] += 1
            prev=key
    for key in tmpdict:         
        dict[key] += 1
def sentdict(pathlist):
    for w in stopwords:
            stopdict[w] = True
    
    
    d1 = defaultdict(lambda: 0)
    d2 = defaultdict(lambda: 0)
    dictlist = [d1,d2]
    
    for i in range(2):
        path = pathlist[i]
        doctree = ET.parse(path)
        root = doctree.getroot()

        for child in root:
            for item in child:
                if item.tag == "review_text":
                    process(item.text,dictlist[i])
    wk = list(d1.keys())    
    wk.extend(d2.keys())
    wk = set(wk)
    wk = list(wk)
    wk.sort()
    sentdict={}
    for k in range(len(wk)):
        k1 = d1[wk[k]]
        k2 = d2[wk[k]]
        if k1*k2<10:            
            continue
        sentdict[wk[k]]=(k1,k2)
    return sentdict