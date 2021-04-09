from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
ps = PorterStemmer()
lem = WordNetLemmatizer()
stem = PorterStemmer()
word = "flying"
'''
text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't he eat ancdesf connected cardboard"""
tokenized_word = word_tokenize(text)
print(tokenized_word)
filtered_sent=[]
stop_words=set(stopwords.words("english"))
for w in tokenized_word:
    if w not in stop_words:
        filtered_sent.append(w)

stemmed_words = []
for w in filtered_sent:
    stemmed_words.append(ps.stem(w))
'''
print("Lemmatized Word:",lem.lemmatize(word,"v"))
print("Stemmed Word:",stem.stem(word))
#print("Tokenized Sentence:",tokenized_word)
#print("Filterd Sentence:",filtered_sent)
#print("Stemmed Sentences:",stemmed_words)
