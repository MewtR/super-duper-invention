
vocabulary = 26 #number of letters in the alphabet
#Open file (concatination of both books)
with open('trainEN.txt', 'r') as myFile:
    training = myFile.read()

#Remove everything that isn't a letter
training = ''.join(c for c in training if ((ord(c) > 96 and ord(c) < 123) or (ord(c) > 64 and ord(c) < 91)))

#Make it lower case
training = training.lower()
#print (training)
total_chars = len(training)
print (total_chars)

#for x in range(97, 123):
#    count = training.count(chr(x))
#    prob =  count/total_chars
#    smoothed_prob = (count+0.5)/(total_chars+vocabulary*0.5)
#    print ("{} {}'s in corpus => probability = {} => smoothed {}".format(count, chr(x), prob, smoothed_prob))
with open('unigramEN.txt', 'w') as myFile:
    for x in range(97, 123):
        count = training.count(chr(x))
        prob =  count/total_chars
        smoothed_prob = (count+0.5)/(total_chars+vocabulary*0.5)
        print ("{} {}'s in corpus => probability = {} => smoothed {}".format(count, chr(x), prob, smoothed_prob))
        myFile.write('({}) = {}\n'.format(chr(x), smoothed_prob))
        
