#import operator
#import string
import os
import sys

dataFileName = 'data_small.txt'


def processData():
        '''
        gets data processes..documention #TODO
        '''
        #print dataFilePath
        f = open(dataFilePath,'r')
        data = f.readlines()

        wordDictionary = {}

        for line in data[0:5]:
                if len(line) == 0:
                        continue
                print line
                print '%d characters in tweet' % len(line)
 


# main part
dataFolder = os.path.join(os.getcwd(), "data")

# check if the data folder path and given file exists
# if not, sys.exit(1)

if os.path.exists(dataFolder):
        dataFilePath = os.path.join(dataFolder, dataFileName)
        if os.path.isfile(dataFilePath):
                processData()

        else:
                print '%s not found' % dataFileName
                sys.exit(1)
else:
        print '%s not found' % dataFolder
        sys.exit(1)




# commented out, will use later			
#sorted_dict = sorted(wordDictionary.items(), key=operator.itemgetter(0))
#print sorted_dict
##               for word in line.split():
##                        
##                        if not wordDictionary.has_key(word):
##                                wordDictionary[word] = 1
##                        else:
##                                wordDictionary[word] += 1
##
##                print wordDictionary

