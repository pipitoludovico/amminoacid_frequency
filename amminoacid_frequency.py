from collections import Counter

sequence = open('sequence.txt','r')
amino_acid = ['C', 'D', 'S', 'Q', 'K', 'P', 'T', 'F', 'A', 'X', 'G', 'I', 'E', 'L', 'H', 'R', 'W', 'M', 'N', 'Y', 'V']
for a in amino_acid:
    if a in sequence.readlines():
        print "Percentage of" + amino_acid[a] + "is" + ((protein.count(a)) * 100 / len(protein))
    else:
        print amino_acid[a] + "is not in sequence"