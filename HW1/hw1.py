import nltk
import random
import sys
from nltk.tokenize import word_tokenize
from nltk import pos_tag, sent_tokenize
from nltk.corpus import gutenberg
from random import seed, randrange
from nltk.corpus import cmudict




nltk.download()
from nltk.corpus import treebank
treebank.words()
len(treebank.words())
treebank.fileids()



for x in range(5):
	print (random.randint(1,200))

treebank.parsed_sents("wsj_0089.mrg")[0]

sentence = treebank.parsed_sents("wsj_0089.mrg")[0]
sentence.draw()


# get the file names of gutenberg and choose alice
nltk.corpus.gutenberg.fileids()
rawText=nltk.corpus.gutenberg.raw('carroll-alice.txt')
sentsOfText=nltk.sent_tokenize(rawText)
len(sentsOfText)


for i in range(10):
	print(i,': ', sentsOfText[i])

# split the sentence into words
wordsList= nltk.tokenize.word_tokenize(sentsOfText[7])
# get the pos tags
taggedWords = nltk.pos_tag(wordsList)
print(taggedWords)

#get the syntax tree for a random sentence
random.seed()
treebank.parsed_sents("wsj_0"+str(random.randrange(200))+".mrg")[0].draw()

# use cmudict
cmudict.dict()['pizza']


### give only one random number at a time
random.seed()
random.randrange(200)


# pentree bank with nltk
from nltk.corpus import ptb
print(ptb.fileids())
ptb.categories()
ptb.words(categories=['news'])
ptb.tagged_words(categories=['news'])
ptb.sents(categories=['news'])
ptb.tagged_sents(categories=['news'])
ptb.parsed_sents(categories=['news'])
ptb.parsed_sents(categories=['news'])[0].draw()

s = ptb.parsed_sents(categories=['news'])[0]
s.productions() # returns tree
s.leaves() # returns words
s.flatten() # returns only the top of the tree with words
s.height() # returns number of nodes
s.pos() # returns pos tags

chomsky_normal_form()
fromstring()
pretty_print()

t = ptb.words(categories=['news'])
text = nltk.Text(t)
words = set(text)
# number of distinct words
len(words)
# lexical diversity
len(words)/len(text)
# {:.3f} get till 3 significant figures after the decimal point
print('Lexical diversity: {:.3f}%'.format(len(words)/len(text)))



# count freqency of "the" 
text.count("the")
text.count("The")
# return the 1000th word
# because index starts from 0, it should be one less. 
# text[1000] returns 1001st word
text[999]
# get first occurence of a word (index to it)
text.index("be")


# get stopwords in English 
stopwords.words('english')

# plot 50 most common words
# pip3 install matplotlib 
d = nltk.FreqDist(text)
print(d)
d.plot(50, cumulatice=True)
# returns most frequent word
d.max()
# the words that occur only once
d.hapaxes()
# returns the number of its freq
d.freq("the")
# get 10 most freq items with their freq number
d.tabulate(10)

# sorting
sorted([1,4,3,2,8,9,6])
sorted([1,4,3,2,8,9,6],reverse=True)
# sorting freq distribution we got above 
# t[1]: sort the items by the second member of the tuple which is the frequency
lst = sorted(d.items(), key=lambda t:t[1], reverse=True)
lst[:10]


# print number of syllables in a word 
aeiou = set("AEIOU")

def (word):
	try:
		ll = cmudict.dict()[word]
		for l in ll:
			vowels = [x for x in l if x[0] in aeiou]
			print('{} has {} syllable(s)'.format(word, len(vowels)))
	except KeyError:
		print('{} is not in CMUDict'.format(word))

if __name__ == "__main__":
	count(sys.argv[1])














