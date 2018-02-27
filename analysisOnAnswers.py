import csv
from bs4 import BeautifulSoup
from textblob import TextBlob

def getAnswersForThisQuestion(question_id, answers):
	required_answers = []
	for answer in answers:
		if(answer['parent_id'] == question_id):
			required_answers.append(answer)

	return required_answers



questionsReader = csv.reader(open('./DataSet/ForBasicStudy.csv', 'rU'), delimiter= ",")

questions = []
for line in questionsReader:
	#print line;
	body = line[1] + line[2]
	questions.append({'id' : line[0], 'body' : BeautifulSoup(body).get_text(), 'difficulty_level' : line[4]})

answersReader = csv.reader(open('./DataSet/Answers-ForBasicStudy.csv', 'rU'), delimiter= ",")

answers = []
for line in answersReader:
	#print line;
	body = line[4]
	answers.append({'id' : line[0], 'body' : BeautifulSoup(body).get_text(), 'parent_id' : line[5], 'owner_id' : line[2]})

output = []
for question in questions:
	required_answers = getAnswersForThisQuestion(question['id'], answers)
	for answer in required_answers:
		content = TextBlob(answer['body'])
		sentiment = content.sentiment_assessments
		# print len(content.words)
		# print content.sentiment
		# print content.sentiment_assessments
		output.append([question['id'], question['difficulty_level'], answer['id'], len(content.words), sentiment[0], sentiment[1], answer['owner_id'], ''])


with open('./DataSet/analysis.csv', 'w') as csvfile:
    output_writer = csv.writer(csvfile, delimiter=',',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    output_writer.writerow(['question_id', 'question_type', 'answer_id', 'no_of_words', 'polarity', 'subjectivity', 'answered_by', 'his_experience_level'])
    for data in output:
    	output_writer.writerow(data)