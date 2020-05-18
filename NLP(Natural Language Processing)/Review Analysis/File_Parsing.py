from bs4 import BeautifulSoup
import re

sentence_pat = re.compile(r"[.?!][ \n\t]")
wordpat  = re.compile(r"[A-Za-z]+[A-Za-z']?[A-Za-z]+", re.IGNORECASE)
bos = "__BOS__"

def parser():
    doc= open("test.xml","r")
    contents = doc.read()
    soup = BeautifulSoup(contents,'xml')
    reviews = soup.find_all('review_text')
    number_of_reviews=0
    word_list=[[]]
    prev  = bos
    for review in reviews:
        number_of_reviews+=1
    total_word_list=[]
    for review in reviews:
        s=review.get_text()
        for w in wordpat.finditer(s):
            x,y = w.span()
            key = s[x:y].lower()
            if y - x > 1:
                word_list.append((prev,key))
                prev=key
        total_word_list.append(word_list)
        word_list=[]
    #print(total_word_list[0])
    return total_word_list
    
    
