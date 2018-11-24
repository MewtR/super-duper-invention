

with open('TrainingCorpusENandFR/en-moby-dick.txt', 'r') as myFile:
    moby_dick = myFile.read()

moby_dick = ''.join(c for c in moby_dick if ((ord(c) > 96 and ord(c) < 123) or (ord(c) > 64 and ord(c) < 91)))

print (moby_dick)
