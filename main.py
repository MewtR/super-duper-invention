from math import log10
import utilities
import sys
sys.path.append('EN')
import unigramEN
import pickle

#Train 
#unigramEN = unigramEN.train('EN/trainEN.txt')

#Or import trained model
with open('unigramEN.pkl', 'rb') as myFile:
    unigramEN = pickle.load(myFile)


with open('input.txt', 'r') as myFile:
    sentences = myFile.read()

sentences = sentences.split('\n')
sentences.pop() # Remove the last elemnt ''
#print (sentences)
purged_sentences = [utilities.purge_string(s) for s in sentences]
#print (purged_sentences)

log_prob_unigramEN = 0
for i in range(len(sentences)):
    log_prob_unigramEN = 0
    output_file = 'out'+str(i+1)+'.txt'
    #File setup
    with open(output_file, 'w') as myFile:
        myFile.write(sentences[i]+'\n'+'\n')
        myFile.write('UNIGRAM MODEL:\n\n')
        for c in purged_sentences[i]:
            log_prob_unigramEN += log10(unigramEN[c])
            myFile.write('UNIGRAM {}:\n'.format(c))
            myFile.write('ENGLISH P({}): = {} ==> log prob of sentence so far: {}\n'.format(c, unigramEN[c], log_prob_unigramEN))
            myFile.write('\n')









