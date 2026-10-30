#bad linear probe method
#bad linked list method
#better linear probe method
#better linked list method
#one big attempt at optimization
#one uses movie title, one uses movie quote

import time
from datetime import datetime
from Movie import Movie

titleList = []
quoteList = []
hashSize = 15000

#next is for linkedlist, get this out of here
def fillTitle():
    for i in range(1, hashSize):
        current = Movie()
        titleList.append(current)
        if(i > 0):
            titleList[i -1].next = current


def fillQuote():
    for i in range(1, hashSize):
        current = Movie()
        quoteList.append(current)
        if(i > 0):
            quoteList[i -1].next = current

def hash():
    #something is wrong with reading this file. I will need help to fix this.
    file = open("MOCK_DATA.csv", "r")
    data = file.read().split("\n")
    for i in range(1, len(data) - 2): #1 for header, -2 to account for blank line at end of mock data
        row = data[i].split(",")
        title = str(row[0])
        quote = str(row[8])
        titleIndex = asciiIfy(title)%hashSize
        quoteIndex = asciiIfy(quote)%hashSize

        target = titleList[titleIndex]
        if(target.status == 0):
            target.title = title
            target.quote = quote
            target.status = 1
        else:
            original = target
            while(target.next.status != 0 & target.next != original):
                target = target.next
            if(target != original):
                target.title = title
                target.quote = quote
                target.status = 1

        target = quoteList[quoteIndex]
        if(target.status == 0):
            target.title = title
            target.quote = quote
            target.status = 1
        else:
            original = target
            while(target.next.status != 0 & target.next != original):
                target = target.next
            if(target != original):
                target.title = title
                target.quote = quote
                target.status = 1
    return 

def asciiIfy(word):
    value = 0
    for i in word:
        value += ord(i)
    return value

fillTitle()
fillQuote()
hash()
print(titleList)