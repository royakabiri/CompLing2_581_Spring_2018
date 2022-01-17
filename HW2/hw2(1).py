#import all the relevant modules
import sys
import nltk
from nltk.corpus import cmudict


#I created a loop to handle the cases where the user might enter more than a word at the same time
#for each word typed in the command line
for word in sys.argv[1:]:

#based on what I tested, cmudict is not case-sensitive
#but to be in the safe side, I make the letters lowercase
	word=word.lower()
	#if the word exists in the dictionary
	if word in cmudict.dict():
		#return the pronounciation of that word
		result=cmudict.dict()[word]
		#creat a counter to count the number of syllables
		numOfsyll= 0
		#create a list including the digits used in the cmudict
		digitList= ['0','1','2']
		#for the first list in the list (as cmudict return a list of lists)
		#as the number of syllables are the same even if the word has more than a pronouncuation,
		#I index only to the first list, so the code just loop through it
		for phonemes in result[0]:
			#if the last character of each member of the list is a digit  
			if phonemes[-1] in digitList:
				#increment the counter
				numOfsyll+=1
		#create is...else to handle the plural 's' in the word 'syllables' in print statement
		if numOfsyll == 1:
			print('The word', '"'+word+'"', 'has', numOfsyll, 'syllable.')
		else:
			print('The word', '"'+word+'"', 'has', numOfsyll, 'syllables.')

	#if the word is not in the dicrionary
	else:
		print ('Oops! The word','"', word, '"', 'is not in cmudict!')










