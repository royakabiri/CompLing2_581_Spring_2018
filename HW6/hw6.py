import nltk
from nltk.corpus import ptb
from cllections import Counter
from math impport log, log10
import matplotlib.pyplot as plt
from sys import argv

topN = int(argv[1]) if len(argv)==2 else 100

excluded = set(['-NONE', '-LRB', '-RRB', 'SYM', ':', '.', ',', '``' "''"])
TOKENS= [X[0] for x in ptb.tagged_words(categories=['news']) if x[1] not in excluded]
size=len(tokens)
c = Counter()
for token in tokens:
	c[token]+=1

mc= c.most_common()
print('corpus check: tokens:{} types:{} top5: {}'. format(size, len(mc), mc[:5])
ranks=[x for x in range(1,len(mc)+1)]
freq=[item[1]/size for item in mc]
plt.figure(1)
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.title('Log-log plot for freq vs rank for PTB WSJ for top-{} words'.format(topN))
plt.plot(ranks[:topN], freq[:topN])
plt.show()
