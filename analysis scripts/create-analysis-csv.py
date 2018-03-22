# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import csv
from bs4 import BeautifulSoup
from textblob import TextBlob
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import datetime, date, time, timedelta
import psycopg2

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

def getAnswersForThisQuestion(question_id, answers):
	required_answers = []
	for answer in answers:
		if(answer['parent_id'] == question_id):
			required_answers.append(answer)

	return required_answers

questions_reader = csv.reader(open('./DataSet/Mar-21/allJavaQuestions.csv', 'rU'), delimiter= ",")

questions = []
for line in questions_reader:
	questions.append({'id' : line[0], 'difficulty_level' : line[1]})

answers_reader = csv.reader(open('./DataSet/Mar-21/allJavaAnswers.csv', 'rU'), delimiter= ",")

answers = []
for line in answers_reader:
	answers.append({'id' : line[0], 'body' : line[1], 'parent_id' : line[2], 'owner_id' : line[3], 'created_date' : line[4]})

output = []
print('Starting to write in a file...')
with open('./DataSet/Mar-21/analysis.csv', 'w') as csvfile:
	output_writer = csv.writer(csvfile, delimiter=',',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
	output_writer.writerow(['question_id', 'question_type', 'answer_id', 'no_of_words', 'polarity', 'subjectivity', 'answered_by', 'his_experience_level'])

	i=0
	for question in questions:
		required_answers = getAnswersForThisQuestion(question['id'], answers)
		j=0
		for answer in required_answers:
			content = TextBlob(answer['body'])
			sentiment = content.sentiment_assessments
			# print len(content.words)
			# print content.sentiment
			# print content.sentiment_assessments
			if(answer['owner_id'] != None and answer['owner_id'] != ''):
				query = 'SELECT * FROM users WHERE id ='+str(answer['owner_id'])
				cur.execute(query)
				dev = []
				for data in cur:
					dev.append(data)
				developer_join_date = dev[0][2]
				difference = relativedelta(answer['created_date'], developer_join_date)
				experienceLevel = getExperienceLevel(difference)
			else:
				experienceLevel = ''
			# print(question['id'],' ', answer['id'],' ',answer['owner_id'])
			output.append([question['id'], question['difficulty_level'], answer['id'], len(content.words), sentiment[0], sentiment[1], answer['owner_id'], experienceLevel])
			output_writer.writerow([question['id'], question['difficulty_level'], answer['id'], len(content.words), sentiment[0], sentiment[1], answer['owner_id'], experienceLevel])
			# printProgressBar(j, len(required_answers), prefix = 'Progress:', suffix = 'Complete', length = 50)
			# j=i+1
		
		printProgressBar(i, len(questions), prefix = 'Progress:', suffix = 'Complete', length = 50)
		i=i+1

