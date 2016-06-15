#!flask/bin/python
from app import db, models
import sys, codecs

def isValidChar(char):
    return not char in u"()<>[]'\"\\|+=\{\}_^~/"

# Usage ./train.py file author 
if len(sys.argv) is not 3:
    print "Usage: ./train.py [file] [author]"
    sys.exit()
author = unicode(sys.argv[2], "utf-8")
textFile = sys.argv[1]

# Markov(author, chain, nextWord)
with codecs.open(textFile, "r", "utf-8") as f:
    text = f.read()
    
allWords = (''.join(filter(isValidChar, text.lower()))).split()

while len(allWords) > 2:
    key = allWords[0] + ' ' + allWords[1]
    val = allWords[2]
    db.session.add(models.Markov(author=author, chain=key, nextWord=val)) 
    db.session.commit()
    allWords = allWords[1:]


