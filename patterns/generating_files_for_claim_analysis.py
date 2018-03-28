import csv
import statistics as statistics
from scipy.stats import mannwhitneyu
import numpy as np
from stats import Stats

analysis_reader = csv.reader(open('./DataSet/Mar-23/analysis.csv', 'rU'), delimiter= ",")

rows = []
for line in analysis_reader:
	if(len(line) >= 7):
		rows.append({'question_type' : line[1], 'wordCount' : line[3], 'polarity': line[4],'subjectivity' : line[5], 'score': line[6], 'viewscount': line[7], 'commentscount': line[8], 'favoritecount': line[9], 'developer' : line[10], 'developer experience' :line[11], 'question_id' : line[0]})

developers = {}

print(len(rows))
totalAnswers = len(rows)

# Segrating questions of each developer in their space
for row in rows:
	if(row['developer'] in developers):
		developers[row['developer']]['answers'].append(row)
	else:
		developers[row['developer']] = {}
		developers[row['developer']]['answers'] = []
		developers[row['developer']]['answers'].append(row)

print(len(developers))
# afterSegregating = 0
# for developer in developers:
# 	# print(len(developers[developer]['answers']))
# 	afterSegregating = afterSegregating + len(developers[developer]['answers'])
# print(afterSegregating)

from_developers = {}
developer_primary_claim_data = []
patterns_helper_data = []
for developer in developers:
	
	novice_answers = novice_easy_answer = novice_medium_answer = novice_difficult_answer = 0
	beginner_answers = beginner_easy_answer = beginner_medium_answer = beginner_difficult_answer = 0
	intermediate_answers = intermediate_easy_answer = intermediate_medium_answer = intermediate_difficult_answer = 0
	experienced_answers = experienced_easy_answer = experienced_medium_answer = experienced_difficult_answer = 0


	for answer in developers[developer]['answers']:
		if(answer['question_type'].lower() == 'easy'):
			if(answer['developer experience'].lower() == 'novice'):
				novice_easy_answer = novice_easy_answer + 1
			if(answer['developer experience'].lower() == 'beginner'):
				beginner_easy_answer = beginner_easy_answer + 1
			if(answer['developer experience'].lower() == 'intermediate'):
				intermediate_easy_answer = intermediate_easy_answer + 1
			if(answer['developer experience'].lower() == 'experienced'):
				experienced_easy_answer = experienced_easy_answer + 1

		if(answer['question_type'].lower() == 'medium'):
			if(answer['developer experience'].lower() == 'novice'):
				novice_medium_answer = novice_medium_answer + 1
			if(answer['developer experience'].lower() == 'beginner'):
				beginner_medium_answer = beginner_medium_answer + 1
			if(answer['developer experience'].lower() == 'intermediate'):
				intermediate_medium_answer = intermediate_medium_answer + 1
			if(answer['developer experience'].lower() == 'experienced'):
				experienced_medium_answer = experienced_medium_answer + 1
			

		if(answer['question_type'].lower() == 'difficult'):
			if(answer['developer experience'].lower() == 'novice'):
				novice_difficult_answer = novice_difficult_answer + 1
			if(answer['developer experience'].lower() == 'beginner'):
				beginner_difficult_answer = beginner_difficult_answer + 1
			if(answer['developer experience'].lower() == 'intermediate'):
				intermediate_difficult_answer = intermediate_difficult_answer + 1
			if(answer['developer experience'].lower() == 'experienced'):
				experienced_difficult_answer = experienced_difficult_answer + 1

	novice_answers = novice_easy_answer + novice_medium_answer + novice_difficult_answer
	beginner_answers = beginner_easy_answer + beginner_medium_answer + beginner_difficult_answer
	intermediate_answers = intermediate_easy_answer + intermediate_medium_answer + intermediate_difficult_answer
	experienced_answers = experienced_easy_answer + experienced_medium_answer + experienced_difficult_answer

	developer_primary_claim_data.append([developer,novice_answers, beginner_answers, intermediate_answers, experienced_answers])
	patterns_helper_data.append([developer,novice_easy_answer, novice_medium_answer, novice_difficult_answer, beginner_easy_answer, beginner_medium_answer, beginner_difficult_answer, intermediate_easy_answer, intermediate_medium_answer,
									intermediate_difficult_answer, experienced_easy_answer, experienced_medium_answer, experienced_difficult_answer])

	# developers[developer]['novice_answers_count'] = novice_answers
	# developers[developer]['beginner_answers_count'] = beginner_answers
	# developers[developer]['intermediate_answers_count'] = intermediate_answers
	# developers[developer]['experienced_answers_count'] = experienced_answers


	# developers[developer]['novice_easy_answer_count'] = novice_easy_answer
	# developers[developer]['novice_medium_answer_count'] = novice_medium_answer
	# developers[developer]['novice_difficult_answer_count'] = novice_difficult_answer
	
	# developers[developer]['beginner_easy_answer_count'] = beginner_easy_answer
	# developers[developer]['beginner_medium_answer_count'] = beginner_medium_answer
	# developers[developer]['beginner_difficult_answer_count'] = beginner_difficult_answer
	
	# developers[developer]['intermediate_easy_answer_count'] = intermediate_easy_answer
	# developers[developer]['intermediate_medium_answer_count'] = intermediate_medium_answer
	# developers[developer]['intermediate_difficult_answer_count'] = intermediate_difficult_answer
	
	# developers[developer]['experienced_easy_answer_count'] = experienced_easy_answer
	# developers[developer]['experienced_medium_answer_count'] = experienced_medium_answer
	# developers[developer]['experienced_difficult_answer_count'] = experienced_difficult_answer


with open('./DataSet/Mar-23/developer_primary_claim_data.csv', 'w') as csvfile:
	output_writer = csv.writer(csvfile, delimiter=',',
	                        quotechar=' ', quoting=csv.QUOTE_MINIMAL)
	# output_writer.writerow(developer_id, novice_answers_count, beginner_answers_count, intermediate_answers_count, experienced_answers_count)
	for data in developer_primary_claim_data:
		output_writer.writerow(data)

with open('./DataSet/Mar-23/patterns_helper_data.csv', 'w') as csvfile:
	output_writer = csv.writer(csvfile, delimiter=',',
	                        quotechar=' ', quoting=csv.QUOTE_MINIMAL)
	for data in patterns_helper_data:
		output_writer.writerow(data)





