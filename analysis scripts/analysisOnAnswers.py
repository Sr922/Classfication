import csv
from bs4 import BeautifulSoup
from textblob import TextBlob
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import datetime, date, time, timedelta
import psycopg2

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
query = 'select id,title, body, difficulty_level from posts p2 where p2.tags Like \'%<java>%\' and p2.posttypeid=1 and p2.difficulty_level is not null'
cur.execute(query)

questions = []
parrent_ids = []
for line in cur:
	#print line;
	#body = line[1] + line[2]
	questions.append({'id' : line[0], 'difficulty_level' : line[3]})

print(len(questions))

for question in questions:
	parrent_ids.append(question['id'])



#answersReader = csv.reader(open('./DataSet/Answers-ForBasicStudy.csv', 'rU'), delimiter= ",")
query = 'SELECT p.id, p.title, p.body, p.parentid, p.owneruserid, p.creationdate from posts p where p.parentid in ('+ ', '.join(str(v) for v in parrent_ids) +')'
# print query
cur.execute(query)

answers = []
for line in cur:
	#print line;
	body = line[2]
	answers.append({'id' : line[0], 'body' : BeautifulSoup(body).get_text(), 'parent_id' : line[3], 'owner_id' : line[4], 'created_date' : line[5]})

output = []
for question in questions:
	required_answers = getAnswersForThisQuestion(question['id'], answers)
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
		output.append([question['id'], question['difficulty_level'], answer['id'], len(content.words), sentiment[0], sentiment[1], answer['owner_id'], experienceLevel])


with open('./DataSet/analysis.csv', 'w') as csvfile:
    output_writer = csv.writer(csvfile, delimiter=',',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    output_writer.writerow(['question_id', 'question_type', 'answer_id', 'no_of_words', 'polarity', 'subjectivity', 'answered_by', 'his_experience_level'])
    for data in output:
    	output_writer.writerow(data)
