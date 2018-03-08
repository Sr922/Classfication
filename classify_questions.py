import html
import pprint
import re
# from html.parser import HTMLParser
import csv
from bs4 import BeautifulSoup
import sys

from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from sklearn.externals import joblib
from sklearn import decomposition
import psycopg2

reload(sys)
sys.setdefaultencoding('utf-8')


# class ReutersParser(HTMLParser):
#     """
#     ReutersParser subclasses HTMLParser and is used to open the SGML
#     files associated with the Reuters-21578 categorised test collection.

#     The parser is a generator and will yield a single document at a time.
#     Since the data will be chunked on parsing, it is necessary to keep 
#     some internal state of when tags have been "entered" and "exited".
#     Hence the in_body, in_topics and in_topic_d boolean members.
#     """
#     def __init__(self, encoding='latin-1'):
#         """
#         Initialise the superclass (HTMLParser) and reset the parser.
#         Sets the encoding of the SGML files by default to latin-1.
#         """
#         html.parser.HTMLParser.__init__(self)
    #     self._reset()
    #     self.encoding = encoding

    # def _reset(self):
    #     """
    #     This is called only on initialisation of the parser class
    #     and when a new topic-body tuple has been generated. It
    #     resets all off the state so that a new tuple can be subsequently
    #     generated.
    #     """
    #     self.in_body = False
    #     self.in_topics = False
    #     self.in_topic_d = False
    #     self.body = ""
    #     self.topics = []
    #     self.topic_d = ""

    # def parse(self, fd):
    #     """
    #     parse accepts a file descriptor and loads the data in chunks
    #     in order to minimise memory usage. It then yields new documents
    #     as they are parsed.
    #     """
    #     self.docs = []
    #     for chunk in fd:
    #         self.feed(chunk.decode(self.encoding))
    #         for doc in self.docs:
    #             yield doc
    #         self.docs = []
    #     self.close()

    # def handle_starttag(self, tag, attrs):
    #     """
    #     This method is used to determine what to do when the parser
    #     comes across a particular tag of type "tag". In this instance
    #     we simply set the internal state booleans to True if that particular
    #     tag has been found.
    #     """
    #     if tag == "reuters":
    #         pass
    #     elif tag == "body":
    #         self.in_body = True
    #     elif tag == "topics":
    #         self.in_topics = True
    #     elif tag == "d":
    #         self.in_topic_d = True 

    # def handle_endtag(self, tag):
    #     """
    #     This method is used to determine what to do when the parser
    #     finishes with a particular tag of type "tag". 

    #     If the tag is a  tag, then we remove all 
    #     white-space with a regular expression and then append the 
    #     topic-body tuple.

    #     If the tag is a  or  tag then we simply set
    #     the internal state to False for these booleans, respectively.

    #     If the tag is a  tag (found within a  tag), then we
    #     append the particular topic to the "topics" list and 
    #     finally reset it.
    #     """
    #     if tag == "reuters":
    #         self.body = re.sub(r'\s+', r' ', self.body)
    #         self.docs.append( (self.topics, self.body) )
    #         self._reset()
    #     elif tag == "body":
    #         self.in_body = False
    #     elif tag == "topics":
    #         self.in_topics = False
    #     elif tag == "d":
    #         self.in_topic_d = False
    #         self.topics.append(self.topic_d)
    #         self.topic_d = ""  

    # def handle_data(self, data):
    #     """
    #     The data is simply appended to the appropriate member state
    #     for that particular tag, up until the end closing tag appears.
    #     """
    #     if self.in_body:
    #         self.body += data
    #     elif self.in_topic_d:
    #         self.topic_d += data


def obtain_topic_tags():
    """
    Open the topic list file and import all of the topic names
    taking care to strip the trailing "\n" from each word.
    """
    topics = open(
        "data/all-topics-strings.lc.txt", "r"
    ).readlines()
    topics = [t.strip() for t in topics]
    return topics


def filter_doc_list_through_topics():
    """
    Reads all of the documents and creates a new list of two-tuples
    that contain a single feature entry and the body text, instead of
    a list of topics. It removes all geographic features and only 
    retains those documents which have at least one non-geographic
    topic.
    """

    # reader = csv.reader(open('./DataSet/updated_to_classify.csv', 'rU'), delimiter= ",")
    db = psycopg2.connect("host='localhost' dbname=stackoverflow user=postgres password='sindhu93'")
    cur = db.cursor()
    query = 'select id,title, body, difficulty_level from posts p2 where p2.tags Like \'%<java>%\' and p2.posttypeid=1 and p2.difficulty_level is not null'
    cur.execute(query)

    record = []
    for data in cur:
        record.append(data)
    
    ref_docs = []
    for data in record:
        body = BeautifulSoup(data[1]+ data[2]).get_text().encode('utf-8').strip()
        d_tup = (data[3], body)
        ref_docs.append(d_tup)
            
    # for d in docs:
    #     if d[0] == [] or d[0] == "":
    #         continue
    #     for t in d[0]:
    #         if t in topics:
    #             d_tup = (t, d[1])
    #             ref_docs.append(d_tup)
    #             break
    return ref_docs

def test_doc():
    db = psycopg2.connect("host='localhost' dbname=stackoverflow user=postgres password='sindhu93'")
    cur = db.cursor()
    query = 'select id,title, body, difficulty_level from posts p2 where p2.tags Like \'%<java>%\' and p2.posttypeid=1 and p2.difficulty_level is null LIMIT 10'
    cur.execute(query)

    record = []
    for data in cur:
        record.append(data)

    test_docs = []
    for data in record:
        body = BeautifulSoup(data[1]+ data[2]).get_text().encode('utf-8').strip()
        d_tup = (0, body)
        test_docs.append(d_tup)

    return test_docs

# for data in record:
#     body = data[1]+data[2]
#     content = BeautifulSoup(body).get_text()
#     if('spring' in content.lower() or 'hibernate' in content.lower() or 'thread' in content.lower() or 'multi-thread' in content.lower() or 'jboss' in content.lower() or 'swing' in content.lower()
#         or 'jdbc' in content.lower() or 'jframe' in content.lower() or 'jbutton' in content.lower()):
#         #print(body, ' is of level : Difficult')
#         training_data.append({"class": 'Difficult', "sentence":content})


def create_tfidf_training_data(docs):
    """
    Creates a document corpus list (by stripping out the
    class labels), then applies the TF-IDF transform to this
    list. 

    The function returns both the class label vector (y) and 
    the corpus token/feature matrix (X).
    """
    # Create the training data class labels
    y = [d[0] for d in docs]
    
    # Create the document corpus list
    corpus = [d[1] for d in docs]

    # Create the TF-IDF vectoriser and transform the corpus
    vectorizer = TfidfVectorizer(min_df=1)
    #print(corpus)
    X = vectorizer.fit_transform(corpus)
    return X, y

def train_svm(X, y):
    """
    Create and train the Support Vector Machine.
    """
    svm = SVC(C=1000000.0, gamma='auto', kernel='rbf')
    svm.fit(X, y)
    return svm


if __name__ == "__main__":
    # Create the list of Reuters data and create the parser
    # files = ["data/reut2-%03d.sgm" % r for r in range(0, 22)]
    # parser = ReutersParser()

    # Parse the document and force all generated docs into
    # a list so that it can be printed out to the console
    # docs = []
    # for fn in files:
    #     for d in parser.parse(open(fn, 'rb')):
    #         docs.append(d)

    # Obtain the topic tags and filter docs through it 
    # topics = obtain_topic_tags()
    ref_docs = filter_doc_list_through_topics()
    
    # Vectorise and TF-IDF transform the corpus 
    X, y = create_tfidf_training_data(ref_docs)

    # Create the training-test split of the data
    # X_train, X_test, y_train, y_test = train_test_split(
    #     X, y, test_size=0.2, random_state=42
    # )

    # Create and train the Support Vector Machine
    print(X)
    print(y)
    svm = train_svm(X, y)
    joblib.dump(svm, './my_model.pkl', compress=9)

    # Make an array of predictions on the test set
    # print("**************")
    # print(X_test)
    # pred = svm.predict(X_test)

    # # Output the hit-rate and the confusion matrix for each model
    # print(y_test)
    # print(svm.score(X_test, y_test))
    # print(confusion_matrix(pred, y_test))



################ Classifier ############
# import nltk
# from nltk.stem.lancaster import LancasterStemmer
# import os
# import csv
# import json
# import datetime
# from bs4 import BeautifulSoup
# import numpy as np
# import time
# import psycopg2
# from textblob import TextBlob

# # compute sigmoid nonlinearity
# def sigmoid(x):
#     output = 1/(1+np.exp(-x))
#     return output

# # convert output of sigmoid function to its derivative
# def sigmoid_output_to_derivative(output):
#     return output*(1-output)
 
# def clean_up_sentence(sentence):
#     # tokenize the pattern
#     sentence_words = nltk.word_tokenize(sentence)
#     # stem each word
#     sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
#     return sentence_words

# # return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
# def bow(sentence, words, show_details=False):
#     # tokenize the pattern
#     sentence_words = clean_up_sentence(sentence)
#     # bag of words
#     bag = [0]*len(words)  
#     for s in sentence_words:
#         for i,w in enumerate(words):
#             if w == s: 
#                 bag[i] = 1
#                 if show_details:
#                     print ("found in bag: %s" % w)

#     return(np.array(bag))

# def think(sentence, show_details=False):
#     x = bow(sentence.lower(), words, show_details)
#     if show_details:
#         print ("sentence:", sentence, "\n bow:", x)
#     # input layer is our bag of words
#     l0 = x
#     # matrix multiplication of input and hidden layer
#     l1 = sigmoid(np.dot(l0, synapse_0))
#     # output layer
#     l2 = sigmoid(np.dot(l1, synapse_1))
#     return l2

# def train(X, y, hidden_neurons=10, alpha=1, epochs=50000, dropout=False, dropout_percent=0.5):

#     print ("Training with %s neurons, alpha:%s, dropout:%s %s" % (hidden_neurons, str(alpha), dropout, dropout_percent if dropout else '') )
#     print ("Input matrix: %sx%s    Output matrix: %sx%s" % (len(X),len(X[0]),1, len(classes)) )
#     np.random.seed(1)

#     last_mean_error = 1
#     # randomly initialize our weights with mean 0
#     synapse_0 = 2*np.random.random((len(X[0]), hidden_neurons)) - 1
#     synapse_1 = 2*np.random.random((hidden_neurons, len(classes))) - 1

#     prev_synapse_0_weight_update = np.zeros_like(synapse_0)
#     prev_synapse_1_weight_update = np.zeros_like(synapse_1)

#     synapse_0_direction_count = np.zeros_like(synapse_0)
#     synapse_1_direction_count = np.zeros_like(synapse_1)
        
#     for j in iter(range(epochs+1)):

#         # Feed forward through layers 0, 1, and 2
#         layer_0 = X
#         layer_1 = sigmoid(np.dot(layer_0, synapse_0))
                
#         if(dropout):
#             layer_1 *= np.random.binomial([np.ones((len(X),hidden_neurons))],1-dropout_percent)[0] * (1.0/(1-dropout_percent))

#         layer_2 = sigmoid(np.dot(layer_1, synapse_1))

#         # how much did we miss the target value?
#         layer_2_error = y - layer_2

#         if (j% 10000) == 0 and j > 5000:
#             # if this 10k iteration's error is greater than the last iteration, break out
#             if np.mean(np.abs(layer_2_error)) < last_mean_error:
#                 print ("delta after "+str(j)+" iterations:" + str(np.mean(np.abs(layer_2_error))) )
#                 last_mean_error = np.mean(np.abs(layer_2_error))
#             else:
#                 print ("break:", np.mean(np.abs(layer_2_error)), ">", last_mean_error )
#                 break
                
#         # in what direction is the target value?
#         # were we really sure? if so, don't change too much.
#         layer_2_delta = layer_2_error * sigmoid_output_to_derivative(layer_2)

#         # how much did each l1 value contribute to the l2 error (according to the weights)?
#         layer_1_error = layer_2_delta.dot(synapse_1.T)

#         # in what direction is the target l1?
#         # were we really sure? if so, don't change too much.
#         layer_1_delta = layer_1_error * sigmoid_output_to_derivative(layer_1)
        
#         synapse_1_weight_update = (layer_1.T.dot(layer_2_delta))
#         synapse_0_weight_update = (layer_0.T.dot(layer_1_delta))
        
#         if(j > 0):
#             synapse_0_direction_count += np.abs(((synapse_0_weight_update > 0)+0) - ((prev_synapse_0_weight_update > 0) + 0))
#             synapse_1_direction_count += np.abs(((synapse_1_weight_update > 0)+0) - ((prev_synapse_1_weight_update > 0) + 0))        
        
#         synapse_1 += alpha * synapse_1_weight_update
#         synapse_0 += alpha * synapse_0_weight_update
        
#         prev_synapse_0_weight_update = synapse_0_weight_update
#         prev_synapse_1_weight_update = synapse_1_weight_update

#     now = datetime.datetime.now()

#     # persist synapses
#     synapse = {'synapse0': synapse_0.tolist(), 'synapse1': synapse_1.tolist(),
#                'datetime': now.strftime("%Y-%m-%d %H:%M"),
#                'words': words,
#                'classes': classes
#               }
#     synapse_file = "./synapses.json"

#     with open(synapse_file, 'w') as outfile:
#         json.dump(synapse, outfile, indent=4, sort_keys=True)
#     print ("saved synapses to:", synapse_file)


# def classify(sentence, show_details=False):
#     results = think(sentence, show_details)

#     results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD ] 
#     results.sort(key=lambda x: x[1], reverse=True) 
#     return_results =[[classes[r[0]],r[1]] for r in results]
#     print ("%s \n classification: %s" % (sentence, return_results))
#     return return_results


# stemmer = LancasterStemmer()

# #Creating Training Data
# # questionsReader = csv.reader(open('./DataSet/updated_to_classify.csv', 'rU'), delimiter= ",")
# training_data = []

# # for line in questionsReader:
# #     if line[3] != 'Question Difficulty Level':
# # 		# print line[4]
# # 		body = line[1] + line[2]
# # 		training_data.append({"class": line[3], "sentence":BeautifulSoup(body).get_text()})

# db = psycopg2.connect("host='localhost' dbname=stackoverflow user=postgres password='sindhu93'")
# cur = db.cursor()
# query = 'select id,title, body, difficulty_level from posts p2 where p2.tags Like \'%<java>%\' and p2.posttypeid=1 and p2.difficulty_level is not null'
# cur.execute(query)

# record = []
# for data in cur:
#     record.append(data)

# for data in record:
#     body = data[1]+data[2]
#     content = BeautifulSoup(body).get_text()
#     training_data.append({"class": data[3], "sentence":content})

# # for data in record:
# # 	body = data[1]+data[2]
# # 	content = BeautifulSoup(body).get_text()
# # 	if('spring' in content.lower() or 'hibernate' in content.lower() or 'thread' in content.lower() or 'multi-thread' in content.lower() or 'jboss' in content.lower() or 'swing' in content.lower()
# # 		or 'jdbc' in content.lower() or 'jframe' in content.lower() or 'jbutton' in content.lower()):
# # 		#print(body, ' is of level : Difficult')
# # 		training_data.append({"class": 'Difficult', "sentence":content})

# print ("%s sentences in training data" % len(training_data))

# words = []
# classes = []
# documents = []
# ignore_words = ['?']
# # loop through each sentence in our training data
# for pattern in training_data:
#     # tokenize each word in the sentence
#     w = nltk.word_tokenize(pattern['sentence'])
#     # add to our words list
#     words.extend(w)
#     # add to documents in our corpus
#     documents.append((w, pattern['class']))
#     # add to our classes list
#     if pattern['class'] not in classes:
#         classes.append(pattern['class'])

# # stem and lower each word and remove duplicates
# words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
# words = list(set(words))

# # remove duplicates
# classes = list(set(classes))

# print (len(documents), "documents")
# print (len(classes), "classes", classes)
# print (len(words), "unique stemmed words")

# #create our training data
# training = []
# output = []
# # create an empty array for our output
# output_empty = [0] * len(classes)

# # training set, bag of words for each sentence
# for doc in documents:
#     # initialize our bag of words
#     bag = []
#     # list of tokenized words for the pattern
#     pattern_words = doc[0]
#     # stem each word
#     pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
#     # create our bag of words array
#     for w in words:
#         bag.append(1) if w in pattern_words else bag.append(0)

#     training.append(bag)
#     # output is a '0' for each tag and '1' for current tag
#     output_row = list(output_empty)
#     output_row[classes.index(doc[1])] = 1
#     output.append(output_row)

# print ("# words", len(words))
# print ("# classes", len(classes))

# # sample training/output
# # i = 0
# # w = documents[i][0]
# # print ([stemmer.stem(word.lower()) for word in w])
# # print (training[i])
# # print (output[i])


# X = np.array(training)
# y = np.array(output)

# start_time = time.time()

# train(X, y, hidden_neurons=20, alpha=0.1, epochs=100000, dropout=False, dropout_percent=0.2)

# elapsed_time = time.time() - start_time
# print ("processing time:", elapsed_time, "seconds")

# # probability threshold
# ERROR_THRESHOLD = 0.2
# # load our calculated synapse values
# synapse_file = 'synapses.json' 
# with open(synapse_file) as data_file: 
#     synapse = json.load(data_file) 
#     synapse_0 = np.asarray(synapse['synapse0']) 
#     synapse_1 = np.asarray(synapse['synapse1'])


# #classify(str(content), show_details=False)
# classify("what is spring in java")
# # classify("how are you today?")
# # classify("talk to you tomorrow")
# # classify("who are you?")
# # classify("make me some lunch")
# # print ()
# # classify("how was your lunch?", show_details=True)


