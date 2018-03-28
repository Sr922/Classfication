import csv
import statistics as statistics
from scipy.stats import mannwhitneyu
import numpy as np
from stats import Stats

analysis_reader = csv.reader(open('./DataSet/Mar-23/patterns_helper_data.csv', 'rU'), delimiter= ",")

rows = []
for line in analysis_reader:
	rows.append({'id' : line[0], 'novice_easy_answer_count': line[1], 'novice_difficult_answer_count': line[3], 'experienced_easy_answer_count': line[10], 'experienced_difficult_answer_count': line[12]})

noviceAnswersEasy = noviceAnswersEqually = noviceAnswersDifficult = experiencedAnswersEasy = experiencedAnswersEqually = experiencedAnswersDifficult = 0
for developer in rows:
	if(developer['novice_easy_answer_count'] > developer['novice_difficult_answer_count']):
		noviceAnswersEasy=noviceAnswersEasy+1
	elif(developer['novice_easy_answer_count'] == developer['novice_difficult_answer_count']):
		noviceAnswersEqually = noviceAnswersEqually + 1
	else:
		noviceAnswersDifficult = noviceAnswersDifficult+1

	if(developer['experienced_easy_answer_count'] > developer['experienced_difficult_answer_count']):
		experiencedAnswersEasy = experiencedAnswersEasy+1
	elif(developer['experienced_easy_answer_count'] == developer['experienced_difficult_answer_count']):
		experiencedAnswersEqually = experiencedAnswersEqually + 1
	else:
		experiencedAnswersDifficult = experiencedAnswersDifficult+1

totalDevelopers = len(rows)
print(noviceAnswersEasy)
print(noviceAnswersEqually)
print(noviceAnswersDifficult)

print(experiencedAnswersEasy)
print(experiencedAnswersEqually)
print(experiencedAnswersDifficult)


# print('Total Developers ', len(rows))
# print('Not of no developer who have answered more questions in their novice stage than experienced stage ', claim1a,(float(claim1a)/float(totalDevelopers))*100, '%')
# print('Not of no developer who have answered more questions in their novice stage than intermediate stage ', claim1b,(float(claim1b)/float(totalDevelopers))*100, '%')

# print('Not of no developer who have answered less questions in their novice stage than experienced stage ', claim2a, (float(claim2a)/float(totalDevelopers))*100, '%')
# print('Not of no developer who have answered less questions in their novice stage than intermediate stage ', claim2b, (float(claim2b)/float(totalDevelopers))*100, '%')

# print('Not of no developer who have answered equal no of questions in their novice stage and experienced stage ', notAClaim1, (float(notAClaim1)/float(totalDevelopers))*100, '%')
# print('Not of no developer who have answered equal no of questions in their novice stage and intermediate stage ', notAClaim2, (float(notAClaim2)/float(totalDevelopers))*100, '%')

# print(claim2a/len(rows))
# print(claim1b/len(rows))
# print(claim2b/len(rows))
# print(notAClaim1/len(rows))
# print(notAClaim2/len(rows))
