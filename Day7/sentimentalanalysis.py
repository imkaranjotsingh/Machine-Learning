import numpy as np
import re
import nltk
from sklearn.datasets import load_files
import pickle  
from nltk.corpus import stopwords
movie_data = load_files("F:\Python Tution\Machine Learning\Day7\txt_sentoken")  
X, y = movie_data.data, movie_data.target
print(X)
print(y)
