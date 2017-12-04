from nltk.stem import PorterStemmer

from nltk.tokenize import word_tokenize

#stemming
#getting the root word for eg stemming of riding is ride
#eg I was taking a ride in car 
#I was riding in the car
#above both sentences mean the same

ps=PorterStemmer()

print('words example')
example_words=["python","pythoner","pythoning","pythoned"]
for word in example_words:
    print(ps.stem(word))

print('sentence example')
example_sentence="Hi thomas was riding a car. He was taking a ride in the car. Riding a car is his hobby"
words=word_tokenize(example_sentence)
for word in words:
    print(ps.stem(word))