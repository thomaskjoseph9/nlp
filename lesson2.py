from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#stop word filteration
example_text="hello Mr. Thomas,how are you doing.We are very pleased to see you. The service was bad but the food was good."
stop_words=set(stopwords.words("english"))

words=word_tokenize(example_text)
filter_sentence=[]

for word in words:
    if(word not in stop_words):
        filter_sentence.append(word)


print(filter_sentence)