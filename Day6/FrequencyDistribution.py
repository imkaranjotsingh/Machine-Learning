from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard"""
tokenized_word = word_tokenize(text)
fdist = FreqDist(tokenized_word)
print(fdist)
print(fdist.most_common(2))
