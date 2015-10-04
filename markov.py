import sylco
import markovlib
import re
from string import punctuation

def num_of_words(words):
        r = re.compile(r'[{}]'.format(punctuation))
        new_words_cont = r.sub(' ',words)
        wordlen = len(new_words_cont.split())
        return wordlen

def splitParagraphIntoSentences(paragraph):
    ''' break a paragraph into sentences
        and return a list '''
    import re
    # to split by multile characters

    #   regular expressions are easiest (and fastest)
    sentenceEnders = re.compile('[.!?,]')
    sentenceList = sentenceEnders.split(paragraph)
    return sentenceList


#print nsyl('multiplication')

file_ = open('text/combined.txt')
while True:
        markov = markovlib.Markov(file_)
        text = markov.generate_markov_text()
        strlen = 0
        sentences = splitParagraphIntoSentences(text)
        for s in sentences:
                senlen = sylco.sylco(s)
                #num_words = num_of_words(s)
                if(senlen <8):
                        print s.strip().capitalize()
                else:
                        print "          [" + s.strip().capitalize() + "]"
                
        print ''
        print ''
        print 'Press anything to continue:'
        response = raw_input()
        print ''
        print ''
