#code


pip install textblob

v = []
adj = []
adv = []
commonv = {}
commonadj = {}
commonadv = {}

from textblob import TextBlob
import nltk
nltk.download("punkt")
frank = open("frankenstein.txt")
text = str(frank.read())
text = text.lower()
text = TextBlob(text)
for word,pos in text.tags:
    if word == "i":
        continue
    elif pos[:2] == "VB":
        v.append(word)
    elif pos[:2] == "JJ":
        adj.append(word)
    elif pos[:2] == "RB":
        adv.append(word)
        
for word in v:
    commonv[word] = commonv.get(word,0)+1
for word in adj:
    commonadj[word] = commonadj.get(word,0)+1
for word in adv:
    commonadv[word] = commonadv.get(word,0)+1
commonv = sorted(commonv.items(),key=lambda x:x[1],reverse=True)
commonadj = sorted(commonadj.items(),key=lambda x:x[1],reverse=True)
commonadv = sorted(commonadv.items(),key=lambda x:x[1],reverse=True)
print("Verbs:",list(commonv)[:5])
print("Adjectives:",list(commonadj)[:5])
print("Adverbs:",list(commonadv)[:5])

frank.close()
