import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
from nltk.stem.snowball import SnowballStemmer
import csv
from bs4 import BeautifulSoup
import psycopg2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
nltk.download('punkt')
#import mpld3

def tokenize_and_stem(text):
	# first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
	tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
	filtered_tokens = []
	# filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
	for token in tokens:
		if re.search('[a-zA-Z]', token):
			filtered_tokens.append(token)
	stems = [stemmer.stem(t) for t in filtered_tokens]
	return stems

def tokenize_only(text):
	# first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
	tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
	filtered_tokens = []
	# filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
	for token in tokens:
		if re.search('[a-zA-Z]', token):
			filtered_tokens.append(token)
	return filtered_tokens

#reader = csv.reader(open('/Volumes/SINDHU/Thesis/Empirical Study/DataSet/OnlyTitles&Questions.csv', 'rU'), delimiter= ",")
db = psycopg2.connect("host='localhost' dbname=stackoverflow user=postgres password='sindhu93'")
cur = db.cursor()
query = 'select id,title, body from posts p2 where p2.tags Like \'%<java>%\' and p2.posttypeid=1 LIMIT 2000'
cur.execute(query)

record = []
ids = []
titles = []
questions = []

for line in cur:
	#record.append(data)
	body = line[1] + line[2]
	ids.append(line[0])
	titles.append(line[1])
	question = BeautifulSoup(body).get_text()
	question = question.encode('utf-8', 'ignore')
	questions.append(question)


# for line in reader:
#     body = line[2] + line[1]
#     ids.append(line[0])
#     titles.append(line[2])
#     question = BeautifulSoup(line[1]).get_text()
#     questions.append(question)

print(len(questions))

ranks = []

for i in range(0,len(questions)-1):
	ranks.append(i)

stopwords = nltk.corpus.stopwords.words('english')
stemmer = SnowballStemmer("english")

totalvocab_stemmed = []
totalvocab_tokenized = []
for i in questions:
	allwords_stemmed = tokenize_and_stem(i.encode('utf-8').strip())
	totalvocab_stemmed.extend(allwords_stemmed)
    
	allwords_tokenized = tokenize_only(i)
	totalvocab_tokenized.extend(allwords_tokenized)

vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
print 'there are ' + str(vocab_frame.shape[0]) + ' items in vocab_frame'
print vocab_frame.head()
print
print
print
print


tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000,
                             	min_df=0.2, stop_words='english',
                             	use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1,3))

tfidf_matrix = tfidf_vectorizer.fit_transform(questions)

print(tfidf_matrix.shape)

terms = tfidf_vectorizer.get_feature_names()

#print terms


num_clusters = 3

km = KMeans(n_clusters=num_clusters)

km.fit(tfidf_matrix)

clusters = km.labels_.tolist()

# km = joblib.load('doc_cluster.pkl')
# clusters = km.labels_.tolist()

print clusters

posts = { 'title': titles, 'ids': ids, 'questions': questions, 'cluster': clusters}

frame = pd.DataFrame(posts, index = [clusters] , columns = ['id', 'title', 'cluster'])

frame['cluster'].value_counts()

print("Top terms per cluster:")
print()
order_centroids = km.cluster_centers_.argsort()[:, ::-1]
for i in range(num_clusters):
    print("Cluster %d words:" % i, )
    for ind in order_centroids[i, :6]:
        print(' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'), )
    print()
    print()
    print("Cluster %d titles:" % i )
    print(len(frame.ix[i]['title']))
    # for title in frame.ix[i]['title'].values.tolist():
    #     print(' %s,' % title)
    print()
    print()
