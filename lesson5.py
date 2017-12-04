import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

#chunking
#group words into hopefully meaningful chunks
train_text=state_union.raw("2005-GWBush.txt")
sample_text=state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer=PunktSentenceTokenizer(train_text)

tokenized=custom_sent_tokenizer.tokenize(sample_text)


def process_content():
    try:
        for sentence in tokenized:
            #for each custom tokenized sentence we tokenize words
            words=nltk.word_tokenize(sentence)
            #now tagg each word 
            tagged=nltk.pos_tag(words)
            
            #create a chunk regular expression
            chunkGram=r"""Chunk:{<RB.?>*<VB.?>*<NNP><NN>?}"""

            # <RB.?>* = "0 or more of any tense of adverb," followed by:

            # <VB.?>* = "0 or more of any tense of verb," followed by:

            # <NNP>+ = "One or more proper nouns," followed by

            # <NN>? = "zero or one singular noun."
            

            chunkParser=nltk.RegexpParser(chunkGram)
            chunked=chunkParser.parse(tagged)

            #print(chunked)
            chunked.draw()


    except Exception as e:
        print(str(e))


process_content()        

#labeling the word with the type


# POS tag list:

# CC	coordinating conjunction
# CD	cardinal digit
# DT	determiner
# EX	existential there (like: "there is" ... think of it like "there exists")
# FW	foreign word
# IN	preposition/subordinating conjunction
# JJ	adjective	'big'
# JJR	adjective, comparative	'bigger'
# JJS	adjective, superlative	'biggest'
# LS	list marker	1)
# MD	modal	could, will
# NN	noun, singular 'desk'
# NNS	noun plural	'desks'
# NNP	proper noun, singular	'Harrison'
# NNPS	proper noun, plural	'Americans'
# PDT	predeterminer	'all the kids'
# POS	possessive ending	parent's
# PRP	personal pronoun	I, he, she
# PRP$	possessive pronoun	my, his, hers
# RB	adverb	very, silently,
# RBR	adverb, comparative	better
# RBS	adverb, superlative	best
# RP	particle	give up
# TO	to	go 'to' the store.
# UH	interjection	errrrrrrrm
# VB	verb, base form	take
# VBD	verb, past tense	took
# VBG	verb, gerund/present participle	taking
# VBN	verb, past participle	taken
# VBP	verb, sing. present, non-3d	take
# VBZ	verb, 3rd person sing. present	takes
# WDT	wh-determiner	which
# WP	wh-pronoun	who, what
# WP$	possessive wh-pronoun	whose
# WRB	wh-abverb	where, when