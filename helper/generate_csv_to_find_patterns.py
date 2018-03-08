# -*- coding: utf-8 -*-
from __future__ import print_function
import urllib2
import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import datetime, date, time, timedelta
from bs4 import BeautifulSoup
from textblob import TextBlob
from connection import Postgres
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

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


ps = Postgres()
print('Loading Java Questions')
answersDetails = ps.getAnswers('java')
print('Loaded')

output = []
i=0
for answer in answersDetails:
	content = TextBlob(BeautifulSoup(answer[7]).get_text())
	sentiment = content.sentiment_assessments
	# print len(content.words)
	# print content.sentiment
	# print content.sentiment_assessments
	if(answer[8] != None):
		dev = ps.read(answer[8])
		#print(dev)
		if dev != None:
			developer_join_date = dev[0][2]
			difference = relativedelta(answer[4], developer_join_date)
			experience_level = getExperienceLevel(difference)
		else:
			experience_level = 'No join date available'
		output.append([answer[3], '' , answer[0], len(content.words), sentiment[0], sentiment[1], answer[8], experience_level])
		printProgressBar(i, len(answersDetails), prefix = 'Progress:', suffix = 'Complete', length = 50)
		i=i+1;

with open('./DataSet/analysis.csv', 'w') as csvfile:
    output_writer = csv.writer(csvfile, delimiter=',',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    output_writer.writerow(['question_id', 'question_type', 'answer_id', 'no_of_words', 'polarity', 'subjectivity', 'answered_by', 'his_experience_level'])
    i=0
    for data in output:
    	output_writer.writerow(data)
    	printProgressBar(i, len(output), prefix = 'Progress:', suffix = 'Complete', length = 50)
    	i=i+1;

