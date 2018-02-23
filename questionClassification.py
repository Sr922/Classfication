import nltk
import sys
import csv
#nltk.download()
from bs4 import BeautifulSoup
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from featx import bag_of_words
nltk.download('stopwords')


csv.field_size_limit(sys.maxsize)
reader = csv.reader(open('/Volumes/SINDHU/Thesis/Empirical Study/DataSet/OnlyTitles&Questions.csv', 'rU'), delimiter= ",")
tokenizer = WordPunctTokenizer()

english_stops = set(stopwords.words('english'))
stemmer = PorterStemmer()

for line in reader:
    #tokens = word_tokenize(field)
    #tokenizer.tokenize(para)
    #words = tokenizer.tokenize(para)
    #removed_stop_words =[word for word in words if word not in english_stops]
  #   for word in removed_stop_words:
		# print(stemmer.stem(word));
    #print(line[2])
    body = line[2] + line[1]
    question = BeautifulSoup(line[1]).get_text()

    #body = str(line[2]) + str(question)
    #print(BeautifulSoup(body))
    #question = BeautifulSoup(line[1]).get_text() + line[2]
    #print question
    words = tokenizer.tokenize(question)
    without_stopwords = [word for word in words if word not in english_stops]
    for word in without_stopwords:
        #print(stemmer.stem(word));
        word = stemmer.stem(word)

    #print without_stopwords
    bow = dict([(word, True) for word in without_stopwords])
    #bow= bag_of_non_stopwords(['the', 'quick', 'brown', 'fox'])
    print bow
    #question = 