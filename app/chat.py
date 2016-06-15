from app import db, models
import random
import sys

MAX_LENGTH = 46
MIN_LENGTH = 5

def getReply(bot, message):
    message = message.lower().split()
    chainStart = scanKey(bot, message)
    reply = chainReply(bot, chainStart)
    return ' '.join(capFirst(reply))
    
def scanKey(bot, message):
    while len(message) >= 2:
        searchKey = ' '.join(message[-2:])
        message = message[:-2]
        res = models.Markov.query.filter_by(author=bot, chain=searchKey).first()
        if res is not None:
            return res.chain
    numRows = models.Markov.query.count()
    res = models.Markov.query.get(random.randrange(1, numRows + 1))
    return res.chain
    
def chainReply(bot, chainStart):
    msg = chainStart.split()
    while (len(msg) < MAX_LENGTH) and (len(msg) < MIN_LENGTH or not isEnding(msg[-1])):
        nextWord = getNext(bot, msg[-2:])
        msg.append(nextWord)
    return msg

def getNext(bot, words):
    searchKey = ' '.join(words)
    res = models.Markov.query.filter_by(author=bot, chain=searchKey).all()
    if not res:
        return getRand(bot)
    n = random.randrange(0, len(res))
    return res[n].nextWord

def getRand(bot):
    numRows = models.Markov.query.count()
    res = models.Markov.query.get(random.randrange(1, numRows + 1))
    return res.nextWord

def isEnding(word):
    return word[-1] in "!?."
    
def capFirst(msg):
    msg[0] = msg[0].capitalize()
    for i in range(len(msg) - 1):
        if msg[i][-1] in "?!.":
            msg[i + 1] = msg[i + 1].capitalize()
    return msg