import csv
import statistics as statistics
from scipy.stats import mannwhitneyu
import numpy as np
from stats import Stats

def cliff(olds,news):
    gt = lt = 0.0
    for  new in news:
        for old in olds:
            if new > old: gt += 1
            if new < old: lt += 1
    return (gt - lt)/(len(olds) * len(news))

def fxsize(olds,news):
    ts=[(0.147,'small'),(0.5,'medium'),(0.8,'large')]
    c = cliff(olds,news)
    least,out = 10**32,ts[-1][1]
    for n,txt in ts:
        delta = abs(n-c)
        if delta < least:
            least,out=delta,txt
    return least
    
analysis_reader = csv.reader(open('./DataSet/Mar-23/analysis.csv', 'rU'), delimiter= ",")

rows = []
for line in analysis_reader:
	if(len(line) >= 7):
		rows.append({'question_type' : line[1], 'wordCount' : line[3], 'polarity': line[4],'subjectivity' : line[5], 'score': line[6], 'viewscount': line[7], 'commentscount': line[8], 'favoritecount': line[9], 'developer' : line[10], 'developer experience' :line[11], 'question_id' : line[0]})

patterns = []
polarity = {}
wordCount = {}
subjectivity = {}

easy = {}
easy['novice'] = {}
easy['novice']['subjectivity'] = []
easy['novice']['polarity'] = []
easy['novice']['word_count'] = []
easy['novice']['score'] = []
easy['novice']['viewscount'] = []
easy['novice']['favoritecount'] = []

easy['beginner'] = {}
easy['beginner']['subjectivity'] = []
easy['beginner']['polarity'] = []
easy['beginner']['word_count'] = []
easy['beginner']['score'] = []
easy['beginner']['viewscount'] = []
easy['beginner']['favoritecount'] = []

easy['intermediate'] = {}
easy['intermediate']['subjectivity'] = []
easy['intermediate']['polarity'] = []
easy['intermediate']['word_count'] = []
easy['intermediate']['score'] = []
easy['intermediate']['viewscount'] = []
easy['intermediate']['favoritecount'] = []

easy['experienced'] = {}
easy['experienced']['subjectivity'] = []
easy['experienced']['polarity'] = []
easy['experienced']['word_count'] = []
easy['experienced']['score'] = []
easy['experienced']['viewscount'] = []
easy['experienced']['favoritecount'] = []

medium = {}
medium['novice'] = {}
medium['novice']['subjectivity'] = []
medium['novice']['polarity'] = []
medium['novice']['word_count'] = []
medium['novice']['score'] = []
medium['novice']['viewscount'] = []
medium['novice']['favoritecount'] = []

medium['beginner'] = {}
medium['beginner']['subjectivity'] = []
medium['beginner']['polarity'] = []
medium['beginner']['word_count'] = []
medium['beginner']['score'] = []
medium['beginner']['viewscount'] = []
medium['beginner']['favoritecount'] = []

medium['intermediate'] = {}
medium['intermediate']['subjectivity'] = []
medium['intermediate']['polarity'] = []
medium['intermediate']['word_count'] = []
medium['intermediate']['score'] = []
medium['intermediate']['viewscount'] = []
medium['intermediate']['favoritecount'] = []

medium['experienced'] = {}
medium['experienced']['subjectivity'] = []
medium['experienced']['polarity'] = []
medium['experienced']['word_count'] = []
medium['experienced']['score'] = []
medium['experienced']['viewscount'] = []
medium['experienced']['favoritecount'] = []

difficult = {}
difficult['novice'] = {}
difficult['novice']['subjectivity'] = []
difficult['novice']['polarity'] = []
difficult['novice']['word_count'] = []
difficult['novice']['score'] = []
difficult['novice']['viewscount'] = []
difficult['novice']['favoritecount'] = []

difficult['beginner'] = {}
difficult['beginner']['subjectivity'] = []
difficult['beginner']['polarity'] = []
difficult['beginner']['word_count'] = []
difficult['beginner']['score'] = []
difficult['beginner']['viewscount'] = []
difficult['beginner']['favoritecount'] = []

difficult['intermediate'] = {}
difficult['intermediate']['subjectivity'] = []
difficult['intermediate']['polarity'] = []
difficult['intermediate']['word_count'] = []
difficult['intermediate']['score'] = []
difficult['intermediate']['viewscount'] = []
difficult['intermediate']['favoritecount'] = []

difficult['experienced'] = {}
difficult['experienced']['subjectivity'] = []
difficult['experienced']['polarity'] = []
difficult['experienced']['word_count'] = []
difficult['experienced']['score'] = []
difficult['experienced']['viewscount'] = []
difficult['experienced']['favoritecount'] = []


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
for developer in developers:
	## Subjectivity
	easy_novice_subjectivity = []
	easy_beginner_subjectivity = []
	easy_intermediate_subjectivity = []
	easy_experienced_subjectivity = []

	medium_novice_subjectivity = []
	medium_beginner_subjectivity = []
	medium_intermediate_subjectivity = []
	medium_experienced_subjectivity = []

	difficult_novice_subjectivity = []
	difficult_beginner_subjectivity = []
	difficult_intermediate_subjectivity = []
	difficult_experienced_subjectivity = []

	## Polarity
	easy_novice_polarity = []
	easy_beginner_polarity = []
	easy_intermediate_polarity = []
	easy_experienced_polarity = []

	medium_novice_polarity = []
	medium_beginner_polarity = []
	medium_intermediate_polarity = []
	medium_experienced_polarity = []

	difficult_novice_polarity = []
	difficult_beginner_polarity = []
	difficult_intermediate_polarity = []
	difficult_experienced_polarity = []

	## Word Count
	easy_novice_word_count = []
	easy_beginner_word_count = []
	easy_intermediate_word_count = []
	easy_experienced_word_count = []

	medium_novice_word_count = []
	medium_beginner_word_count = []
	medium_intermediate_word_count = []
	medium_experienced_word_count = []

	difficult_novice_word_count = []
	difficult_beginner_word_count = []
	difficult_intermediate_word_count = []
	difficult_experienced_word_count = []
	
	## Score
	easy_novice_score = []
	easy_beginner_score = []
	easy_intermediate_score = []
	easy_experienced_score = []

	medium_novice_score = []
	medium_beginner_score = []
	medium_intermediate_score = []
	medium_experienced_score = []

	difficult_novice_score = []
	difficult_beginner_score = []
	difficult_intermediate_score = []
	difficult_experienced_score = []

	## Views Count
	easy_novice_viewscount = []
	easy_beginner_viewscount = []
	easy_intermediate_viewscount = []
	easy_experienced_viewscount = []

	medium_novice_viewscount = []
	medium_beginner_viewscount = []
	medium_intermediate_viewscount = []
	medium_experienced_viewscount = []

	difficult_novice_viewscount = []
	difficult_beginner_viewscount = []
	difficult_intermediate_viewscount = []
	difficult_experienced_viewscount = []

	## Favorite Count
	easy_novice_favoritecount = []
	easy_beginner_favoritecount = []
	easy_intermediate_favoritecount = []
	easy_experienced_favoritecount = []

	medium_novice_favoritecount = []
	medium_beginner_favoritecount = []
	medium_intermediate_favoritecount = []
	medium_experienced_favoritecount = []

	difficult_novice_favoritecount = []
	difficult_beginner_favoritecount = []
	difficult_intermediate_favoritecount = []
	difficult_experienced_favoritecount = []

	novice_answers = novice_easy_answer = novice_medium_answer = novice_difficult_answer = 0
	beginner_answers = beginner_easy_answer = beginner_medium_answer = beginner_difficult_answer = 0
	intermediate_answers = intermediate_easy_answer = intermediate_medium_answer = intermediate_difficult_answer = 0
	experienced_answers = experienced_easy_answer = experienced_medium_answer = experienced_difficult_answer = 0


	for answer in developers[developer]['answers']:
		if(answer['viewscount'] == ''):
			answer['viewscount'] = 0
		if(answer['favoritecount'] == ''):
			answer['favoritecount'] = 0

		if(answer['question_type'].lower() == 'easy'):
			if(answer['developer experience'].lower() == 'novice'):
				easy_novice_subjectivity.append(answer['subjectivity'])
				easy_novice_polarity.append(answer['polarity'])
				easy_novice_word_count.append(answer['wordCount'])
				easy_novice_score.append(answer['score'])
				easy_novice_viewscount.append(answer['viewscount'])
				easy_novice_favoritecount.append(answer['favoritecount'])
				novice_easy_answer = novice_easy_answer + 1

			if(answer['developer experience'].lower() == 'beginner'):
				easy_beginner_subjectivity.append(answer['subjectivity'])
				easy_beginner_polarity.append(answer['polarity'])
				easy_beginner_word_count.append(answer['wordCount'])
				easy_beginner_score.append(answer['score'])
				easy_beginner_viewscount.append(answer['viewscount'])
				easy_beginner_favoritecount.append(answer['favoritecount'])
				beginner_easy_answer = beginner_easy_answer + 1

				
			if(answer['developer experience'].lower() == 'intermediate'):
				easy_intermediate_subjectivity.append(answer['subjectivity'])
				easy_intermediate_polarity.append(answer['polarity'])
				easy_intermediate_word_count.append(answer['wordCount'])
				easy_intermediate_score.append(answer['score'])
				easy_intermediate_viewscount.append(answer['viewscount'])
				easy_intermediate_favoritecount.append(answer['favoritecount'])
				intermediate_easy_answer = intermediate_easy_answer + 1
				
			if(answer['developer experience'].lower() == 'experienced'):
				easy_experienced_subjectivity.append(answer['subjectivity'])
				easy_experienced_polarity.append(answer['polarity'])
				easy_experienced_word_count.append(answer['wordCount'])
				easy_experienced_score.append(answer['score'])
				easy_experienced_viewscount.append(answer['viewscount'])
				easy_experienced_favoritecount.append(answer['favoritecount'])
				experienced_easy_answer = experienced_easy_answer + 1

		if(answer['question_type'].lower() == 'medium'):
			if(answer['developer experience'].lower() == 'novice'):
				medium_novice_subjectivity.append(answer['subjectivity'])
				medium_novice_polarity.append(answer['polarity'])
				medium_novice_word_count.append(answer['wordCount'])
				medium_novice_score.append(answer['score'])
				medium_novice_viewscount.append(answer['viewscount'])
				medium_novice_favoritecount.append(answer['favoritecount'])
				novice_medium_answer = novice_medium_answer + 1
				
			if(answer['developer experience'].lower() == 'beginner'):
				medium_beginner_subjectivity.append(answer['subjectivity'])
				medium_beginner_polarity.append(answer['polarity'])
				medium_beginner_word_count.append(answer['wordCount'])
				medium_beginner_score.append(answer['score'])
				medium_beginner_viewscount.append(answer['viewscount'])
				medium_beginner_favoritecount.append(answer['favoritecount'])
				beginner_medium_answer = beginner_medium_answer + 1
				
			if(answer['developer experience'].lower() == 'intermediate'):
				medium_intermediate_subjectivity.append(answer['subjectivity'])
				medium_intermediate_polarity.append(answer['polarity'])
				medium_intermediate_word_count.append(answer['wordCount'])
				medium_intermediate_score.append(answer['score'])
				medium_intermediate_viewscount.append(answer['viewscount'])
				medium_intermediate_favoritecount.append(answer['favoritecount'])
				intermediate_medium_answer = intermediate_medium_answer + 1
				
			if(answer['developer experience'].lower() == 'experienced'):
				medium_experienced_subjectivity.append(answer['subjectivity'])
				medium_experienced_polarity.append(answer['polarity'])
				medium_experienced_word_count.append(answer['wordCount'])
				medium_experienced_score.append(answer['score'])
				medium_experienced_viewscount.append(answer['viewscount'])
				medium_experienced_favoritecount.append(answer['favoritecount'])
				experienced_medium_answer = experienced_medium_answer + 1
			

		if(answer['question_type'].lower() == 'difficult'):
			if(answer['developer experience'].lower() == 'novice'):
				difficult_novice_subjectivity.append(answer['subjectivity'])
				difficult_novice_polarity.append(answer['polarity'])
				difficult_novice_word_count.append(answer['wordCount'])
				difficult_novice_score.append(answer['score'])
				difficult_novice_viewscount.append(answer['viewscount'])
				difficult_novice_favoritecount.append(answer['favoritecount'])
				novice_difficult_answer = novice_difficult_answer + 1

			if(answer['developer experience'].lower() == 'beginner'):
				difficult_beginner_subjectivity.append(answer['subjectivity'])
				difficult_beginner_polarity.append(answer['polarity'])
				difficult_beginner_word_count.append(answer['wordCount'])
				difficult_beginner_score.append(answer['score'])
				difficult_beginner_viewscount.append(answer['viewscount'])
				difficult_beginner_favoritecount.append(answer['favoritecount'])
				beginner_difficult_answer = beginner_difficult_answer + 1
			
			if(answer['developer experience'].lower() == 'intermediate'):
				difficult_intermediate_subjectivity.append(answer['subjectivity'])
				difficult_intermediate_polarity.append(answer['polarity'])
				difficult_intermediate_word_count.append(answer['wordCount'])
				difficult_intermediate_score.append(answer['score'])
				difficult_intermediate_viewscount.append(answer['viewscount'])
				difficult_intermediate_favoritecount.append(answer['favoritecount'])
				intermediate_difficult_answer = intermediate_difficult_answer + 1
			
			if(answer['developer experience'].lower() == 'experienced'):
				difficult_experienced_subjectivity.append(answer['subjectivity'])
				difficult_experienced_polarity.append(answer['polarity'])
				difficult_experienced_word_count.append(answer['wordCount'])
				difficult_experienced_score.append(answer['score'])
				difficult_experienced_viewscount.append(answer['viewscount'])
				difficult_experienced_favoritecount.append(answer['favoritecount'])
				experienced_difficult_answer = experienced_difficult_answer + 1

	novice_answers = novice_easy_answer + novice_medium_answer + novice_difficult_answer
	beginner_answers = beginner_easy_answer + beginner_medium_answer + beginner_difficult_answer
	intermediate_answers = intermediate_easy_answer + intermediate_medium_answer + intermediate_difficult_answer
	experienced_answers = experienced_easy_answer + experienced_medium_answer + experienced_difficult_answer

	# print(len(developers[developer]['answers']))
	# totalAnswers = novice_answers + beginner_answers + intermediate_answers + experienced_answers
	# print(totalAnswers)
	# print(len(developers[developer]['answers']) == totalAnswers)
	developers[developer]['subjectivity'] = {}
	developers[developer]['subjectivity']['easy_novice_mean'] = np.mean(np.array(easy_novice_subjectivity).astype(np.float)) if len(easy_novice_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['easy_beginner_mean'] = np.mean(np.array(easy_beginner_subjectivity).astype(np.float)) if len(easy_beginner_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['easy_intermediate_mean'] = np.mean(np.array(easy_intermediate_subjectivity).astype(np.float)) if len(easy_intermediate_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['easy_experienced_mean'] = np.mean(np.array(easy_experienced_subjectivity).astype(np.float)) if len(easy_experienced_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['medium_novice_mean'] = np.mean(np.array(medium_novice_subjectivity).astype(np.float)) if len(medium_novice_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['medium_beginner_mean'] = np.mean(np.array(medium_beginner_subjectivity).astype(np.float)) if len(medium_beginner_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['medium_intermediate_mean'] = np.mean(np.array(medium_intermediate_subjectivity).astype(np.float)) if len(medium_intermediate_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['medium_experienced_mean'] = np.mean(np.array(medium_experienced_subjectivity).astype(np.float)) if len(medium_experienced_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['difficult_novice_mean'] = np.mean(np.array(difficult_novice_subjectivity).astype(np.float)) if len(difficult_novice_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['difficult_beginner_mean'] = np.mean(np.array(difficult_beginner_subjectivity).astype(np.float)) if len(difficult_beginner_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['difficult_intermediate_mean'] = np.mean(np.array(difficult_intermediate_subjectivity).astype(np.float)) if len(difficult_intermediate_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['difficult_experienced_mean'] = np.mean(np.array(difficult_experienced_subjectivity).astype(np.float)) if len(difficult_experienced_subjectivity) > 0 else -1

	developers[developer]['subjectivity']['easy_novice_max'] = np.amax(np.array(easy_novice_subjectivity).astype(np.float)) if len(easy_novice_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['easy_beginner_max'] = np.amax(np.array(easy_beginner_subjectivity).astype(np.float)) if len(easy_beginner_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['easy_intermediate_max'] = np.amax(np.array(easy_intermediate_subjectivity).astype(np.float)) if len(easy_intermediate_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['easy_experienced_max'] = np.amax(np.array(easy_experienced_subjectivity).astype(np.float)) if len(easy_experienced_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['medium_novice_max'] = np.amax(np.array(medium_novice_subjectivity).astype(np.float)) if len(medium_novice_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['medium_beginner_max'] = np.amax(np.array(medium_beginner_subjectivity).astype(np.float)) if len(medium_beginner_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['medium_intermediate_max'] = np.amax(np.array(medium_intermediate_subjectivity).astype(np.float)) if len(medium_intermediate_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['medium_experienced_max'] = np.amax(np.array(medium_experienced_subjectivity).astype(np.float)) if len(medium_experienced_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['difficult_novice_max'] = np.amax(np.array(difficult_novice_subjectivity).astype(np.float)) if len(difficult_novice_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['difficult_beginner_max'] = np.amax(np.array(difficult_beginner_subjectivity).astype(np.float)) if len(difficult_beginner_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['difficult_intermediate_max'] = np.amax(np.array(difficult_intermediate_subjectivity).astype(np.float)) if len(difficult_intermediate_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['difficult_experienced_max'] = np.amax(np.array(difficult_experienced_subjectivity).astype(np.float)) if len(difficult_experienced_subjectivity) > 0 else -1

	developers[developer]['subjectivity']['easy_novice_min'] = np.amin(np.array(easy_novice_subjectivity).astype(np.float)) if len(easy_novice_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['easy_beginner_min'] = np.amin(np.array(easy_beginner_subjectivity).astype(np.float)) if len(easy_beginner_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['easy_intermediate_min'] = np.amin(np.array(easy_intermediate_subjectivity).astype(np.float)) if len(easy_intermediate_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['easy_experienced_min'] = np.amin(np.array(easy_experienced_subjectivity).astype(np.float)) if len(easy_experienced_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['medium_novice_min'] = np.amin(np.array(medium_novice_subjectivity).astype(np.float)) if len(medium_novice_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['medium_beginner_min'] = np.amin(np.array(medium_beginner_subjectivity).astype(np.float)) if len(medium_beginner_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['medium_intermediate_min'] = np.amin(np.array(medium_intermediate_subjectivity).astype(np.float)) if len(medium_intermediate_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['medium_experienced_min'] = np.amin(np.array(medium_experienced_subjectivity).astype(np.float)) if len(medium_experienced_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['difficult_novice_min'] = np.amin(np.array(difficult_novice_subjectivity).astype(np.float)) if len(difficult_novice_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['difficult_beginner_min'] = np.amin(np.array(difficult_beginner_subjectivity).astype(np.float)) if len(difficult_beginner_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['difficult_intermediate_min'] = np.amin(np.array(difficult_intermediate_subjectivity).astype(np.float)) if len(difficult_intermediate_subjectivity) > 0 else -1
	developers[developer]['subjectivity']['difficult_experienced_min'] = np.amin(np.array(difficult_experienced_subjectivity).astype(np.float)) if len(difficult_experienced_subjectivity) > 0 else -1

	## Polarity
	developers[developer]['polarity'] = {}
	developers[developer]['polarity']['easy_novice_mean'] = np.mean(np.array(easy_novice_polarity).astype(np.float)) if len(easy_novice_polarity) > 0 else -1
	developers[developer]['polarity']['easy_beginner_mean'] = np.mean(np.array(easy_beginner_polarity).astype(np.float)) if len(easy_beginner_polarity) > 0 else -1
	developers[developer]['polarity']['easy_intermediate_mean'] = np.mean(np.array(easy_intermediate_polarity).astype(np.float)) if len(easy_intermediate_polarity) > 0 else -1
	developers[developer]['polarity']['easy_experienced_mean'] = np.mean(np.array(easy_experienced_polarity).astype(np.float)) if len(easy_experienced_polarity) > 0 else -1
	developers[developer]['polarity']['medium_novice_mean'] = np.mean(np.array(medium_novice_polarity).astype(np.float)) if len(medium_novice_polarity) > 0 else -1
	developers[developer]['polarity']['medium_beginner_mean'] = np.mean(np.array(medium_beginner_polarity).astype(np.float)) if len(medium_beginner_polarity) > 0 else -1
	developers[developer]['polarity']['medium_intermediate_mean'] = np.mean(np.array(medium_intermediate_polarity).astype(np.float)) if len(medium_intermediate_polarity) > 0 else -1
	developers[developer]['polarity']['medium_experienced_mean'] = np.mean(np.array(medium_experienced_polarity).astype(np.float)) if len(medium_experienced_polarity) > 0 else -1
	developers[developer]['polarity']['difficult_novice_mean'] = np.mean(np.array(difficult_novice_polarity).astype(np.float)) if len(difficult_novice_polarity) > 0 else -1
	developers[developer]['polarity']['difficult_beginner_mean'] = np.mean(np.array(difficult_beginner_polarity).astype(np.float)) if len(difficult_beginner_polarity) > 0 else -1
	developers[developer]['polarity']['difficult_intermediate_mean'] = np.mean(np.array(difficult_intermediate_polarity).astype(np.float)) if len(difficult_intermediate_polarity) > 0 else -1
	developers[developer]['polarity']['difficult_experienced_mean'] = np.mean(np.array(difficult_experienced_polarity).astype(np.float)) if len(difficult_experienced_polarity) > 0 else -1

	developers[developer]['polarity']['easy_novice_max'] = np.amax(np.array(easy_novice_polarity).astype(np.float)) if len(easy_novice_polarity) > 0 else -1
	developers[developer]['polarity']['easy_beginner_max'] = np.amax(np.array(easy_beginner_polarity).astype(np.float)) if len(easy_beginner_polarity) > 0 else -1
	developers[developer]['polarity']['easy_intermediate_max'] = np.amax(np.array(easy_intermediate_polarity).astype(np.float)) if len(easy_intermediate_polarity) > 0 else -1
	developers[developer]['polarity']['easy_experienced_max'] = np.amax(np.array(easy_experienced_polarity).astype(np.float)) if len(easy_experienced_polarity) > 0 else -1
	developers[developer]['polarity']['medium_novice_max'] = np.amax(np.array(medium_novice_polarity).astype(np.float)) if len(medium_novice_polarity) > 0 else -1
	developers[developer]['polarity']['medium_beginner_max'] = np.amax(np.array(medium_beginner_polarity).astype(np.float)) if len(medium_beginner_polarity) > 0 else -1
	developers[developer]['polarity']['medium_intermediate_max'] = np.amax(np.array(medium_intermediate_polarity).astype(np.float)) if len(medium_intermediate_polarity) > 0 else -1
	developers[developer]['polarity']['medium_experienced_max'] = np.amax(np.array(medium_experienced_polarity).astype(np.float)) if len(medium_experienced_polarity) > 0 else -1
	developers[developer]['polarity']['difficult_novice_max'] = np.amax(np.array(difficult_novice_polarity).astype(np.float)) if len(difficult_novice_polarity) > 0 else -1
	developers[developer]['polarity']['difficult_beginner_max'] = np.amax(np.array(difficult_beginner_polarity).astype(np.float)) if len(difficult_beginner_polarity) > 0 else -1
	developers[developer]['polarity']['difficult_intermediate_max'] = np.amax(np.array(difficult_intermediate_polarity).astype(np.float)) if len(difficult_intermediate_polarity) > 0 else -1
	developers[developer]['polarity']['difficult_experienced_max'] = np.amax(np.array(difficult_experienced_polarity).astype(np.float)) if len(difficult_experienced_polarity) > 0 else -1

	developers[developer]['polarity']['easy_novice_min'] = np.amin(np.array(easy_novice_polarity).astype(np.float)) if len(easy_novice_polarity) > 0 else -1
	developers[developer]['polarity']['easy_beginner_min'] = np.amin(np.array(easy_beginner_polarity).astype(np.float)) if len(easy_beginner_polarity) > 0 else -1
	developers[developer]['polarity']['easy_intermediate_min'] = np.amin(np.array(easy_intermediate_polarity).astype(np.float)) if len(easy_intermediate_polarity) > 0 else -1
	developers[developer]['polarity']['easy_experienced_min'] = np.amin(np.array(easy_experienced_polarity).astype(np.float)) if len(easy_experienced_polarity) > 0 else -1
	developers[developer]['polarity']['medium_novice_min'] = np.amin(np.array(medium_novice_polarity).astype(np.float)) if len(medium_novice_polarity) > 0 else -1
	developers[developer]['polarity']['medium_beginner_min'] = np.amin(np.array(medium_beginner_polarity).astype(np.float)) if len(medium_beginner_polarity) > 0 else -1
	developers[developer]['polarity']['medium_intermediate_min'] = np.amin(np.array(medium_intermediate_polarity).astype(np.float)) if len(medium_intermediate_polarity) > 0 else -1
	developers[developer]['polarity']['medium_experienced_min'] = np.amin(np.array(medium_experienced_polarity).astype(np.float)) if len(medium_experienced_polarity) > 0 else -1
	developers[developer]['polarity']['difficult_novice_min'] = np.amin(np.array(difficult_novice_polarity).astype(np.float)) if len(difficult_novice_polarity) > 0 else -1
	developers[developer]['polarity']['difficult_beginner_min'] = np.amin(np.array(difficult_beginner_polarity).astype(np.float)) if len(difficult_beginner_polarity) > 0 else -1
	developers[developer]['polarity']['difficult_intermediate_min'] = np.amin(np.array(difficult_intermediate_polarity).astype(np.float)) if len(difficult_intermediate_polarity) > 0 else -1
	developers[developer]['polarity']['difficult_experienced_min'] = np.amin(np.array(difficult_experienced_polarity).astype(np.float)) if len(difficult_experienced_polarity) > 0 else -1

	## Word Count
	developers[developer]['word_count'] = {}
	developers[developer]['word_count']['easy_novice_mean'] = np.mean(np.array(easy_novice_word_count).astype(np.float)) if len(easy_novice_word_count) > 0 else -1
	developers[developer]['word_count']['easy_beginner_mean'] = np.mean(np.array(easy_beginner_word_count).astype(np.float)) if len(easy_beginner_word_count) > 0 else -1
	developers[developer]['word_count']['easy_intermediate_mean'] = np.mean(np.array(easy_intermediate_word_count).astype(np.float)) if len(easy_intermediate_word_count) > 0 else -1
	developers[developer]['word_count']['easy_experienced_mean'] = np.mean(np.array(easy_experienced_word_count).astype(np.float)) if len(easy_experienced_word_count) > 0 else -1
	developers[developer]['word_count']['medium_novice_mean'] = np.mean(np.array(medium_novice_word_count).astype(np.float)) if len(medium_novice_word_count) > 0 else -1
	developers[developer]['word_count']['medium_beginner_mean'] = np.mean(np.array(medium_beginner_word_count).astype(np.float)) if len(medium_beginner_word_count) > 0 else -1
	developers[developer]['word_count']['medium_intermediate_mean'] = np.mean(np.array(medium_intermediate_word_count).astype(np.float)) if len(medium_intermediate_word_count) > 0 else -1
	developers[developer]['word_count']['medium_experienced_mean'] = np.mean(np.array(medium_experienced_word_count).astype(np.float)) if len(medium_experienced_word_count) > 0 else -1
	developers[developer]['word_count']['difficult_novice_mean'] = np.mean(np.array(difficult_novice_word_count).astype(np.float)) if len(difficult_novice_word_count) > 0 else -1
	developers[developer]['word_count']['difficult_beginner_mean'] = np.mean(np.array(difficult_beginner_word_count).astype(np.float)) if len(difficult_beginner_word_count) > 0 else -1
	developers[developer]['word_count']['difficult_intermediate_mean'] = np.mean(np.array(difficult_intermediate_word_count).astype(np.float)) if len(difficult_intermediate_word_count) > 0 else -1
	developers[developer]['word_count']['difficult_experienced_mean'] = np.mean(np.array(difficult_experienced_word_count).astype(np.float)) if len(difficult_experienced_word_count) > 0 else -1

	developers[developer]['word_count']['easy_novice_max'] = np.amax(np.array(easy_novice_word_count).astype(np.float)) if len(easy_novice_word_count) > 0 else -1
	developers[developer]['word_count']['easy_beginner_max'] = np.amax(np.array(easy_beginner_word_count).astype(np.float)) if len(easy_beginner_word_count) > 0 else -1
	developers[developer]['word_count']['easy_intermediate_max'] = np.amax(np.array(easy_intermediate_word_count).astype(np.float)) if len(easy_intermediate_word_count) > 0 else -1
	developers[developer]['word_count']['easy_experienced_max'] = np.amax(np.array(easy_experienced_word_count).astype(np.float)) if len(easy_experienced_word_count) > 0 else -1
	developers[developer]['word_count']['medium_novice_max'] = np.amax(np.array(medium_novice_word_count).astype(np.float)) if len(medium_novice_word_count) > 0 else -1
	developers[developer]['word_count']['medium_beginner_max'] = np.amax(np.array(medium_beginner_word_count).astype(np.float)) if len(medium_beginner_word_count) > 0 else -1
	developers[developer]['word_count']['medium_intermediate_max'] = np.amax(np.array(medium_intermediate_word_count).astype(np.float)) if len(medium_intermediate_word_count) > 0 else -1
	developers[developer]['word_count']['medium_experienced_max'] = np.amax(np.array(medium_experienced_word_count).astype(np.float)) if len(medium_experienced_word_count) > 0 else -1
	developers[developer]['word_count']['difficult_novice_max'] = np.amax(np.array(difficult_novice_word_count).astype(np.float)) if len(difficult_novice_word_count) > 0 else -1
	developers[developer]['word_count']['difficult_beginner_max'] = np.amax(np.array(difficult_beginner_word_count).astype(np.float)) if len(difficult_beginner_word_count) > 0 else -1
	developers[developer]['word_count']['difficult_intermediate_max'] = np.amax(np.array(difficult_intermediate_word_count).astype(np.float)) if len(difficult_intermediate_word_count) > 0 else -1
	developers[developer]['word_count']['difficult_experienced_max'] = np.amax(np.array(difficult_experienced_word_count).astype(np.float)) if len(difficult_experienced_word_count) > 0 else -1

	developers[developer]['word_count']['easy_novice_min'] = np.amin(np.array(easy_novice_word_count).astype(np.float)) if len(easy_novice_word_count) > 0 else -1
	developers[developer]['word_count']['easy_beginner_min'] = np.amin(np.array(easy_beginner_word_count).astype(np.float)) if len(easy_beginner_word_count) > 0 else -1
	developers[developer]['word_count']['easy_intermediate_min'] = np.amin(np.array(easy_intermediate_word_count).astype(np.float)) if len(easy_intermediate_word_count) > 0 else -1
	developers[developer]['word_count']['easy_experienced_min'] = np.amin(np.array(easy_experienced_word_count).astype(np.float)) if len(easy_experienced_word_count) > 0 else -1
	developers[developer]['word_count']['medium_novice_min'] = np.amin(np.array(medium_novice_word_count).astype(np.float)) if len(medium_novice_word_count) > 0 else -1
	developers[developer]['word_count']['medium_beginner_min'] = np.amin(np.array(medium_beginner_word_count).astype(np.float)) if len(medium_beginner_word_count) > 0 else -1
	developers[developer]['word_count']['medium_intermediate_min'] = np.amin(np.array(medium_intermediate_word_count).astype(np.float)) if len(medium_intermediate_word_count) > 0 else -1
	developers[developer]['word_count']['medium_experienced_min'] = np.amin(np.array(medium_experienced_word_count).astype(np.float)) if len(medium_experienced_word_count) > 0 else -1
	developers[developer]['word_count']['difficult_novice_min'] = np.amin(np.array(difficult_novice_word_count).astype(np.float)) if len(difficult_novice_word_count) > 0 else -1
	developers[developer]['word_count']['difficult_beginner_min'] = np.amin(np.array(difficult_beginner_word_count).astype(np.float)) if len(difficult_beginner_word_count) > 0 else -1
	developers[developer]['word_count']['difficult_intermediate_min'] = np.amin(np.array(difficult_intermediate_word_count).astype(np.float)) if len(difficult_intermediate_word_count) > 0 else -1
	developers[developer]['word_count']['difficult_experienced_min'] = np.amin(np.array(difficult_experienced_word_count).astype(np.float)) if len(difficult_experienced_word_count) > 0 else -1

	## Score
	developers[developer]['score'] = {}
	developers[developer]['score']['easy_novice_mean'] = np.mean(np.array(easy_novice_score).astype(np.float)) if len(easy_novice_score) > 0 else -1
	developers[developer]['score']['easy_beginner_mean'] = np.mean(np.array(easy_beginner_score).astype(np.float)) if len(easy_beginner_score) > 0 else -1
	developers[developer]['score']['easy_intermediate_mean'] = np.mean(np.array(easy_intermediate_score).astype(np.float)) if len(easy_intermediate_score) > 0 else -1
	developers[developer]['score']['easy_experienced_mean'] = np.mean(np.array(easy_experienced_score).astype(np.float)) if len(easy_experienced_score) > 0 else -1
	developers[developer]['score']['medium_novice_mean'] = np.mean(np.array(medium_novice_score).astype(np.float)) if len(medium_novice_score) > 0 else -1
	developers[developer]['score']['medium_beginner_mean'] = np.mean(np.array(medium_beginner_score).astype(np.float)) if len(medium_beginner_score) > 0 else -1
	developers[developer]['score']['medium_intermediate_mean'] = np.mean(np.array(medium_intermediate_score).astype(np.float)) if len(medium_intermediate_score) > 0 else -1
	developers[developer]['score']['medium_experienced_mean'] = np.mean(np.array(medium_experienced_score).astype(np.float)) if len(medium_experienced_score) > 0 else -1
	developers[developer]['score']['difficult_novice_mean'] = np.mean(np.array(difficult_novice_score).astype(np.float)) if len(difficult_novice_score) > 0 else -1
	developers[developer]['score']['difficult_beginner_mean'] = np.mean(np.array(difficult_beginner_score).astype(np.float)) if len(difficult_beginner_score) > 0 else -1
	developers[developer]['score']['difficult_intermediate_mean'] = np.mean(np.array(difficult_intermediate_score).astype(np.float)) if len(difficult_intermediate_score) > 0 else -1
	developers[developer]['score']['difficult_experienced_mean'] = np.mean(np.array(difficult_experienced_score).astype(np.float)) if len(difficult_experienced_score) > 0 else -1

	developers[developer]['score']['easy_novice_max'] = np.amax(np.array(easy_novice_score).astype(np.float)) if len(easy_novice_score) > 0 else -1
	developers[developer]['score']['easy_beginner_max'] = np.amax(np.array(easy_beginner_score).astype(np.float)) if len(easy_beginner_score) > 0 else -1
	developers[developer]['score']['easy_intermediate_max'] = np.amax(np.array(easy_intermediate_score).astype(np.float)) if len(easy_intermediate_score) > 0 else -1
	developers[developer]['score']['easy_experienced_max'] = np.amax(np.array(easy_experienced_score).astype(np.float)) if len(easy_experienced_score) > 0 else -1
	developers[developer]['score']['medium_novice_max'] = np.amax(np.array(medium_novice_score).astype(np.float)) if len(medium_novice_score) > 0 else -1
	developers[developer]['score']['medium_beginner_max'] = np.amax(np.array(medium_beginner_score).astype(np.float)) if len(medium_beginner_score) > 0 else -1
	developers[developer]['score']['medium_intermediate_max'] = np.amax(np.array(medium_intermediate_score).astype(np.float)) if len(medium_intermediate_score) > 0 else -1
	developers[developer]['score']['medium_experienced_max'] = np.amax(np.array(medium_experienced_score).astype(np.float)) if len(medium_experienced_score) > 0 else -1
	developers[developer]['score']['difficult_novice_max'] = np.amax(np.array(difficult_novice_score).astype(np.float)) if len(difficult_novice_score) > 0 else -1
	developers[developer]['score']['difficult_beginner_max'] = np.amax(np.array(difficult_beginner_score).astype(np.float)) if len(difficult_beginner_score) > 0 else -1
	developers[developer]['score']['difficult_intermediate_max'] = np.amax(np.array(difficult_intermediate_score).astype(np.float)) if len(difficult_intermediate_score) > 0 else -1
	developers[developer]['score']['difficult_experienced_max'] = np.amax(np.array(difficult_experienced_score).astype(np.float)) if len(difficult_experienced_score) > 0 else -1

	developers[developer]['score']['easy_novice_min'] = np.amin(np.array(easy_novice_score).astype(np.float)) if len(easy_novice_score) > 0 else -1
	developers[developer]['score']['easy_beginner_min'] = np.amin(np.array(easy_beginner_score).astype(np.float)) if len(easy_beginner_score) > 0 else -1
	developers[developer]['score']['easy_intermediate_min'] = np.amin(np.array(easy_intermediate_score).astype(np.float)) if len(easy_intermediate_score) > 0 else -1
	developers[developer]['score']['easy_experienced_min'] = np.amin(np.array(easy_experienced_score).astype(np.float)) if len(easy_experienced_score) > 0 else -1
	developers[developer]['score']['medium_novice_min'] = np.amin(np.array(medium_novice_score).astype(np.float)) if len(medium_novice_score) > 0 else -1
	developers[developer]['score']['medium_beginner_min'] = np.amin(np.array(medium_beginner_score).astype(np.float)) if len(medium_beginner_score) > 0 else -1
	developers[developer]['score']['medium_intermediate_min'] = np.amin(np.array(medium_intermediate_score).astype(np.float)) if len(medium_intermediate_score) > 0 else -1
	developers[developer]['score']['medium_experienced_min'] = np.amin(np.array(medium_experienced_score).astype(np.float)) if len(medium_experienced_score) > 0 else -1
	developers[developer]['score']['difficult_novice_min'] = np.amin(np.array(difficult_novice_score).astype(np.float)) if len(difficult_novice_score) > 0 else -1
	developers[developer]['score']['difficult_beginner_min'] = np.amin(np.array(difficult_beginner_score).astype(np.float)) if len(difficult_beginner_score) > 0 else -1
	developers[developer]['score']['difficult_intermediate_min'] = np.amin(np.array(difficult_intermediate_score).astype(np.float)) if len(difficult_intermediate_score) > 0 else -1
	developers[developer]['score']['difficult_experienced_min'] = np.amin(np.array(difficult_experienced_score).astype(np.float)) if len(difficult_experienced_score) > 0 else -1

	## Views Count
	developers[developer]['viewscount'] = {}
	developers[developer]['viewscount']['easy_novice_mean'] = np.mean(np.array(easy_novice_viewscount).astype(np.float)) if len(easy_novice_viewscount) > 0 else -1
	developers[developer]['viewscount']['easy_beginner_mean'] = np.mean(np.array(easy_beginner_viewscount).astype(np.float)) if len(easy_beginner_viewscount) > 0 else -1
	developers[developer]['viewscount']['easy_intermediate_mean'] = np.mean(np.array(easy_intermediate_viewscount).astype(np.float)) if len(easy_intermediate_viewscount) > 0 else -1
	developers[developer]['viewscount']['easy_experienced_mean'] = np.mean(np.array(easy_experienced_viewscount).astype(np.float)) if len(easy_experienced_viewscount) > 0 else -1
	developers[developer]['viewscount']['medium_novice_mean'] = np.mean(np.array(medium_novice_viewscount).astype(np.float)) if len(medium_novice_viewscount) > 0 else -1
	developers[developer]['viewscount']['medium_beginner_mean'] = np.mean(np.array(medium_beginner_viewscount).astype(np.float)) if len(medium_beginner_viewscount) > 0 else -1
	developers[developer]['viewscount']['medium_intermediate_mean'] = np.mean(np.array(medium_intermediate_viewscount).astype(np.float)) if len(medium_intermediate_viewscount) > 0 else -1
	developers[developer]['viewscount']['medium_experienced_mean'] = np.mean(np.array(medium_experienced_viewscount).astype(np.float)) if len(medium_experienced_viewscount) > 0 else -1
	developers[developer]['viewscount']['difficult_novice_mean'] = np.mean(np.array(difficult_novice_viewscount).astype(np.float)) if len(difficult_novice_viewscount) > 0 else -1
	developers[developer]['viewscount']['difficult_beginner_mean'] = np.mean(np.array(difficult_beginner_viewscount).astype(np.float)) if len(difficult_beginner_viewscount) > 0 else -1
	developers[developer]['viewscount']['difficult_intermediate_mean'] = np.mean(np.array(difficult_intermediate_viewscount).astype(np.float)) if len(difficult_intermediate_viewscount) > 0 else -1
	developers[developer]['viewscount']['difficult_experienced_mean'] = np.mean(np.array(difficult_experienced_viewscount).astype(np.float)) if len(difficult_experienced_viewscount) > 0 else -1

	developers[developer]['viewscount']['easy_novice_max'] = np.amax(np.array(easy_novice_viewscount).astype(np.float)) if len(easy_novice_viewscount) > 0 else -1
	developers[developer]['viewscount']['easy_beginner_max'] = np.amax(np.array(easy_beginner_viewscount).astype(np.float)) if len(easy_beginner_viewscount) > 0 else -1
	developers[developer]['viewscount']['easy_intermediate_max'] = np.amax(np.array(easy_intermediate_viewscount).astype(np.float)) if len(easy_intermediate_viewscount) > 0 else -1
	developers[developer]['viewscount']['easy_experienced_max'] = np.amax(np.array(easy_experienced_viewscount).astype(np.float)) if len(easy_experienced_viewscount) > 0 else -1
	developers[developer]['viewscount']['medium_novice_max'] = np.amax(np.array(medium_novice_viewscount).astype(np.float)) if len(medium_novice_viewscount) > 0 else -1
	developers[developer]['viewscount']['medium_beginner_max'] = np.amax(np.array(medium_beginner_viewscount).astype(np.float)) if len(medium_beginner_viewscount) > 0 else -1
	developers[developer]['viewscount']['medium_intermediate_max'] = np.amax(np.array(medium_intermediate_viewscount).astype(np.float)) if len(medium_intermediate_viewscount) > 0 else -1
	developers[developer]['viewscount']['medium_experienced_max'] = np.amax(np.array(medium_experienced_viewscount).astype(np.float)) if len(medium_experienced_viewscount) > 0 else -1
	developers[developer]['viewscount']['difficult_novice_max'] = np.amax(np.array(difficult_novice_viewscount).astype(np.float)) if len(difficult_novice_viewscount) > 0 else -1
	developers[developer]['viewscount']['difficult_beginner_max'] = np.amax(np.array(difficult_beginner_viewscount).astype(np.float)) if len(difficult_beginner_viewscount) > 0 else -1
	developers[developer]['viewscount']['difficult_intermediate_max'] = np.amax(np.array(difficult_intermediate_viewscount).astype(np.float)) if len(difficult_intermediate_viewscount) > 0 else -1
	developers[developer]['viewscount']['difficult_experienced_max'] = np.amax(np.array(difficult_experienced_viewscount).astype(np.float)) if len(difficult_experienced_viewscount) > 0 else -1

	developers[developer]['viewscount']['easy_novice_min'] = np.amin(np.array(easy_novice_viewscount).astype(np.float)) if len(easy_novice_viewscount) > 0 else -1
	developers[developer]['viewscount']['easy_beginner_min'] = np.amin(np.array(easy_beginner_viewscount).astype(np.float)) if len(easy_beginner_viewscount) > 0 else -1
	developers[developer]['viewscount']['easy_intermediate_min'] = np.amin(np.array(easy_intermediate_viewscount).astype(np.float)) if len(easy_intermediate_viewscount) > 0 else -1
	developers[developer]['viewscount']['easy_experienced_min'] = np.amin(np.array(easy_experienced_viewscount).astype(np.float)) if len(easy_experienced_viewscount) > 0 else -1
	developers[developer]['viewscount']['medium_novice_min'] = np.amin(np.array(medium_novice_viewscount).astype(np.float)) if len(medium_novice_viewscount) > 0 else -1
	developers[developer]['viewscount']['medium_beginner_min'] = np.amin(np.array(medium_beginner_viewscount).astype(np.float)) if len(medium_beginner_viewscount) > 0 else -1
	developers[developer]['viewscount']['medium_intermediate_min'] = np.amin(np.array(medium_intermediate_viewscount).astype(np.float)) if len(medium_intermediate_viewscount) > 0 else -1
	developers[developer]['viewscount']['medium_experienced_min'] = np.amin(np.array(medium_experienced_viewscount).astype(np.float)) if len(medium_experienced_viewscount) > 0 else -1
	developers[developer]['viewscount']['difficult_novice_min'] = np.amin(np.array(difficult_novice_viewscount).astype(np.float)) if len(difficult_novice_viewscount) > 0 else -1
	developers[developer]['viewscount']['difficult_beginner_min'] = np.amin(np.array(difficult_beginner_viewscount).astype(np.float)) if len(difficult_beginner_viewscount) > 0 else -1
	developers[developer]['viewscount']['difficult_intermediate_min'] = np.amin(np.array(difficult_intermediate_viewscount).astype(np.float)) if len(difficult_intermediate_viewscount) > 0 else -1
	developers[developer]['viewscount']['difficult_experienced_min'] = np.amin(np.array(difficult_experienced_viewscount).astype(np.float)) if len(difficult_experienced_viewscount) > 0 else -1

	## Favorites Count
	developers[developer]['favoritecount'] = {}
	developers[developer]['favoritecount']['easy_novice_mean'] = np.mean(np.array(easy_novice_favoritecount).astype(np.float)) if len(easy_novice_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['easy_beginner_mean'] = np.mean(np.array(easy_beginner_favoritecount).astype(np.float)) if len(easy_beginner_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['easy_intermediate_mean'] = np.mean(np.array(easy_intermediate_favoritecount).astype(np.float)) if len(easy_intermediate_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['easy_experienced_mean'] = np.mean(np.array(easy_experienced_favoritecount).astype(np.float)) if len(easy_experienced_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['medium_novice_mean'] = np.mean(np.array(medium_novice_favoritecount).astype(np.float)) if len(medium_novice_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['medium_beginner_mean'] = np.mean(np.array(medium_beginner_favoritecount).astype(np.float)) if len(medium_beginner_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['medium_intermediate_mean'] = np.mean(np.array(medium_intermediate_favoritecount).astype(np.float)) if len(medium_intermediate_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['medium_experienced_mean'] = np.mean(np.array(medium_experienced_favoritecount).astype(np.float)) if len(medium_experienced_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['difficult_novice_mean'] = np.mean(np.array(difficult_novice_favoritecount).astype(np.float)) if len(difficult_novice_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['difficult_beginner_mean'] = np.mean(np.array(difficult_beginner_favoritecount).astype(np.float)) if len(difficult_beginner_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['difficult_intermediate_mean'] = np.mean(np.array(difficult_intermediate_favoritecount).astype(np.float)) if len(difficult_intermediate_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['difficult_experienced_mean'] = np.mean(np.array(difficult_experienced_favoritecount).astype(np.float)) if len(difficult_experienced_favoritecount) > 0 else -1

	developers[developer]['favoritecount']['easy_novice_max'] = np.amax(np.array(easy_novice_favoritecount).astype(np.float)) if len(easy_novice_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['easy_beginner_max'] = np.amax(np.array(easy_beginner_favoritecount).astype(np.float)) if len(easy_beginner_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['easy_intermediate_max'] = np.amax(np.array(easy_intermediate_favoritecount).astype(np.float)) if len(easy_intermediate_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['easy_experienced_max'] = np.amax(np.array(easy_experienced_favoritecount).astype(np.float)) if len(easy_experienced_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['medium_novice_max'] = np.amax(np.array(medium_novice_favoritecount).astype(np.float)) if len(medium_novice_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['medium_beginner_max'] = np.amax(np.array(medium_beginner_favoritecount).astype(np.float)) if len(medium_beginner_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['medium_intermediate_max'] = np.amax(np.array(medium_intermediate_favoritecount).astype(np.float)) if len(medium_intermediate_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['medium_experienced_max'] = np.amax(np.array(medium_experienced_favoritecount).astype(np.float)) if len(medium_experienced_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['difficult_novice_max'] = np.amax(np.array(difficult_novice_favoritecount).astype(np.float)) if len(difficult_novice_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['difficult_beginner_max'] = np.amax(np.array(difficult_beginner_favoritecount).astype(np.float)) if len(difficult_beginner_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['difficult_intermediate_max'] = np.amax(np.array(difficult_intermediate_favoritecount).astype(np.float)) if len(difficult_intermediate_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['difficult_experienced_max'] = np.amax(np.array(difficult_experienced_favoritecount).astype(np.float)) if len(difficult_experienced_favoritecount) > 0 else -1

	developers[developer]['favoritecount']['easy_novice_min'] = np.amin(np.array(easy_novice_favoritecount).astype(np.float)) if len(easy_novice_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['easy_beginner_min'] = np.amin(np.array(easy_beginner_favoritecount).astype(np.float)) if len(easy_beginner_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['easy_intermediate_min'] = np.amin(np.array(easy_intermediate_favoritecount).astype(np.float)) if len(easy_intermediate_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['easy_experienced_min'] = np.amin(np.array(easy_experienced_favoritecount).astype(np.float)) if len(easy_experienced_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['medium_novice_min'] = np.amin(np.array(medium_novice_favoritecount).astype(np.float)) if len(medium_novice_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['medium_beginner_min'] = np.amin(np.array(medium_beginner_favoritecount).astype(np.float)) if len(medium_beginner_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['medium_intermediate_min'] = np.amin(np.array(medium_intermediate_favoritecount).astype(np.float)) if len(medium_intermediate_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['medium_experienced_min'] = np.amin(np.array(medium_experienced_favoritecount).astype(np.float)) if len(medium_experienced_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['difficult_novice_min'] = np.amin(np.array(difficult_novice_favoritecount).astype(np.float)) if len(difficult_novice_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['difficult_beginner_min'] = np.amin(np.array(difficult_beginner_favoritecount).astype(np.float)) if len(difficult_beginner_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['difficult_intermediate_min'] = np.amin(np.array(difficult_intermediate_favoritecount).astype(np.float)) if len(difficult_intermediate_favoritecount) > 0 else -1
	developers[developer]['favoritecount']['difficult_experienced_min'] = np.amin(np.array(difficult_experienced_favoritecount).astype(np.float)) if len(difficult_experienced_viewscount) > 0 else -1

for developer in developers:
	# Subjectivity 
	## Mean Value
	if(developers[developer]['subjectivity']['easy_novice_mean'] != -1):
		easy['novice']['subjectivity'].append(developers[developer]['subjectivity']['easy_novice_mean'])
	if(developers[developer]['subjectivity']['easy_beginner_mean'] != -1):
		easy['beginner']['subjectivity'].append(developers[developer]['subjectivity']['easy_beginner_mean'])
	if(developers[developer]['subjectivity']['easy_intermediate_mean'] != -1):
		easy['intermediate']['subjectivity'].append(developers[developer]['subjectivity']['easy_intermediate_mean'])
	if(developers[developer]['subjectivity']['easy_experienced_mean'] != -1):
		easy['experienced']['subjectivity'].append(developers[developer]['subjectivity']['easy_experienced_mean'])
	
	if(developers[developer]['subjectivity']['medium_novice_mean'] != -1):
		medium['novice']['subjectivity'].append(developers[developer]['subjectivity']['medium_novice_mean'])
	if(developers[developer]['subjectivity']['medium_beginner_mean'] != -1):
		medium['beginner']['subjectivity'].append(developers[developer]['subjectivity']['medium_beginner_mean'])
	if(developers[developer]['subjectivity']['medium_intermediate_mean'] != -1):
		medium['intermediate']['subjectivity'].append(developers[developer]['subjectivity']['medium_intermediate_mean'])
	if(developers[developer]['subjectivity']['medium_experienced_mean'] != -1):
		medium['experienced']['subjectivity'].append(developers[developer]['subjectivity']['medium_experienced_mean'])
	
	if(developers[developer]['subjectivity']['difficult_novice_mean'] != -1):
		difficult['novice']['subjectivity'].append(developers[developer]['subjectivity']['difficult_novice_mean'])
	if(developers[developer]['subjectivity']['difficult_beginner_mean'] != -1):
		difficult['beginner']['subjectivity'].append(developers[developer]['subjectivity']['difficult_beginner_mean'])
	if(developers[developer]['subjectivity']['difficult_intermediate_mean'] != -1):
		difficult['intermediate']['subjectivity'].append(developers[developer]['subjectivity']['difficult_intermediate_mean'])
	if(developers[developer]['subjectivity']['difficult_experienced_mean'] != -1):
		difficult['experienced']['subjectivity'].append(developers[developer]['subjectivity']['difficult_experienced_mean'])

	
	## Polarity
	if(developers[developer]['polarity']['easy_novice_mean'] != -1):
		easy['novice']['polarity'].append(developers[developer]['polarity']['easy_novice_mean'])
	if(developers[developer]['polarity']['easy_beginner_mean'] != -1):
		easy['beginner']['polarity'].append(developers[developer]['polarity']['easy_beginner_mean'])
	if(developers[developer]['polarity']['easy_intermediate_mean'] != -1):
		easy['intermediate']['polarity'].append(developers[developer]['polarity']['easy_intermediate_mean'])
	if(developers[developer]['polarity']['easy_experienced_mean'] != -1):
		easy['experienced']['polarity'].append(developers[developer]['polarity']['easy_experienced_mean'])

	if(developers[developer]['polarity']['medium_novice_mean'] != -1):
		medium['novice']['polarity'].append(developers[developer]['polarity']['medium_novice_mean'])
	if(developers[developer]['polarity']['medium_beginner_mean'] != -1):
		medium['beginner']['polarity'].append(developers[developer]['polarity']['medium_beginner_mean'])
	if(developers[developer]['polarity']['medium_intermediate_mean'] != -1):
		medium['intermediate']['polarity'].append(developers[developer]['polarity']['medium_intermediate_mean'])
	if(developers[developer]['polarity']['medium_experienced_mean'] != -1):
		medium['experienced']['polarity'].append(developers[developer]['polarity']['medium_experienced_mean'])
	
	if(developers[developer]['polarity']['difficult_novice_mean'] != -1):
		difficult['novice']['polarity'].append(developers[developer]['polarity']['difficult_novice_mean'])
	if(developers[developer]['polarity']['difficult_beginner_mean'] != -1):
		difficult['beginner']['polarity'].append(developers[developer]['polarity']['difficult_beginner_mean'])
	if(developers[developer]['polarity']['difficult_intermediate_mean'] != -1):
		difficult['intermediate']['polarity'].append(developers[developer]['polarity']['difficult_intermediate_mean'])
	if(developers[developer]['polarity']['difficult_experienced_mean'] != -1):
		difficult['experienced']['polarity'].append(developers[developer]['polarity']['difficult_experienced_mean'])
	
	## Word Count
	if(developers[developer]['word_count']['easy_novice_mean'] != -1):
		easy['novice']['word_count'].append(developers[developer]['word_count']['easy_novice_mean'])
	if(developers[developer]['word_count']['easy_beginner_mean'] != -1):
		easy['beginner']['word_count'].append(developers[developer]['word_count']['easy_beginner_mean'])
	if(developers[developer]['word_count']['easy_intermediate_mean'] != -1):
		easy['intermediate']['word_count'].append(developers[developer]['word_count']['easy_intermediate_mean'])
	if(developers[developer]['word_count']['easy_experienced_mean'] != -1):
		easy['experienced']['word_count'].append(developers[developer]['word_count']['easy_experienced_mean'])
	
	if(developers[developer]['word_count']['medium_novice_mean'] != -1):
		medium['novice']['word_count'].append(developers[developer]['word_count']['medium_novice_mean'])
	if(developers[developer]['word_count']['medium_beginner_mean'] != -1):
		medium['beginner']['word_count'].append(developers[developer]['word_count']['medium_beginner_mean'])
	if(developers[developer]['word_count']['medium_intermediate_mean'] != -1):
		medium['intermediate']['word_count'].append(developers[developer]['word_count']['medium_intermediate_mean'])
	if(developers[developer]['word_count']['medium_experienced_mean'] != -1):
		medium['experienced']['word_count'].append(developers[developer]['word_count']['medium_experienced_mean'])
	
	if(developers[developer]['word_count']['difficult_novice_mean'] != -1):
		difficult['novice']['word_count'].append(developers[developer]['word_count']['difficult_novice_mean'])
	if(developers[developer]['word_count']['difficult_beginner_mean'] != -1):
		difficult['beginner']['word_count'].append(developers[developer]['word_count']['difficult_beginner_mean'])
	if(developers[developer]['word_count']['difficult_intermediate_mean'] != -1):
		difficult['intermediate']['word_count'].append(developers[developer]['word_count']['difficult_intermediate_mean'])
	if(developers[developer]['word_count']['difficult_experienced_mean'] != -1):
		difficult['experienced']['word_count'].append(developers[developer]['word_count']['difficult_experienced_mean'])

	## Score
	if(developers[developer]['score']['easy_novice_mean'] != -1):
		easy['novice']['score'].append(developers[developer]['score']['easy_novice_mean'])
	if(developers[developer]['score']['easy_beginner_mean'] != -1):
		easy['beginner']['score'].append(developers[developer]['score']['easy_beginner_mean'])
	if(developers[developer]['score']['easy_intermediate_mean'] != -1):
		easy['intermediate']['score'].append(developers[developer]['score']['easy_intermediate_mean'])
	if(developers[developer]['score']['easy_experienced_mean'] != -1):
		easy['experienced']['score'].append(developers[developer]['score']['easy_experienced_mean'])
	
	if(developers[developer]['score']['medium_novice_mean'] != -1):
		medium['novice']['score'].append(developers[developer]['score']['medium_novice_mean'])
	if(developers[developer]['score']['medium_beginner_mean'] != -1):
		medium['beginner']['score'].append(developers[developer]['score']['medium_beginner_mean'])
	if(developers[developer]['score']['medium_intermediate_mean'] != -1):
		medium['intermediate']['score'].append(developers[developer]['score']['medium_intermediate_mean'])
	if(developers[developer]['score']['medium_experienced_mean'] != -1):
		medium['experienced']['score'].append(developers[developer]['score']['medium_experienced_mean'])
	
	if(developers[developer]['score']['difficult_novice_mean'] != -1):
		difficult['novice']['score'].append(developers[developer]['score']['difficult_novice_mean'])
	if(developers[developer]['score']['difficult_beginner_mean'] != -1):
		difficult['beginner']['score'].append(developers[developer]['score']['difficult_beginner_mean'])
	if(developers[developer]['score']['difficult_intermediate_mean'] != -1):
		difficult['intermediate']['score'].append(developers[developer]['score']['difficult_intermediate_mean'])
	if(developers[developer]['score']['difficult_experienced_mean'] != -1):
		difficult['experienced']['score'].append(developers[developer]['score']['difficult_experienced_mean'])

	## Views Count
	if(developers[developer]['viewscount']['easy_novice_mean'] != -1):
		easy['novice']['viewscount'].append(developers[developer]['viewscount']['easy_novice_mean'])
	if(developers[developer]['viewscount']['easy_beginner_mean'] != -1):
		easy['beginner']['viewscount'].append(developers[developer]['viewscount']['easy_beginner_mean'])
	if(developers[developer]['viewscount']['easy_intermediate_mean'] != -1):
		easy['intermediate']['viewscount'].append(developers[developer]['viewscount']['easy_intermediate_mean'])
	if(developers[developer]['viewscount']['easy_experienced_mean'] != -1):
		easy['experienced']['viewscount'].append(developers[developer]['viewscount']['easy_experienced_mean'])
	
	if(developers[developer]['viewscount']['medium_novice_mean'] != -1):
		medium['novice']['viewscount'].append(developers[developer]['viewscount']['medium_novice_mean'])
	if(developers[developer]['viewscount']['medium_beginner_mean'] != -1):
		medium['beginner']['viewscount'].append(developers[developer]['viewscount']['medium_beginner_mean'])
	if(developers[developer]['viewscount']['medium_intermediate_mean'] != -1):
		medium['intermediate']['viewscount'].append(developers[developer]['viewscount']['medium_intermediate_mean'])
	if(developers[developer]['viewscount']['medium_experienced_mean'] != -1):
		medium['experienced']['viewscount'].append(developers[developer]['viewscount']['medium_experienced_mean'])
	
	if(developers[developer]['viewscount']['difficult_novice_mean'] != -1):
		difficult['novice']['viewscount'].append(developers[developer]['viewscount']['difficult_novice_mean'])
	if(developers[developer]['viewscount']['difficult_beginner_mean'] != -1):
		difficult['beginner']['viewscount'].append(developers[developer]['viewscount']['difficult_beginner_mean'])
	if(developers[developer]['viewscount']['difficult_intermediate_mean'] != -1):
		difficult['intermediate']['viewscount'].append(developers[developer]['viewscount']['difficult_intermediate_mean'])
	if(developers[developer]['viewscount']['difficult_experienced_mean'] != -1):
		difficult['experienced']['viewscount'].append(developers[developer]['viewscount']['difficult_experienced_mean'])

	## Favorite Count
	if(developers[developer]['favoritecount']['easy_novice_mean'] != -1):
		easy['novice']['favoritecount'].append(developers[developer]['favoritecount']['easy_novice_mean'])
	if(developers[developer]['favoritecount']['easy_beginner_mean'] != -1):
		easy['beginner']['favoritecount'].append(developers[developer]['favoritecount']['easy_beginner_mean'])
	if(developers[developer]['favoritecount']['easy_intermediate_mean'] != -1):
		easy['intermediate']['favoritecount'].append(developers[developer]['favoritecount']['easy_intermediate_mean'])
	if(developers[developer]['favoritecount']['easy_experienced_mean'] != -1):
		easy['experienced']['favoritecount'].append(developers[developer]['favoritecount']['easy_experienced_mean'])
	
	if(developers[developer]['favoritecount']['medium_novice_mean'] != -1):
		medium['novice']['favoritecount'].append(developers[developer]['favoritecount']['medium_novice_mean'])
	if(developers[developer]['favoritecount']['medium_beginner_mean'] != -1):
		medium['beginner']['favoritecount'].append(developers[developer]['favoritecount']['medium_beginner_mean'])
	if(developers[developer]['favoritecount']['medium_intermediate_mean'] != -1):
		medium['intermediate']['favoritecount'].append(developers[developer]['favoritecount']['medium_intermediate_mean'])
	if(developers[developer]['favoritecount']['medium_experienced_mean'] != -1):
		medium['experienced']['favoritecount'].append(developers[developer]['favoritecount']['medium_experienced_mean'])
	
	if(developers[developer]['favoritecount']['difficult_novice_mean'] != -1):
		difficult['novice']['favoritecount'].append(developers[developer]['favoritecount']['difficult_novice_mean'])
	if(developers[developer]['favoritecount']['difficult_beginner_mean'] != -1):
		difficult['beginner']['favoritecount'].append(developers[developer]['favoritecount']['difficult_beginner_mean'])
	if(developers[developer]['favoritecount']['difficult_intermediate_mean'] != -1):
		difficult['intermediate']['favoritecount'].append(developers[developer]['favoritecount']['difficult_intermediate_mean'])
	if(developers[developer]['favoritecount']['difficult_experienced_mean'] != -1):
		difficult['experienced']['favoritecount'].append(developers[developer]['favoritecount']['difficult_experienced_mean'])

print('Subjectivity buckets Mean Value')
print('Easy')
print('------')
print('Novice ',np.mean(np.array(easy['novice']['subjectivity']).astype(np.float)))
print('Beginner ',np.mean(np.array(easy['beginner']['subjectivity']).astype(np.float)))
print('Intermediate ',np.mean(np.array(easy['intermediate']['subjectivity']).astype(np.float)))
print('Experienced ',np.mean(np.array(easy['experienced']['subjectivity']).astype(np.float)))
print('\n')
print('Medium')
print('------')
print('Novice ',np.mean(np.array(medium['novice']['subjectivity']).astype(np.float)))
print('Beginner ',np.mean(np.array(medium['beginner']['subjectivity']).astype(np.float)))
print('Intermediate ',np.mean(np.array(medium['intermediate']['subjectivity']).astype(np.float)))
print('Experienced ',np.mean(np.array(medium['experienced']['subjectivity']).astype(np.float)))
print('\n')
print('Difficult')
print('------')
print('Novice ',np.mean(np.array(difficult['novice']['subjectivity']).astype(np.float)))
print('Beginner ',np.mean(np.array(difficult['beginner']['subjectivity']).astype(np.float)))
print('Intermediate ',np.mean(np.array(difficult['intermediate']['subjectivity']).astype(np.float)))
print('Experienced ',np.mean(np.array(difficult['experienced']['subjectivity']).astype(np.float)))
print('\n\n')


print('Polarity buckets Mean Value')
print('Easy')
print('------')
print('Novice ',np.mean(np.array(easy['novice']['polarity']).astype(np.float)))
print('Beginner ',np.mean(np.array(easy['beginner']['polarity']).astype(np.float)))
print('Intermediate ',np.mean(np.array(easy['intermediate']['polarity']).astype(np.float)))
print('Experienced ',np.mean(np.array(easy['experienced']['polarity']).astype(np.float)))
print('\n')
print('Medium')
print('------')
print('Novice ',np.mean(np.array(medium['novice']['polarity']).astype(np.float)))
print('Beginner ',np.mean(np.array(medium['beginner']['polarity']).astype(np.float)))
print('Intermediate ',np.mean(np.array(medium['intermediate']['polarity']).astype(np.float)))
print('Experienced ',np.mean(np.array(medium['experienced']['polarity']).astype(np.float)))
print('\n')
print('Difficult')
print('------')
print('Novice ',np.mean(np.array(difficult['novice']['polarity']).astype(np.float)))
print('Beginner ',np.mean(np.array(difficult['beginner']['polarity']).astype(np.float)))
print('Intermediate ',np.mean(np.array(difficult['intermediate']['polarity']).astype(np.float)))
print('Experienced ',np.mean(np.array(difficult['experienced']['polarity']).astype(np.float)))
print('\n\n')

print('Word Counts buckets Mean Value')
print('Easy')
print('------')
print('Novice ',np.mean(np.array(easy['novice']['word_count']).astype(np.float)))
print('Beginner ',np.mean(np.array(easy['beginner']['word_count']).astype(np.float)))
print('Intermediate ',np.mean(np.array(easy['intermediate']['word_count']).astype(np.float)))
print('Experienced ',np.mean(np.array(easy['experienced']['word_count']).astype(np.float)))
print('\n')
print('Medium')
print('------')
print('Novice ',np.mean(np.array(medium['novice']['word_count']).astype(np.float)))
print('Beginner ',np.mean(np.array(medium['beginner']['word_count']).astype(np.float)))
print('Intermediate ',np.mean(np.array(medium['intermediate']['word_count']).astype(np.float)))
print('Experienced ',np.mean(np.array(medium['experienced']['word_count']).astype(np.float)))
print('\n')
print('Difficult')
print('------')
print('Novice ',np.mean(np.array(difficult['novice']['word_count']).astype(np.float)))
print('Beginner ',np.mean(np.array(difficult['beginner']['word_count']).astype(np.float)))
print('Intermediate ',np.mean(np.array(difficult['intermediate']['word_count']).astype(np.float)))
print('Experienced ',np.mean(np.array(difficult['experienced']['word_count']).astype(np.float)))
print('\n\n')

print('Score buckets Mean Value')
print('Easy')
print('------')
print('Novice ',np.mean(np.array(easy['novice']['score']).astype(np.float)))
print('Beginner ',np.mean(np.array(easy['beginner']['score']).astype(np.float)))
print('Intermediate ',np.mean(np.array(easy['intermediate']['score']).astype(np.float)))
print('Experienced ',np.mean(np.array(easy['experienced']['score']).astype(np.float)))
print('\n')
print('Medium')
print('------')
print('Novice ',np.mean(np.array(medium['novice']['score']).astype(np.float)))
print('Beginner ',np.mean(np.array(medium['beginner']['score']).astype(np.float)))
print('Intermediate ',np.mean(np.array(medium['intermediate']['score']).astype(np.float)))
print('Experienced ',np.mean(np.array(medium['experienced']['score']).astype(np.float)))
print('\n')
print('Difficult')
print('------')
print('Novice ',np.mean(np.array(difficult['novice']['score']).astype(np.float)))
print('Beginner ',np.mean(np.array(difficult['beginner']['score']).astype(np.float)))
print('Intermediate ',np.mean(np.array(difficult['intermediate']['score']).astype(np.float)))
print('Experienced ',np.mean(np.array(difficult['experienced']['score']).astype(np.float)))
print('\n\n')

# print('Subjectivity buckets length')
# print('Easy')
# print('------')
# print('Novice ',len(easy['novice']['subjectivity']))
# print('Beginner ',len(easy['beginner']['subjectivity']))
# print('Intermediate ',len(easy['intermediate']['subjectivity']))
# print('Experienced ',len(easy['experienced']['subjectivity']))
# print('\n')
# print('Medium')
# print('------')
# print('Novice ',len(medium['novice']['subjectivity']))
# print('Beginner ',len(medium['beginner']['subjectivity']))
# print('Intermediate ',len(medium['intermediate']['subjectivity']))
# print('Experienced ',len(medium['experienced']['subjectivity']))
# print('\n')
# print('Difficult')
# print('------')
# print('Novice ',len(difficult['novice']['subjectivity']))
# print('Beginner ',len(difficult['beginner']['subjectivity']))
# print('Intermediate ',len(difficult['intermediate']['subjectivity']))
# print('Experienced ',len(difficult['experienced']['subjectivity']))
# print('\n\n')

# print('Polarity buckets length')
# print('Easy')
# print('------')
# print('Novice ',len(easy['novice']['polarity']))
# print('Beginner ',len(easy['beginner']['polarity']))
# print('Intermediate ',len(easy['intermediate']['polarity']))
# print('Experienced ',len(easy['experienced']['polarity']))
# print('\n')
# print('Medium')
# print('------')
# print('Novice ',len(medium['novice']['polarity']))
# print('Beginner ',len(medium['beginner']['polarity']))
# print('Intermediate ',len(medium['intermediate']['polarity']))
# print('Experienced ',len(medium['experienced']['polarity']))
# print('\n')
# print('Difficult')
# print('------')
# print('Novice ',len(difficult['novice']['polarity']))
# print('Beginner ',len(difficult['beginner']['polarity']))
# print('Intermediate ',len(difficult['intermediate']['polarity']))
# print('Experienced ',len(difficult['experienced']['polarity']))
# print('\n\n')

# print('Word Count buckets length')
# print('Easy')
# print('------')
# print('Novice ',len(easy['novice']['word_count']))
# print('Beginner ',len(easy['beginner']['word_count']))
# print('Intermediate ',len(easy['intermediate']['word_count']))
# print('Experienced ',len(easy['experienced']['word_count']))
# print('\n')
# print('Medium')
# print('------')
# print('Novice ',len(medium['novice']['word_count']))
# print('Beginner ',len(medium['beginner']['word_count']))
# print('Intermediate ',len(medium['intermediate']['word_count']))
# print('Experienced ',len(medium['experienced']['word_count']))
# print('\n')
# print('Difficult')
# print('------')
# print('Novice ',len(difficult['novice']['word_count']))
# print('Beginner ',len(difficult['beginner']['word_count']))
# print('Intermediate ',len(difficult['intermediate']['word_count']))
# print('Experienced ',len(difficult['experienced']['word_count']))
# print('\n')


# manwhitney(easy, medium, difficult)

analysis = Stats()
print('\t On Mean Value \n')
# analysis.manwhitneytest(easy, medium, difficult)


#### On Max Values #####
for developer in developers:
	# Subjectivity 
	if(developers[developer]['subjectivity']['easy_novice_max'] != -1):
		easy['novice']['subjectivity'].append(developers[developer]['subjectivity']['easy_novice_max'])
	if(developers[developer]['subjectivity']['easy_beginner_max'] != -1):
		easy['beginner']['subjectivity'].append(developers[developer]['subjectivity']['easy_beginner_max'])
	if(developers[developer]['subjectivity']['easy_intermediate_max'] != -1):
		easy['intermediate']['subjectivity'].append(developers[developer]['subjectivity']['easy_intermediate_max'])
	if(developers[developer]['subjectivity']['easy_experienced_max'] != -1):
		easy['experienced']['subjectivity'].append(developers[developer]['subjectivity']['easy_experienced_max'])
	
	if(developers[developer]['subjectivity']['medium_novice_max'] != -1):
		medium['novice']['subjectivity'].append(developers[developer]['subjectivity']['medium_novice_max'])
	if(developers[developer]['subjectivity']['medium_beginner_max'] != -1):
		medium['beginner']['subjectivity'].append(developers[developer]['subjectivity']['medium_beginner_max'])
	if(developers[developer]['subjectivity']['medium_intermediate_max'] != -1):
		medium['intermediate']['subjectivity'].append(developers[developer]['subjectivity']['medium_intermediate_max'])
	if(developers[developer]['subjectivity']['medium_experienced_max'] != -1):
		medium['experienced']['subjectivity'].append(developers[developer]['subjectivity']['medium_experienced_max'])
	
	if(developers[developer]['subjectivity']['difficult_novice_max'] != -1):
		difficult['novice']['subjectivity'].append(developers[developer]['subjectivity']['difficult_novice_max'])
	if(developers[developer]['subjectivity']['difficult_beginner_max'] != -1):
		difficult['beginner']['subjectivity'].append(developers[developer]['subjectivity']['difficult_beginner_max'])
	if(developers[developer]['subjectivity']['difficult_intermediate_max'] != -1):
		difficult['intermediate']['subjectivity'].append(developers[developer]['subjectivity']['difficult_intermediate_max'])
	if(developers[developer]['subjectivity']['difficult_experienced_max'] != -1):
		difficult['experienced']['subjectivity'].append(developers[developer]['subjectivity']['difficult_experienced_max'])

	## Polarity
	if(developers[developer]['polarity']['easy_novice_max'] != -1):
		easy['novice']['polarity'].append(developers[developer]['polarity']['easy_novice_max'])
	if(developers[developer]['polarity']['easy_beginner_max'] != -1):
		easy['beginner']['polarity'].append(developers[developer]['polarity']['easy_beginner_max'])
	if(developers[developer]['polarity']['easy_intermediate_max'] != -1):
		easy['intermediate']['polarity'].append(developers[developer]['polarity']['easy_intermediate_max'])
	if(developers[developer]['polarity']['easy_experienced_max'] != -1):
		easy['experienced']['polarity'].append(developers[developer]['polarity']['easy_experienced_max'])

	if(developers[developer]['polarity']['medium_novice_max'] != -1):
		medium['novice']['polarity'].append(developers[developer]['polarity']['medium_novice_max'])
	if(developers[developer]['polarity']['medium_beginner_max'] != -1):
		medium['beginner']['polarity'].append(developers[developer]['polarity']['medium_beginner_max'])
	if(developers[developer]['polarity']['medium_intermediate_max'] != -1):
		medium['intermediate']['polarity'].append(developers[developer]['polarity']['medium_intermediate_max'])
	if(developers[developer]['polarity']['medium_experienced_max'] != -1):
		medium['experienced']['polarity'].append(developers[developer]['polarity']['medium_experienced_max'])
	
	if(developers[developer]['polarity']['difficult_novice_max'] != -1):
		difficult['novice']['polarity'].append(developers[developer]['polarity']['difficult_novice_max'])
	if(developers[developer]['polarity']['difficult_beginner_max'] != -1):
		difficult['beginner']['polarity'].append(developers[developer]['polarity']['difficult_beginner_max'])
	if(developers[developer]['polarity']['difficult_intermediate_max'] != -1):
		difficult['intermediate']['polarity'].append(developers[developer]['polarity']['difficult_intermediate_max'])
	if(developers[developer]['polarity']['difficult_experienced_max'] != -1):
		difficult['experienced']['polarity'].append(developers[developer]['polarity']['difficult_experienced_max'])
	
	# ## Word Count
	if(developers[developer]['word_count']['easy_novice_max'] != -1):
		easy['novice']['word_count'].append(developers[developer]['word_count']['easy_novice_max'])
	if(developers[developer]['word_count']['easy_beginner_max'] != -1):
		easy['beginner']['word_count'].append(developers[developer]['word_count']['easy_beginner_max'])
	if(developers[developer]['word_count']['easy_intermediate_max'] != -1):
		easy['intermediate']['word_count'].append(developers[developer]['word_count']['easy_intermediate_max'])
	if(developers[developer]['word_count']['easy_experienced_max'] != -1):
		easy['experienced']['word_count'].append(developers[developer]['word_count']['easy_experienced_max'])
	
	if(developers[developer]['word_count']['medium_novice_max'] != -1):
		medium['novice']['word_count'].append(developers[developer]['word_count']['medium_novice_max'])
	if(developers[developer]['word_count']['medium_beginner_max'] != -1):
		medium['beginner']['word_count'].append(developers[developer]['word_count']['medium_beginner_max'])
	if(developers[developer]['word_count']['medium_intermediate_max'] != -1):
		medium['intermediate']['word_count'].append(developers[developer]['word_count']['medium_intermediate_max'])
	if(developers[developer]['word_count']['medium_experienced_max'] != -1):
		medium['experienced']['word_count'].append(developers[developer]['word_count']['medium_experienced_max'])
	
	if(developers[developer]['word_count']['difficult_novice_max'] != -1):
		difficult['novice']['word_count'].append(developers[developer]['word_count']['difficult_novice_max'])
	if(developers[developer]['word_count']['difficult_beginner_max'] != -1):
		difficult['beginner']['word_count'].append(developers[developer]['word_count']['difficult_beginner_max'])
	if(developers[developer]['word_count']['difficult_intermediate_max'] != -1):
		difficult['intermediate']['word_count'].append(developers[developer]['word_count']['difficult_intermediate_max'])
	if(developers[developer]['word_count']['difficult_experienced_max'] != -1):
		difficult['experienced']['word_count'].append(developers[developer]['word_count']['difficult_experienced_max'])

	## Score
	if(developers[developer]['score']['easy_novice_max'] != -1):
		easy['novice']['score'].append(developers[developer]['score']['easy_novice_max'])
	if(developers[developer]['score']['easy_beginner_max'] != -1):
		easy['beginner']['score'].append(developers[developer]['score']['easy_beginner_max'])
	if(developers[developer]['score']['easy_intermediate_max'] != -1):
		easy['intermediate']['score'].append(developers[developer]['score']['easy_intermediate_max'])
	if(developers[developer]['score']['easy_experienced_max'] != -1):
		easy['experienced']['score'].append(developers[developer]['score']['easy_experienced_max'])
	
	if(developers[developer]['score']['medium_novice_max'] != -1):
		medium['novice']['score'].append(developers[developer]['score']['medium_novice_max'])
	if(developers[developer]['score']['medium_beginner_max'] != -1):
		medium['beginner']['score'].append(developers[developer]['score']['medium_beginner_max'])
	if(developers[developer]['score']['medium_intermediate_max'] != -1):
		medium['intermediate']['score'].append(developers[developer]['score']['medium_intermediate_max'])
	if(developers[developer]['score']['medium_experienced_max'] != -1):
		medium['experienced']['score'].append(developers[developer]['score']['medium_experienced_max'])
	
	if(developers[developer]['score']['difficult_novice_max'] != -1):
		difficult['novice']['score'].append(developers[developer]['score']['difficult_novice_max'])
	if(developers[developer]['score']['difficult_beginner_max'] != -1):
		difficult['beginner']['score'].append(developers[developer]['score']['difficult_beginner_max'])
	if(developers[developer]['score']['difficult_intermediate_max'] != -1):
		difficult['intermediate']['score'].append(developers[developer]['score']['difficult_intermediate_max'])
	if(developers[developer]['score']['difficult_experienced_max'] != -1):
		difficult['experienced']['score'].append(developers[developer]['score']['difficult_experienced_max'])

	## Views Count
	if(developers[developer]['viewscount']['easy_novice_max'] != -1):
		easy['novice']['viewscount'].append(developers[developer]['viewscount']['easy_novice_max'])
	if(developers[developer]['viewscount']['easy_beginner_max'] != -1):
		easy['beginner']['viewscount'].append(developers[developer]['viewscount']['easy_beginner_max'])
	if(developers[developer]['viewscount']['easy_intermediate_max'] != -1):
		easy['intermediate']['viewscount'].append(developers[developer]['viewscount']['easy_intermediate_max'])
	if(developers[developer]['viewscount']['easy_experienced_max'] != -1):
		easy['experienced']['viewscount'].append(developers[developer]['viewscount']['easy_experienced_max'])
	
	if(developers[developer]['viewscount']['medium_novice_max'] != -1):
		medium['novice']['viewscount'].append(developers[developer]['viewscount']['medium_novice_max'])
	if(developers[developer]['viewscount']['medium_beginner_max'] != -1):
		medium['beginner']['viewscount'].append(developers[developer]['viewscount']['medium_beginner_max'])
	if(developers[developer]['viewscount']['medium_intermediate_max'] != -1):
		medium['intermediate']['viewscount'].append(developers[developer]['viewscount']['medium_intermediate_max'])
	if(developers[developer]['viewscount']['medium_experienced_max'] != -1):
		medium['experienced']['viewscount'].append(developers[developer]['viewscount']['medium_experienced_max'])
	
	if(developers[developer]['viewscount']['difficult_novice_max'] != -1):
		difficult['novice']['viewscount'].append(developers[developer]['viewscount']['difficult_novice_max'])
	if(developers[developer]['viewscount']['difficult_beginner_max'] != -1):
		difficult['beginner']['viewscount'].append(developers[developer]['viewscount']['difficult_beginner_max'])
	if(developers[developer]['viewscount']['difficult_intermediate_max'] != -1):
		difficult['intermediate']['viewscount'].append(developers[developer]['viewscount']['difficult_intermediate_max'])
	if(developers[developer]['viewscount']['difficult_experienced_max'] != -1):
		difficult['experienced']['viewscount'].append(developers[developer]['viewscount']['difficult_experienced_max'])

	## Favorite Count
	if(developers[developer]['favoritecount']['easy_novice_max'] != -1):
		easy['novice']['favoritecount'].append(developers[developer]['favoritecount']['easy_novice_max'])
	if(developers[developer]['favoritecount']['easy_beginner_max'] != -1):
		easy['beginner']['favoritecount'].append(developers[developer]['favoritecount']['easy_beginner_max'])
	if(developers[developer]['favoritecount']['easy_intermediate_max'] != -1):
		easy['intermediate']['favoritecount'].append(developers[developer]['favoritecount']['easy_intermediate_max'])
	if(developers[developer]['favoritecount']['easy_experienced_max'] != -1):
		easy['experienced']['favoritecount'].append(developers[developer]['favoritecount']['easy_experienced_max'])
	
	if(developers[developer]['favoritecount']['medium_novice_max'] != -1):
		medium['novice']['favoritecount'].append(developers[developer]['favoritecount']['medium_novice_max'])
	if(developers[developer]['favoritecount']['medium_beginner_max'] != -1):
		medium['beginner']['favoritecount'].append(developers[developer]['favoritecount']['medium_beginner_max'])
	if(developers[developer]['favoritecount']['medium_intermediate_max'] != -1):
		medium['intermediate']['favoritecount'].append(developers[developer]['favoritecount']['medium_intermediate_max'])
	if(developers[developer]['favoritecount']['medium_experienced_max'] != -1):
		medium['experienced']['favoritecount'].append(developers[developer]['favoritecount']['medium_experienced_max'])
	
	if(developers[developer]['favoritecount']['difficult_novice_max'] != -1):
		difficult['novice']['favoritecount'].append(developers[developer]['favoritecount']['difficult_novice_max'])
	if(developers[developer]['favoritecount']['difficult_beginner_max'] != -1):
		difficult['beginner']['favoritecount'].append(developers[developer]['favoritecount']['difficult_beginner_max'])
	if(developers[developer]['favoritecount']['difficult_intermediate_max'] != -1):
		difficult['intermediate']['favoritecount'].append(developers[developer]['favoritecount']['difficult_intermediate_max'])
	if(developers[developer]['favoritecount']['difficult_experienced_max'] != -1):
		difficult['experienced']['favoritecount'].append(developers[developer]['favoritecount']['difficult_experienced_max'])

print('Subjectivity buckets Mean Value')
print('Easy')
print('------')
print('Novice ',np.mean(np.array(easy['novice']['subjectivity']).astype(np.float)))
print('Beginner ',np.mean(np.array(easy['beginner']['subjectivity']).astype(np.float)))
print('Intermediate ',np.mean(np.array(easy['intermediate']['subjectivity']).astype(np.float)))
print('Experienced ',np.mean(np.array(easy['experienced']['subjectivity']).astype(np.float)))
print('\n')
print('Medium')
print('------')
print('Novice ',np.mean(np.array(medium['novice']['subjectivity']).astype(np.float)))
print('Beginner ',np.mean(np.array(medium['beginner']['subjectivity']).astype(np.float)))
print('Intermediate ',np.mean(np.array(medium['intermediate']['subjectivity']).astype(np.float)))
print('Experienced ',np.mean(np.array(medium['experienced']['subjectivity']).astype(np.float)))
print('\n')
print('Difficult')
print('------')
print('Novice ',np.mean(np.array(difficult['novice']['subjectivity']).astype(np.float)))
print('Beginner ',np.mean(np.array(difficult['beginner']['subjectivity']).astype(np.float)))
print('Intermediate ',np.mean(np.array(difficult['intermediate']['subjectivity']).astype(np.float)))
print('Experienced ',np.mean(np.array(difficult['experienced']['subjectivity']).astype(np.float)))
print('\n\n')


print('Polarity buckets Mean Value')
print('Easy')
print('------')
print('Novice ',np.mean(np.array(easy['novice']['polarity']).astype(np.float)))
print('Beginner ',np.mean(np.array(easy['beginner']['polarity']).astype(np.float)))
print('Intermediate ',np.mean(np.array(easy['intermediate']['polarity']).astype(np.float)))
print('Experienced ',np.mean(np.array(easy['experienced']['polarity']).astype(np.float)))
print('\n')
print('Medium')
print('------')
print('Novice ',np.mean(np.array(medium['novice']['polarity']).astype(np.float)))
print('Beginner ',np.mean(np.array(medium['beginner']['polarity']).astype(np.float)))
print('Intermediate ',np.mean(np.array(medium['intermediate']['polarity']).astype(np.float)))
print('Experienced ',np.mean(np.array(medium['experienced']['polarity']).astype(np.float)))
print('\n')
print('Difficult')
print('------')
print('Novice ',np.mean(np.array(difficult['novice']['polarity']).astype(np.float)))
print('Beginner ',np.mean(np.array(difficult['beginner']['polarity']).astype(np.float)))
print('Intermediate ',np.mean(np.array(difficult['intermediate']['polarity']).astype(np.float)))
print('Experienced ',np.mean(np.array(difficult['experienced']['polarity']).astype(np.float)))
print('\n\n')

print('Word Counts buckets Mean Value')
print('Easy')
print('------')
print('Novice ',np.mean(np.array(easy['novice']['word_count']).astype(np.float)))
print('Beginner ',np.mean(np.array(easy['beginner']['word_count']).astype(np.float)))
print('Intermediate ',np.mean(np.array(easy['intermediate']['word_count']).astype(np.float)))
print('Experienced ',np.mean(np.array(easy['experienced']['word_count']).astype(np.float)))
print('\n')
print('Medium')
print('------')
print('Novice ',np.mean(np.array(medium['novice']['word_count']).astype(np.float)))
print('Beginner ',np.mean(np.array(medium['beginner']['word_count']).astype(np.float)))
print('Intermediate ',np.mean(np.array(medium['intermediate']['word_count']).astype(np.float)))
print('Experienced ',np.mean(np.array(medium['experienced']['word_count']).astype(np.float)))
print('\n')
print('Difficult')
print('------')
print('Novice ',np.mean(np.array(difficult['novice']['word_count']).astype(np.float)))
print('Beginner ',np.mean(np.array(difficult['beginner']['word_count']).astype(np.float)))
print('Intermediate ',np.mean(np.array(difficult['intermediate']['word_count']).astype(np.float)))
print('Experienced ',np.mean(np.array(difficult['experienced']['word_count']).astype(np.float)))
print('\n\n')

print('Score buckets Mean Value')
print('Easy')
print('------')
print('Novice ',np.mean(np.array(easy['novice']['score']).astype(np.float)))
print('Beginner ',np.mean(np.array(easy['beginner']['score']).astype(np.float)))
print('Intermediate ',np.mean(np.array(easy['intermediate']['score']).astype(np.float)))
print('Experienced ',np.mean(np.array(easy['experienced']['score']).astype(np.float)))
print('\n')
print('Medium')
print('------')
print('Novice ',np.mean(np.array(medium['novice']['score']).astype(np.float)))
print('Beginner ',np.mean(np.array(medium['beginner']['score']).astype(np.float)))
print('Intermediate ',np.mean(np.array(medium['intermediate']['score']).astype(np.float)))
print('Experienced ',np.mean(np.array(medium['experienced']['score']).astype(np.float)))
print('\n')
print('Difficult')
print('------')
print('Novice ',np.mean(np.array(difficult['novice']['score']).astype(np.float)))
print('Beginner ',np.mean(np.array(difficult['beginner']['score']).astype(np.float)))
print('Intermediate ',np.mean(np.array(difficult['intermediate']['score']).astype(np.float)))
print('Experienced ',np.mean(np.array(difficult['experienced']['score']).astype(np.float)))
print('\n\n')

print('\tOn Max Values\n')
# analysis.manwhitneytest(easy, medium, difficult)

#### On Min Values #####
for developer in developers:
	# Subjectivity 
	if(developers[developer]['subjectivity']['easy_novice_min'] != -1):
		easy['novice']['subjectivity'].append(developers[developer]['subjectivity']['easy_novice_min'])
	if(developers[developer]['subjectivity']['easy_beginner_min'] != -1):
		easy['beginner']['subjectivity'].append(developers[developer]['subjectivity']['easy_beginner_min'])
	if(developers[developer]['subjectivity']['easy_intermediate_min'] != -1):
		easy['intermediate']['subjectivity'].append(developers[developer]['subjectivity']['easy_intermediate_min'])
	if(developers[developer]['subjectivity']['easy_experienced_min'] != -1):
		easy['experienced']['subjectivity'].append(developers[developer]['subjectivity']['easy_experienced_min'])
	
	if(developers[developer]['subjectivity']['medium_novice_min'] != -1):
		medium['novice']['subjectivity'].append(developers[developer]['subjectivity']['medium_novice_min'])
	if(developers[developer]['subjectivity']['medium_beginner_min'] != -1):
		medium['beginner']['subjectivity'].append(developers[developer]['subjectivity']['medium_beginner_min'])
	if(developers[developer]['subjectivity']['medium_intermediate_min'] != -1):
		medium['intermediate']['subjectivity'].append(developers[developer]['subjectivity']['medium_intermediate_min'])
	if(developers[developer]['subjectivity']['medium_experienced_min'] != -1):
		medium['experienced']['subjectivity'].append(developers[developer]['subjectivity']['medium_experienced_min'])
	
	if(developers[developer]['subjectivity']['difficult_novice_min'] != -1):
		difficult['novice']['subjectivity'].append(developers[developer]['subjectivity']['difficult_novice_min'])
	if(developers[developer]['subjectivity']['difficult_beginner_min'] != -1):
		difficult['beginner']['subjectivity'].append(developers[developer]['subjectivity']['difficult_beginner_min'])
	if(developers[developer]['subjectivity']['difficult_intermediate_min'] != -1):
		difficult['intermediate']['subjectivity'].append(developers[developer]['subjectivity']['difficult_intermediate_min'])
	if(developers[developer]['subjectivity']['difficult_experienced_min'] != -1):
		difficult['experienced']['subjectivity'].append(developers[developer]['subjectivity']['difficult_experienced_min'])

	## Polarity
	if(developers[developer]['polarity']['easy_novice_min'] != -1):
		easy['novice']['polarity'].append(developers[developer]['polarity']['easy_novice_min'])
	if(developers[developer]['polarity']['easy_beginner_min'] != -1):
		easy['beginner']['polarity'].append(developers[developer]['polarity']['easy_beginner_min'])
	if(developers[developer]['polarity']['easy_intermediate_min'] != -1):
		easy['intermediate']['polarity'].append(developers[developer]['polarity']['easy_intermediate_min'])
	if(developers[developer]['polarity']['easy_experienced_min'] != -1):
		easy['experienced']['polarity'].append(developers[developer]['polarity']['easy_experienced_min'])

	if(developers[developer]['polarity']['medium_novice_min'] != -1):
		medium['novice']['polarity'].append(developers[developer]['polarity']['medium_novice_min'])
	if(developers[developer]['polarity']['medium_beginner_min'] != -1):
		medium['beginner']['polarity'].append(developers[developer]['polarity']['medium_beginner_min'])
	if(developers[developer]['polarity']['medium_intermediate_min'] != -1):
		medium['intermediate']['polarity'].append(developers[developer]['polarity']['medium_intermediate_min'])
	if(developers[developer]['polarity']['medium_experienced_min'] != -1):
		medium['experienced']['polarity'].append(developers[developer]['polarity']['medium_experienced_min'])
	
	if(developers[developer]['polarity']['difficult_novice_min'] != -1):
		difficult['novice']['polarity'].append(developers[developer]['polarity']['difficult_novice_min'])
	if(developers[developer]['polarity']['difficult_beginner_min'] != -1):
		difficult['beginner']['polarity'].append(developers[developer]['polarity']['difficult_beginner_min'])
	if(developers[developer]['polarity']['difficult_intermediate_min'] != -1):
		difficult['intermediate']['polarity'].append(developers[developer]['polarity']['difficult_intermediate_min'])
	if(developers[developer]['polarity']['difficult_experienced_min'] != -1):
		difficult['experienced']['polarity'].append(developers[developer]['polarity']['difficult_experienced_min'])
	
	# ## Word Count
	if(developers[developer]['word_count']['easy_novice_min'] != -1):
		easy['novice']['word_count'].append(developers[developer]['word_count']['easy_novice_min'])
	if(developers[developer]['word_count']['easy_beginner_min'] != -1):
		easy['beginner']['word_count'].append(developers[developer]['word_count']['easy_beginner_min'])
	if(developers[developer]['word_count']['easy_intermediate_min'] != -1):
		easy['intermediate']['word_count'].append(developers[developer]['word_count']['easy_intermediate_min'])
	if(developers[developer]['word_count']['easy_experienced_min'] != -1):
		easy['experienced']['word_count'].append(developers[developer]['word_count']['easy_experienced_min'])
	
	if(developers[developer]['word_count']['medium_novice_min'] != -1):
		medium['novice']['word_count'].append(developers[developer]['word_count']['medium_novice_min'])
	if(developers[developer]['word_count']['medium_beginner_min'] != -1):
		medium['beginner']['word_count'].append(developers[developer]['word_count']['medium_beginner_min'])
	if(developers[developer]['word_count']['medium_intermediate_min'] != -1):
		medium['intermediate']['word_count'].append(developers[developer]['word_count']['medium_intermediate_min'])
	if(developers[developer]['word_count']['medium_experienced_min'] != -1):
		medium['experienced']['word_count'].append(developers[developer]['word_count']['medium_experienced_min'])
	
	if(developers[developer]['word_count']['difficult_novice_min'] != -1):
		difficult['novice']['word_count'].append(developers[developer]['word_count']['difficult_novice_min'])
	if(developers[developer]['word_count']['difficult_beginner_min'] != -1):
		difficult['beginner']['word_count'].append(developers[developer]['word_count']['difficult_beginner_min'])
	if(developers[developer]['word_count']['difficult_intermediate_min'] != -1):
		difficult['intermediate']['word_count'].append(developers[developer]['word_count']['difficult_intermediate_min'])
	if(developers[developer]['word_count']['difficult_experienced_min'] != -1):
		difficult['experienced']['word_count'].append(developers[developer]['word_count']['difficult_experienced_min'])

	## Score
	if(developers[developer]['score']['easy_novice_min'] != -1):
		easy['novice']['score'].append(developers[developer]['score']['easy_novice_min'])
	if(developers[developer]['score']['easy_beginner_min'] != -1):
		easy['beginner']['score'].append(developers[developer]['score']['easy_beginner_min'])
	if(developers[developer]['score']['easy_intermediate_min'] != -1):
		easy['intermediate']['score'].append(developers[developer]['score']['easy_intermediate_min'])
	if(developers[developer]['score']['easy_experienced_min'] != -1):
		easy['experienced']['score'].append(developers[developer]['score']['easy_experienced_min'])
	
	if(developers[developer]['score']['medium_novice_min'] != -1):
		medium['novice']['score'].append(developers[developer]['score']['medium_novice_min'])
	if(developers[developer]['score']['medium_beginner_min'] != -1):
		medium['beginner']['score'].append(developers[developer]['score']['medium_beginner_min'])
	if(developers[developer]['score']['medium_intermediate_min'] != -1):
		medium['intermediate']['score'].append(developers[developer]['score']['medium_intermediate_min'])
	if(developers[developer]['score']['medium_experienced_min'] != -1):
		medium['experienced']['score'].append(developers[developer]['score']['medium_experienced_min'])
	
	if(developers[developer]['score']['difficult_novice_min'] != -1):
		difficult['novice']['score'].append(developers[developer]['score']['difficult_novice_min'])
	if(developers[developer]['score']['difficult_beginner_min'] != -1):
		difficult['beginner']['score'].append(developers[developer]['score']['difficult_beginner_min'])
	if(developers[developer]['score']['difficult_intermediate_min'] != -1):
		difficult['intermediate']['score'].append(developers[developer]['score']['difficult_intermediate_min'])
	if(developers[developer]['score']['difficult_experienced_min'] != -1):
		difficult['experienced']['score'].append(developers[developer]['score']['difficult_experienced_min'])

	## Views Count
	if(developers[developer]['viewscount']['easy_novice_min'] != -1):
		easy['novice']['viewscount'].append(developers[developer]['viewscount']['easy_novice_min'])
	if(developers[developer]['viewscount']['easy_beginner_min'] != -1):
		easy['beginner']['viewscount'].append(developers[developer]['viewscount']['easy_beginner_min'])
	if(developers[developer]['viewscount']['easy_intermediate_min'] != -1):
		easy['intermediate']['viewscount'].append(developers[developer]['viewscount']['easy_intermediate_min'])
	if(developers[developer]['viewscount']['easy_experienced_min'] != -1):
		easy['experienced']['viewscount'].append(developers[developer]['viewscount']['easy_experienced_min'])
	
	if(developers[developer]['viewscount']['medium_novice_min'] != -1):
		medium['novice']['viewscount'].append(developers[developer]['viewscount']['medium_novice_min'])
	if(developers[developer]['viewscount']['medium_beginner_min'] != -1):
		medium['beginner']['viewscount'].append(developers[developer]['viewscount']['medium_beginner_min'])
	if(developers[developer]['viewscount']['medium_intermediate_min'] != -1):
		medium['intermediate']['viewscount'].append(developers[developer]['viewscount']['medium_intermediate_min'])
	if(developers[developer]['viewscount']['medium_experienced_min'] != -1):
		medium['experienced']['viewscount'].append(developers[developer]['viewscount']['medium_experienced_min'])
	
	if(developers[developer]['viewscount']['difficult_novice_min'] != -1):
		difficult['novice']['viewscount'].append(developers[developer]['viewscount']['difficult_novice_min'])
	if(developers[developer]['viewscount']['difficult_beginner_min'] != -1):
		difficult['beginner']['viewscount'].append(developers[developer]['viewscount']['difficult_beginner_min'])
	if(developers[developer]['viewscount']['difficult_intermediate_min'] != -1):
		difficult['intermediate']['viewscount'].append(developers[developer]['viewscount']['difficult_intermediate_min'])
	if(developers[developer]['viewscount']['difficult_experienced_min'] != -1):
		difficult['experienced']['viewscount'].append(developers[developer]['viewscount']['difficult_experienced_min'])

	## Favorite Count
	if(developers[developer]['favoritecount']['easy_novice_min'] != -1):
		easy['novice']['favoritecount'].append(developers[developer]['favoritecount']['easy_novice_min'])
	if(developers[developer]['favoritecount']['easy_beginner_min'] != -1):
		easy['beginner']['favoritecount'].append(developers[developer]['favoritecount']['easy_beginner_min'])
	if(developers[developer]['favoritecount']['easy_intermediate_min'] != -1):
		easy['intermediate']['favoritecount'].append(developers[developer]['favoritecount']['easy_intermediate_min'])
	if(developers[developer]['favoritecount']['easy_experienced_min'] != -1):
		easy['experienced']['favoritecount'].append(developers[developer]['favoritecount']['easy_experienced_min'])
	
	if(developers[developer]['favoritecount']['medium_novice_min'] != -1):
		medium['novice']['favoritecount'].append(developers[developer]['favoritecount']['medium_novice_min'])
	if(developers[developer]['favoritecount']['medium_beginner_min'] != -1):
		medium['beginner']['favoritecount'].append(developers[developer]['favoritecount']['medium_beginner_min'])
	if(developers[developer]['favoritecount']['medium_intermediate_min'] != -1):
		medium['intermediate']['favoritecount'].append(developers[developer]['favoritecount']['medium_intermediate_min'])
	if(developers[developer]['favoritecount']['medium_experienced_min'] != -1):
		medium['experienced']['favoritecount'].append(developers[developer]['favoritecount']['medium_experienced_min'])
	
	if(developers[developer]['favoritecount']['difficult_novice_min'] != -1):
		difficult['novice']['favoritecount'].append(developers[developer]['favoritecount']['difficult_novice_min'])
	if(developers[developer]['favoritecount']['difficult_beginner_min'] != -1):
		difficult['beginner']['favoritecount'].append(developers[developer]['favoritecount']['difficult_beginner_min'])
	if(developers[developer]['favoritecount']['difficult_intermediate_min'] != -1):
		difficult['intermediate']['favoritecount'].append(developers[developer]['favoritecount']['difficult_intermediate_min'])
	if(developers[developer]['favoritecount']['difficult_experienced_min'] != -1):
		difficult['experienced']['favoritecount'].append(developers[developer]['favoritecount']['difficult_experienced_min'])
print('Subjectivity buckets Mean Value')
print('Easy')
print('------')
print('Novice ',np.mean(np.array(easy['novice']['subjectivity']).astype(np.float)))
print('Beginner ',np.mean(np.array(easy['beginner']['subjectivity']).astype(np.float)))
print('Intermediate ',np.mean(np.array(easy['intermediate']['subjectivity']).astype(np.float)))
print('Experienced ',np.mean(np.array(easy['experienced']['subjectivity']).astype(np.float)))
print('\n')
print('Medium')
print('------')
print('Novice ',np.mean(np.array(medium['novice']['subjectivity']).astype(np.float)))
print('Beginner ',np.mean(np.array(medium['beginner']['subjectivity']).astype(np.float)))
print('Intermediate ',np.mean(np.array(medium['intermediate']['subjectivity']).astype(np.float)))
print('Experienced ',np.mean(np.array(medium['experienced']['subjectivity']).astype(np.float)))
print('\n')
print('Difficult')
print('------')
print('Novice ',np.mean(np.array(difficult['novice']['subjectivity']).astype(np.float)))
print('Beginner ',np.mean(np.array(difficult['beginner']['subjectivity']).astype(np.float)))
print('Intermediate ',np.mean(np.array(difficult['intermediate']['subjectivity']).astype(np.float)))
print('Experienced ',np.mean(np.array(difficult['experienced']['subjectivity']).astype(np.float)))
print('\n\n')


print('Polarity buckets Mean Value')
print('Easy')
print('------')
print('Novice ',np.mean(np.array(easy['novice']['polarity']).astype(np.float)))
print('Beginner ',np.mean(np.array(easy['beginner']['polarity']).astype(np.float)))
print('Intermediate ',np.mean(np.array(easy['intermediate']['polarity']).astype(np.float)))
print('Experienced ',np.mean(np.array(easy['experienced']['polarity']).astype(np.float)))
print('\n')
print('Medium')
print('------')
print('Novice ',np.mean(np.array(medium['novice']['polarity']).astype(np.float)))
print('Beginner ',np.mean(np.array(medium['beginner']['polarity']).astype(np.float)))
print('Intermediate ',np.mean(np.array(medium['intermediate']['polarity']).astype(np.float)))
print('Experienced ',np.mean(np.array(medium['experienced']['polarity']).astype(np.float)))
print('\n')
print('Difficult')
print('------')
print('Novice ',np.mean(np.array(difficult['novice']['polarity']).astype(np.float)))
print('Beginner ',np.mean(np.array(difficult['beginner']['polarity']).astype(np.float)))
print('Intermediate ',np.mean(np.array(difficult['intermediate']['polarity']).astype(np.float)))
print('Experienced ',np.mean(np.array(difficult['experienced']['polarity']).astype(np.float)))
print('\n\n')

print('Word Counts buckets Mean Value')
print('Easy')
print('------')
print('Novice ',np.mean(np.array(easy['novice']['word_count']).astype(np.float)))
print('Beginner ',np.mean(np.array(easy['beginner']['word_count']).astype(np.float)))
print('Intermediate ',np.mean(np.array(easy['intermediate']['word_count']).astype(np.float)))
print('Experienced ',np.mean(np.array(easy['experienced']['word_count']).astype(np.float)))
print('\n')
print('Medium')
print('------')
print('Novice ',np.mean(np.array(medium['novice']['word_count']).astype(np.float)))
print('Beginner ',np.mean(np.array(medium['beginner']['word_count']).astype(np.float)))
print('Intermediate ',np.mean(np.array(medium['intermediate']['word_count']).astype(np.float)))
print('Experienced ',np.mean(np.array(medium['experienced']['word_count']).astype(np.float)))
print('\n')
print('Difficult')
print('------')
print('Novice ',np.mean(np.array(difficult['novice']['word_count']).astype(np.float)))
print('Beginner ',np.mean(np.array(difficult['beginner']['word_count']).astype(np.float)))
print('Intermediate ',np.mean(np.array(difficult['intermediate']['word_count']).astype(np.float)))
print('Experienced ',np.mean(np.array(difficult['experienced']['word_count']).astype(np.float)))
print('\n\n')
print('Score buckets Mean Value')
print('Easy')
print('------')
print('Novice ',np.mean(np.array(easy['novice']['score']).astype(np.float)))
print('Beginner ',np.mean(np.array(easy['beginner']['score']).astype(np.float)))
print('Intermediate ',np.mean(np.array(easy['intermediate']['score']).astype(np.float)))
print('Experienced ',np.mean(np.array(easy['experienced']['score']).astype(np.float)))
print('\n')
print('Medium')
print('------')
print('Novice ',np.mean(np.array(medium['novice']['score']).astype(np.float)))
print('Beginner ',np.mean(np.array(medium['beginner']['score']).astype(np.float)))
print('Intermediate ',np.mean(np.array(medium['intermediate']['score']).astype(np.float)))
print('Experienced ',np.mean(np.array(medium['experienced']['score']).astype(np.float)))
print('\n')
print('Difficult')
print('------')
print('Novice ',np.mean(np.array(difficult['novice']['score']).astype(np.float)))
print('Beginner ',np.mean(np.array(difficult['beginner']['score']).astype(np.float)))
print('Intermediate ',np.mean(np.array(difficult['intermediate']['score']).astype(np.float)))
print('Experienced ',np.mean(np.array(difficult['experienced']['score']).astype(np.float)))
print('\n\n')
print('\tOn Min Values\n')
# analysis.manwhitneytest(easy, medium, difficult)


