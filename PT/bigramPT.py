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
    
    bigramPT = {}
    with open('PT/bigramPT.txt', 'w') as myFile:
        for x in range(97, 123):
            count = training.count(chr(x))
            bigramPT[chr(x)] = {}
            for y in range(97, 123):
                bi_count = training.count(chr(x)+chr(y))
                bi_prob = bi_count/count
                bi_smoothed_prob = (bi_count+0.5)/(count+vocabulary*0.5)
                print ("{} {}'s => {} {}'s followed by {}'s => probability = {} => smoothed {}".format(count, chr(x), bi_count,chr(x), chr(y), bi_prob, bi_smoothed_prob))
                myFile.write('({}|{}) = {}\n'.format(chr(y), chr(x), bi_smoothed_prob))
                bigramPT[chr(x)][chr(y)] = bi_smoothed_prob
            
    #print (bigramPT)
    with open('PT/bigramPT.pkl', 'wb') as myFile:
        pickle.dump(bigramPT, myFile)
    return bigramPT

#train('trainPT.txt')
