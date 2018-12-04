import pickle
import sys
sys.path.append('../')
import utilities


def train(f):
    vocabulary = 26 #number of letters in the alphabet
    #Open file (concatination of both books)
    with open(f, 'r') as myFile:
        training = myFile.read()
    
    training = utilities.purge_string(training)
    
    total_chars = len(training)
    print (total_chars)
    
    unigramPT = {}
    with open('PT/unigramPT.txt', 'w') as myFile:
        for x in range(97, 123):
            count = training.count(chr(x))
            prob =  count/total_chars
            smoothed_prob = (count+0.5)/(total_chars+vocabulary*0.5)
            print ("{} {}'s in corpus => probability = {} => smoothed {}".format(count, chr(x), prob, smoothed_prob))
            myFile.write('({}) = {}\n'.format(chr(x), smoothed_prob))
            unigramPT[chr(x)] = smoothed_prob
            
    print (unigramPT)
    with open('PT/unigramPT.pkl', 'wb') as myFile:
        pickle.dump(unigramPT, myFile)
    return unigramPT
#train('PT/trainPT.txt')
