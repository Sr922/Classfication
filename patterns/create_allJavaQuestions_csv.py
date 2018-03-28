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

def getExperienceLevel(difference):
	if difference.years >= 0 and difference.years < 2:
		return 'Novice'
	elif difference.years >= 2 and difference.years < 5:
		return 'Beginner'
	elif difference.years >= 5 and difference.years < 7:
		return 'Intermediate'
	elif difference.years >= 7:
		return 'Experienced'
	else:
		return difference.years


#questionsReader = csv.reader(open('./DataSet/ForBasicStudy.csv', 'rU'), delimiter= ",")
db = psycopg2.connect("host='localhost' dbname=stackoverflow user=postgres password='sindhu93'")
cur = db.cursor()
# query = 'select id,title, body, difficulty_level from posts p2 where p2.tags Like \'%<java>%\' and p2.posttypeid=1 and p2.difficulty_level IN (\'Easy\', \'Medium\', \'Difficult\')'
# cur.execute(query)

# questions = []
# parrent_ids = []
# for line in cur:
# 	#print line;
# 	#body = line[1] + line[2]
# 	body = line[2]
# 	questions.append({'id' : line[0], 'body': BeautifulSoup(body).get_text(), 'difficulty_level' : line[3]})
questions_reader = csv.reader(open('./DataSet/Mar-21/allJavaQuestions.csv', 'rU'), delimiter= ",")

questions = []
question_ids = []
for line in questions_reader:
	if(line[0] != 'question_id'):
		questions.append({'id' : line[0], 'difficulty_level' : line[1]})

i=0
required_data = []
for question in questions:
	query = 'select body from posts where id = '+question['id']+''
	cur.execute(query)
	body = cur.fetchone()[0]
	required_data.append({'id' : question['id'], 'body': BeautifulSoup(body).get_text(), 'difficulty_level' : question['difficulty_level']})
	printProgressBar(i, len(questions), prefix = 'Progress:', suffix = 'Complete', length = 50)
	i=i+1
	

with open('./DataSet/Mar-27/allJavaQuestions.csv', 'w') as csvfile:
	output_writer = csv.writer(csvfile, delimiter=',')
	output_writer.writerow(['question_id', 'body','difficulty_level'])

	i=0
	for question in required_answers:
		output_writer.writerow([question['id'], question['body'].encode('ascii', 'ignore').decode('ascii'), question['difficulty_level']])
		printProgressBar(i, len(questions), prefix = 'Progress:', suffix = 'Complete', length = 50)
		i=i+1



