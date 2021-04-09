from sklearn.model_selection import train_test_split  
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from nltk.corpus import stopwords  
from sklearn.datasets import load_files
from nltk.stem import WordNetLemmatizer
import re
documents = []
document = []
movie_data = load_files(r"F:\Python Tution\Machine Learning\Day7\txt_sentoken")  
X, y = movie_data.data, movie_data.target

stemmer = WordNetLemmatizer()

for sen in range(0, len(X)):  
    # Remove all the special characters
    document = re.sub(r'\W', ' ', str(X[sen]))

    # remove all single characters
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)

    # Remove single characters from the start
    document = re.sub(r'\^[a-zA-Z]\s+', ' ', document) 

    # Substituting multiple spaces with single space
    document = re.sub(r'\s+', ' ', document, flags=re.I)

    # Removing prefixed 'b'
    document = re.sub(r'^b\s+', '', document)

    # Converting to Lowercase
    document = document.lower()

    # Lemmatization
    document = document.split()

    document = [stemmer.lemmatize(word) for word in document]
    document = ' '.join(document)

    documents.append(document)

#vectorizer = CountVectorizer(max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))  
#X = vectorizer.fit_transform(documents).toarray()
tfidfconverter = TfidfVectorizer(max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))  
X = tfidfconverter.fit_transform(documents).toarray()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
print("------X_Train-------")
print(X_train)
print("------X_Test--------")
print(X_test)
print("------Y_Train--------")
print(y_train)
print("------Y_Test---------")
print(y_test)
classifier = RandomForestClassifier(n_estimators=1000, random_state=0)  
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print("------Y_pred------")
print(y_pred)
