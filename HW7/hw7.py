import re
#read section 23
f = open('section23.txt','r')
text = f.read()
f.close()
#remove empty categories and extra symbols
newText=re.sub('wsj_23.*mrg-[0-9]+\s+', '', text)
newText=re.sub ('\*T\*-[0-9]+', '', newText)
newText=re.sub ('\*-[0-9]+', '', newText)
newText=re.sub ('\*U\*', ' ', newText)
newText=re.sub ('\*EXP(\*-[0-9]+)?', '', newText)
newText=re.sub ('\*ICH\*-[0-9]+', '', newText)
newText=re.sub ('\*ICH\\b', '', newText) 
newText=re.sub ('-LRB-', '', newText)
newText=re.sub ('-LCB-', '', newText)
newText=re.sub ('-RCB-', '', newText)
newText=re.sub ('-RRB-', '', newText)
newText=re.sub ('\\b0\\b', '', newText)
newText=re.sub ('\\b\*\\b', '', newText)
#remove extra spaces
newText=re.sub ('[ \t]{2,}', ' ', newText) 

#open a new file stream and write the cleaned text to it
outFile = open('cleanedSection.txt','w')
outFile.write(newText)
outFile.close()
#read the new file and add parentheses and write them to a new text file
f = open('cleanedSection.txt','r')
outF = open('cleanedSectionLast.txt','w')
line=f.readline()
while line:
	line=line.strip('\n')
	line= "("+line+")"+'\n' 
	outF.write(line)    
	line=f.readline()
f.close()
outF.close()



