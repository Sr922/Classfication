import csv
import statistics as statistics
from scipy.stats import mannwhitneyu
import numpy as np
from stats import Stats

analysis_reader = csv.reader(open('./DataSet/Mar-23/developer_primary_claim_data.csv', 'rU'), delimiter= ",")

rows = []
for line in analysis_reader:
	rows.append({'id' : line[0], 'novice_answers': line[1], 'beginner_answers': line[2], 'intermediate_answers': line[3], 'experienced_answers': line[4]})

claim1a = claim1b = claim2a = claim2b = notAClaim1 = notAClaim2 = 0
for developer in rows:
	if(developer['novice_answers'] > developer['experienced_answers']):
		claim1a = claim1a+1
	elif(developer['novice_answers'] == developer['experienced_answers']):
		notAClaim1 = notAClaim1 + 1
	else:
		claim2a = claim2a+1

	if(developer['novice_answers'] > developer['intermediate_answers']):
		claim1b = claim1b+1
	elif(developer['novice_answers'] == developer['intermediate_answers']):
		notAClaim2 = notAClaim2 + 1
	else:
		claim2b = claim2b+1

totalDevelopers = len(rows)
print('Total Developers ', len(rows))
print('Not of no developer who have answered more questions in their novice stage than experienced stage ', claim1a,(float(claim1a)/float(totalDevelopers))*100, '%')
print('Not of no developer who have answered more questions in their novice stage than intermediate stage ', claim1b,(float(claim1b)/float(totalDevelopers))*100, '%')

print('Not of no developer who have answered less questions in their novice stage than experienced stage ', claim2a, (float(claim2a)/float(totalDevelopers))*100, '%')
print('Not of no developer who have answered less questions in their novice stage than intermediate stage ', claim2b, (float(claim2b)/float(totalDevelopers))*100, '%')

print('Not of no developer who have answered equal no of questions in their novice stage and experienced stage ', notAClaim1, (float(notAClaim1)/float(totalDevelopers))*100, '%')
print('Not of no developer who have answered equal no of questions in their novice stage and intermediate stage ', notAClaim2, (float(notAClaim2)/float(totalDevelopers))*100, '%')

# print(claim2a/len(rows))
# print(claim1b/len(rows))
# print(claim2b/len(rows))
# print(notAClaim1/len(rows))
# print(notAClaim2/len(rows))
