import sys
import nltk
from nltk.corpus import cmudict

word=input('Please type a word: ')
word=word.lower()
if word in cmudict.dict():
	result=cmudict.dict()[word]
		#print(result)
	numOfsyll= 0
	digitList= ['0','1','2']
	for phonemes in result[0]:
		#print(phonemes) 
		if phonemes[-1] in digitList:
			numOfsyll+=1

	if numOfsyll == 1:
		print('The word', '"'+word+'"', 'has', numOfsyll, 'syllable.')
	else:
		print('The word', '"'+word+'"', 'has', numOfsyll, 'syllables.')

else:
		print ('Oops! The word','"', word, '"', 'is not in cmudict!')