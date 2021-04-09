from nltk.corpus import stopwords
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't he eat ancdesf cardboard"""
tokenized_word = word_tokenize(text)
print(tokenized_word)
filtered_sent=[]
stop_words=set(stopwords.words("english"))
for w in tokenized_word:
    if w not in stop_words:
        filtered_sent.append(w)
print("Tokenized Sentence:",tokenized_word)
print("Filterd Sentence:",filtered_sent)
