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
    
    bigramFR = {}
    with open('FR/bigramFR.txt', 'w') as myFile:
        for x in range(97, 123):
            count = training.count(chr(x))
            bigramFR[chr(x)] = {}
            for y in range(97, 123):
                bi_count = training.count(chr(x)+chr(y))
                bi_prob = bi_count/count
                bi_smoothed_prob = (bi_count+0.5)/(count+vocabulary*0.5)
                print ("{} {}'s => {} {}'s followed by {}'s => probability = {} => smoothed {}".format(count, chr(x), bi_count,chr(x), chr(y), bi_prob, bi_smoothed_prob))
                myFile.write('({}|{}) = {}\n'.format(chr(y), chr(x), bi_smoothed_prob))
                bigramFR[chr(x)][chr(y)] = bi_smoothed_prob
            
    #print (bigramFR)
    with open('FR/bigramFR.pkl', 'wb') as myFile:
        pickle.dump(bigramFR, myFile)
    return bigramFR

#train('trainFR.txt')
