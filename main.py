from math import log10
import utilities
import sys
sys.path.append('EN')
sys.path.append('FR')
sys.path.append('PT')
import unigramEN
import bigramEN
import unigramPT
import bigramPT
import unigramFR
import bigramFR
import pickle

#Train 
#unigramEN = unigramEN.train('EN/trainEN.txt')
#bigramEN = bigramEN.train('EN/trainEN.txt')
#unigramPT = unigramPT.train('PT/trainPT.txt')
#bigramPT = bigramPT.train('PT/trainPT.txt')
#unigramFR = unigramFR.train('FR/trainFR.txt')
#bigramFR = bigramFR.train('FR/trainFR.txt')

#Or import trained model
with open('EN/unigramEN.pkl', 'rb') as myFile:
    unigramEN = pickle.load(myFile)
with open('EN/bigramEN.pkl', 'rb') as myFile:
    bigramEN = pickle.load(myFile)
#Or import trained model
with open('FR/unigramFR.pkl', 'rb') as myFile:
    unigramFR = pickle.load(myFile)
with open('FR/bigramFR.pkl', 'rb') as myFile:
    bigramFR = pickle.load(myFile)
#Or import trained model
with open('PT/unigramPT.pkl', 'rb') as myFile:
    unigramPT = pickle.load(myFile)
with open('PT/bigramPT.pkl', 'rb') as myFile:
    bigramPT = pickle.load(myFile)


with open('input.txt', 'r') as myFile:
    sentences = myFile.read()

sentences = sentences.split('\n')
sentences.pop() # Remove the last elemnt ''
#print (sentences)
purged_sentences = [utilities.purge_string(s) for s in sentences]
#print (purged_sentences)

log_prob_unigramEN = 0
#loop over the different sentences
for i in range(len(sentences)):
    log_prob_unigramEN = 0
    log_prob_bigramEN = 0
    log_prob_unigramFR = 0
    log_prob_bigramFR = 0
    log_prob_unigramPT = 0
    log_prob_bigramPT = 0
    output_file = 'out'+str(i+1)+'.txt'
    #File setup
    with open(output_file, 'w') as myFile:
        myFile.write(sentences[i]+'\n'+'\n')
        myFile.write('UNIGRAM MODEL:\n\n')
        #loop ovr each character in a sentence
        for c in purged_sentences[i]:
            log_prob_unigramEN += log10(unigramEN[c])
            log_prob_unigramFR += log10(unigramFR[c])
            log_prob_unigramPT += log10(unigramPT[c])
            myFile.write('UNIGRAM {}:\n'.format(c))
            myFile.write('ENGLISH P({}): = {} ==> log prob of sentence so far: {}\n'.format(c, unigramEN[c], log_prob_unigramEN))
            myFile.write('FRENCH P({}): = {} ==> log prob of sentence so far: {}\n'.format(c, unigramFR[c], log_prob_unigramFR))
            myFile.write('PORTUGUESE P({}): = {} ==> log prob of sentence so far: {}\n'.format(c, unigramPT[c], log_prob_unigramPT))
            myFile.write('\n')
        max_value = max(log_prob_unigramEN, log_prob_unigramFR, log_prob_unigramPT)
        if (max_value == log_prob_unigramEN):
            myFile.write('According to the unigram model, the sentence is in English')
            print('According to the unigram model, the sentence {} is in English'.format(sentences[i]))
        if (max_value == log_prob_unigramFR):
            myFile.write('According to the unigram model, the sentence is in French')
            print('According to the unigram model, the sentence {} is in French'.format(sentences[i]))
        if (max_value == log_prob_unigramPT):
            myFile.write('According to the unigram model, the sentence is in Portuguese')
            print('According to the unigram model, the sentence {} is in Portuguese'.format(sentences[i]))
            myFile.write('\n')

        myFile.write('------------------\n\n')
        myFile.write('BIGRAM MODEL:\n\n')
        for j in range(len(purged_sentences[i])-1):
            current_c = purged_sentences[i][j] #First character in current bigram
            next_c = purged_sentences[i][j+1] #Second character in current bigram
            log_prob_bigramEN += log10(bigramEN[current_c][next_c])
            log_prob_bigramFR += log10(bigramFR[current_c][next_c])
            log_prob_bigramPT += log10(bigramPT[current_c][next_c])
            myFile.write('BIGRAM {}{}:\n'.format(current_c, next_c ))
            myFile.write('ENGLISH P({}|{}): = {} ==> log prob of sentence so far: {}\n'.format(next_c, current_c, bigramEN[current_c][next_c], log_prob_bigramEN))
            myFile.write('FRENCH P({}|{}): = {} ==> log prob of sentence so far: {}\n'.format(next_c, current_c, bigramFR[current_c][next_c], log_prob_bigramFR))
            myFile.write('PORTUGUEESE P({}|{}): = {} ==> log prob of sentence so far: {}\n'.format(next_c, current_c, bigramPT[current_c][next_c], log_prob_bigramPT))
            myFile.write('\n')
        max_value = max(log_prob_bigramEN, log_prob_bigramFR, log_prob_bigramPT)
        if (max_value == log_prob_bigramEN):
            myFile.write('According to the bigram model, the sentence is in English')
            print('According to the bigram model, the sentence {} is in English'.format(sentences[i]))
        if (max_value == log_prob_bigramFR):
            myFile.write('According to the bigram model, the sentence is in French')
            print('According to the bigram model, the sentence {} is in French'.format(sentences[i]))
        if (max_value == log_prob_bigramPT):
            myFile.write('According to the bigram model, the sentence is in Portuguese')
            print('According to the bigram model, the sentence {} is in Portuguese'.format(sentences[i]))
            myFile.write('\n')


print (sentences)
print (purged_sentences)









