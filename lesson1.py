from nltk.tokenize import sent_tokenize,word_tokenize

#nltk.download()

#tokenizing - two types grouping by words and groups by sentences
#lexicon - word and what it means
#corpora - body of text .. 

#investor-speak.... regular english-speak

#investor speak 'bull' = positive in market
#english-speak 'bull' = animal

example_text="hello Mr. Thomas,how are you doing.We are very pleased to see you. The service was bad but the food was good."


print(sent_tokenize(example_text))
#print(word_tokenize(example_text))

for word in word_tokenize(example_text):
    print(word)