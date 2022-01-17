#punctuationTags= ["-NONE-", "-LRB-", "-RRB-", "SYM", ":", ".", ",", "``", "''", "$", "(", ")", "#"]
# cd /Users/roya/nltk_data/corpora/ptb
# chmod -R u+w wsj
# for f in `find wsj`; do mv -v "$f" "`echo $f | tr '[a-z]' '[A-Z]'`"; done
# python

import nltk
from nltk.corpus import ptb



print(ptb.fileids())
ptb.categories()
#['news']
ptb.fileids('news')


allTokens=ptb.words(categories=['news'])
len(allTokens)
#1253013
rawText=nltk.Text(allTokens)
punctuationTags= ["-NONE-", "-LRB-", "-RRB-", "SYM", ":", ".", ",", "``", "''", "$", "(", ")", "#"]
taggedText= ptb.tagged_words(categories=['news'])
cleanedText=[x[0] for x in taggedText if x[1] not in punctuationTags]
len(cleanedText)
#1028278
distinctWords=set(cleanedText)
len(distinctWords)
#49175


def lexicalDiversity(text):
	result= len(set(text)/len(text))
	newresult=format(result, '.3g')
	return newresult



lexicalDiversity(cleanedText)
# '20.9'
#distGraph=FreqDist(cleanedText)
distGraph=nltk.FreqDist(cleanedText)
print(distGraph)
distGraph.plot(50, cumulative=True)

print(distGraph[:10])


totalNum=0
i=0
for i in distGraph:
	totalNum+int(x[1])
	i+1
	count=<1028278/2


	count=0
i=1
for i in fdist1.most_common(0:):
	while count=<1028278/2:
	count+=i[1]
	i+1

print(i)


mostFreq=distGraph.most_common()
count=0
i=1
while count<1028278/2:
	for i in mostFreq:
		count+=i[1]
		i+1
print(i)

x=1
sum(x[1] for x in structure)


for key, val in d.items():
    print val, key
    
new2=[]
for key, val in new.items():
	new2+=key.casefold(),val 
	print(new2)


 new2={}
for key, val in new.items():
	new2[key.casefold()]=val


list(d.items())











