import csv
import statistics as statistics
from scipy.stats import mannwhitneyu
import numpy as np

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

analysis_reader = csv.reader(open('../DataSet/Mar-21/analysis.csv', 'rU'), delimiter= ",")

rows = []
for line in analysis_reader:
	if(len(line) >= 7):
		rows.append({'question_type' : line[1], 'wordCount' : line[3], 'polarity': line[4],'subjectivity' : line[5], 'developer' : line[6], 'developer experience' :line[7], 'question_id' : line[0]})

novice = {}
novice['easy'] = {}
novice['easy']['subjectivity'] = []
novice['easy']['polarity'] = []
novice['easy']['word_count'] = []

novice['medium'] = {}
novice['medium']['subjectivity'] = []
novice['medium']['polarity'] = []
novice['medium']['word_count'] = []

novice['difficult'] = {}
novice['difficult']['subjectivity'] = []
novice['difficult']['polarity'] = []
novice['difficult']['word_count'] = []

beginner = {}
beginner['easy'] = {}
beginner['easy']['subjectivity'] = []
beginner['easy']['polarity'] = []
beginner['easy']['word_count'] = []

beginner['medium'] = {}
beginner['medium']['subjectivity'] = []
beginner['medium']['polarity'] = []
beginner['medium']['word_count'] = []

beginner['difficult'] = {}
beginner['difficult']['subjectivity'] = []
beginner['difficult']['polarity'] = []
beginner['difficult']['word_count'] = []

intermediate = {}
intermediate['easy'] = {}
intermediate['easy']['subjectivity'] = []
intermediate['easy']['polarity'] = []
intermediate['easy']['word_count'] = []

intermediate['medium'] = {}
intermediate['medium']['subjectivity'] = []
intermediate['medium']['polarity'] = []
intermediate['medium']['word_count'] = []

intermediate['difficult'] = {}
intermediate['difficult']['subjectivity'] = []
intermediate['difficult']['polarity'] = []
intermediate['difficult']['word_count'] = []

experienced = {}
experienced['easy'] = {}
experienced['easy']['subjectivity'] = []
experienced['easy']['polarity'] = []
experienced['easy']['word_count'] = []

experienced['medium'] = {}
experienced['medium']['subjectivity'] = []
experienced['medium']['polarity'] = []
experienced['medium']['word_count'] = []

experienced['difficult'] = {}
experienced['difficult']['subjectivity'] = []
experienced['difficult']['polarity'] = []
experienced['difficult']['word_count'] = []

developers = {}

# Segrating questions of each developer in their space
for row in rows:
	if(row['developer'] in developers):
		developers[row['developer']]['answers'].append(row)
	else:
		developers[row['developer']] = {}
		developers[row['developer']]['answers'] = []
		developers[row['developer']]['answers'].append(row)

for developer in developers:
	for answer in developers[developer]['answers']:
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

		if(answer['question_type'].lower() == 'easy'):
			if(answer['developer experience'].lower() == 'novice'):
				easy_novice_subjectivity.append(answer['subjectivity'])
			if(answer['developer experience'].lower() == 'beginner'):
				easy_beginner_subjectivity.append(answer['subjectivity'])
			if(answer['developer experience'].lower() == 'intermediate'):
				easy_intermediate_subjectivity.append(answer['subjectivity'])
			if(answer['developer experience'].lower() == 'experienced'):
				easy_experienced_subjectivity.append(answer['subjectivity'])

		if(answer['question_type'].lower() == 'medium'):
			if(answer['developer experience'].lower() == 'novice'):
				medium_novice_subjectivity.append(answer['subjectivity'])
			if(answer['developer experience'].lower() == 'beginner'):
				medium_beginner_subjectivity.append(answer['subjectivity'])
			if(answer['developer experience'].lower() == 'intermediate'):
				medium_intermediate_subjectivity.append(answer['subjectivity'])
			if(answer['developer experience'].lower() == 'experienced'):
				medium_experienced_subjectivity.append(answer['subjectivity'])

		if(answer['question_type'].lower() == 'difficult'):
			if(answer['developer experience'].lower() == 'novice'):
				difficult_novice_subjectivity.append(answer['subjectivity'])
			if(answer['developer experience'].lower() == 'beginner'):
				difficult_beginner_subjectivity.append(answer['subjectivity'])
			if(answer['developer experience'].lower() == 'intermediate'):
				difficult_intermediate_subjectivity.append(answer['subjectivity'])
			if(answer['developer experience'].lower() == 'experienced'):
				difficult_experienced_subjectivity.append(answer['subjectivity'])


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

		if(answer['question_type'].lower() == 'easy'):
			if(answer['developer experience'].lower() == 'novice'):
				easy_novice_polarity.append(answer['polarity'])
			if(answer['developer experience'].lower() == 'beginner'):
				easy_beginner_polarity.append(answer['polarity'])
			if(answer['developer experience'].lower() == 'intermediate'):
				easy_intermediate_polarity.append(answer['polarity'])
			if(answer['developer experience'].lower() == 'experienced'):
				easy_experienced_polarity.append(answer['polarity'])

		if(answer['question_type'].lower() == 'medium'):
			if(answer['developer experience'].lower() == 'novice'):
				medium_novice_polarity.append(answer['polarity'])
			if(answer['developer experience'].lower() == 'beginner'):
				medium_beginner_polarity.append(answer['polarity'])
			if(answer['developer experience'].lower() == 'intermediate'):
				medium_intermediate_polarity.append(answer['polarity'])
			if(answer['developer experience'].lower() == 'experienced'):
				medium_experienced_polarity.append(answer['polarity'])

		if(answer['question_type'].lower() == 'difficult'):
			if(answer['developer experience'].lower() == 'novice'):
				difficult_novice_polarity.append(answer['polarity'])
			if(answer['developer experience'].lower() == 'beginner'):
				difficult_beginner_polarity.append(answer['polarity'])
			if(answer['developer experience'].lower() == 'intermediate'):
				difficult_intermediate_polarity.append(answer['polarity'])
			if(answer['developer experience'].lower() == 'experienced'):
				difficult_experienced_polarity.append(answer['polarity'])	

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

		if(answer['question_type'].lower() == 'easy'):
			if(answer['developer experience'].lower() == 'novice'):
				easy_novice_word_count.append(answer['wordCount'])
			if(answer['developer experience'].lower() == 'beginner'):
				easy_beginner_word_count.append(answer['wordCount'])
			if(answer['developer experience'].lower() == 'intermediate'):
				easy_intermediate_word_count.append(answer['wordCount'])
			if(answer['developer experience'].lower() == 'experienced'):
				easy_experienced_word_count.append(answer['wordCount'])

		if(answer['question_type'].lower() == 'medium'):
			if(answer['developer experience'].lower() == 'novice'):
				medium_novice_word_count.append(answer['wordCount'])
			if(answer['developer experience'].lower() == 'beginner'):
				medium_beginner_word_count.append(answer['wordCount'])
			if(answer['developer experience'].lower() == 'intermediate'):
				medium_intermediate_word_count.append(answer['wordCount'])
			if(answer['developer experience'].lower() == 'experienced'):
				medium_experienced_word_count.append(answer['wordCount'])

		if(answer['question_type'].lower() == 'difficult'):
			if(answer['developer experience'].lower() == 'novice'):
				difficult_novice_word_count.append(answer['wordCount'])
			if(answer['developer experience'].lower() == 'beginner'):
				difficult_beginner_word_count.append(answer['wordCount'])
			if(answer['developer experience'].lower() == 'intermediate'):
				difficult_intermediate_word_count.append(answer['wordCount'])
			if(answer['developer experience'].lower() == 'experienced'):
				difficult_experienced_word_count.append(answer['wordCount'])		


	developers[developer]['subjectivity'] = {}
	developers[developer]['subjectivity']['easy_novice_mean'] = np.mean(np.array(easy_novice_subjectivity).astype(np.float)) if len(easy_novice_subjectivity) > 0 else 0.00
	developers[developer]['subjectivity']['easy_beginner_mean'] = np.mean(np.array(easy_beginner_subjectivity).astype(np.float)) if len(easy_beginner_subjectivity) > 0 else 0.00
	developers[developer]['subjectivity']['easy_intermediate_mean'] = np.mean(np.array(easy_intermediate_subjectivity).astype(np.float)) if len(easy_intermediate_subjectivity) > 0 else 0.00
	developers[developer]['subjectivity']['easy_experienced_mean'] = np.mean(np.array(easy_experienced_subjectivity).astype(np.float)) if len(easy_experienced_subjectivity) > 0 else 0.00
	developers[developer]['subjectivity']['medium_novice_mean'] = np.mean(np.array(medium_novice_subjectivity).astype(np.float)) if len(medium_novice_subjectivity) > 0 else 0.00
	developers[developer]['subjectivity']['medium_beginner_mean'] = np.mean(np.array(medium_beginner_subjectivity).astype(np.float)) if len(medium_beginner_subjectivity) > 0 else 0.00
	developers[developer]['subjectivity']['medium_intermediate_mean'] = np.mean(np.array(medium_intermediate_subjectivity).astype(np.float)) if len(medium_intermediate_subjectivity) > 0 else 0.00
	developers[developer]['subjectivity']['medium_experienced_mean'] = np.mean(np.array(medium_experienced_subjectivity).astype(np.float)) if len(medium_experienced_subjectivity) > 0 else 0.00
	developers[developer]['subjectivity']['difficult_novice_mean'] = np.mean(np.array(difficult_novice_subjectivity).astype(np.float)) if len(difficult_novice_subjectivity) > 0 else 0.00
	developers[developer]['subjectivity']['difficult_beginner_mean'] = np.mean(np.array(difficult_beginner_subjectivity).astype(np.float)) if len(difficult_beginner_subjectivity) > 0 else 0.00
	developers[developer]['subjectivity']['difficult_intermediate_mean'] = np.mean(np.array(difficult_intermediate_subjectivity).astype(np.float)) if len(difficult_intermediate_subjectivity) > 0 else 0.00
	developers[developer]['subjectivity']['difficult_experienced_mean'] = np.mean(np.array(difficult_experienced_subjectivity).astype(np.float)) if len(difficult_experienced_subjectivity) > 0 else 0.00

	## Polarity
	developers[developer]['polarity'] = {}
	developers[developer]['polarity']['easy_novice_mean'] = np.mean(np.array(easy_novice_polarity).astype(np.float)) if len(easy_novice_polarity) > 0 else 0.00
	developers[developer]['polarity']['easy_beginner_mean'] = np.mean(np.array(easy_beginner_polarity).astype(np.float)) if len(easy_beginner_polarity) > 0 else 0.00
	developers[developer]['polarity']['easy_intermediate_mean'] = np.mean(np.array(easy_intermediate_polarity).astype(np.float)) if len(easy_intermediate_polarity) > 0 else 0.00
	developers[developer]['polarity']['easy_experienced_mean'] = np.mean(np.array(easy_experienced_polarity).astype(np.float)) if len(easy_experienced_polarity) > 0 else 0.00
	developers[developer]['polarity']['medium_novice_mean'] = np.mean(np.array(medium_novice_polarity).astype(np.float)) if len(medium_novice_polarity) > 0 else 0.00
	developers[developer]['polarity']['medium_beginner_mean'] = np.mean(np.array(medium_beginner_polarity).astype(np.float)) if len(medium_beginner_polarity) > 0 else 0.00
	developers[developer]['polarity']['medium_intermediate_mean'] = np.mean(np.array(medium_intermediate_polarity).astype(np.float)) if len(medium_intermediate_polarity) > 0 else 0.00
	developers[developer]['polarity']['medium_experienced_mean'] = np.mean(np.array(medium_experienced_polarity).astype(np.float)) if len(medium_experienced_polarity) > 0 else 0.00
	developers[developer]['polarity']['difficult_novice_mean'] = np.mean(np.array(difficult_novice_polarity).astype(np.float)) if len(difficult_novice_polarity) > 0 else 0.00
	developers[developer]['polarity']['difficult_beginner_mean'] = np.mean(np.array(difficult_beginner_polarity).astype(np.float)) if len(difficult_beginner_polarity) > 0 else 0.00
	developers[developer]['polarity']['difficult_intermediate_mean'] = np.mean(np.array(difficult_intermediate_polarity).astype(np.float)) if len(difficult_intermediate_polarity) > 0 else 0.00
	developers[developer]['polarity']['difficult_experienced_mean'] = np.mean(np.array(difficult_experienced_polarity).astype(np.float)) if len(difficult_experienced_polarity) > 0 else 0.00

	## Word Count
	developers[developer]['word_count'] = {}
	developers[developer]['word_count']['easy_novice_mean'] = np.mean(np.array(easy_novice_word_count).astype(np.float)) if len(easy_novice_word_count) > 0 else 0.00
	developers[developer]['word_count']['easy_beginner_mean'] = np.mean(np.array(easy_beginner_word_count).astype(np.float)) if len(easy_beginner_word_count) > 0 else 0.00
	developers[developer]['word_count']['easy_intermediate_mean'] = np.mean(np.array(easy_intermediate_word_count).astype(np.float)) if len(easy_intermediate_word_count) > 0 else 0.00
	developers[developer]['word_count']['easy_experienced_mean'] = np.mean(np.array(easy_experienced_word_count).astype(np.float)) if len(easy_experienced_word_count) > 0 else 0.00
	developers[developer]['word_count']['medium_novice_mean'] = np.mean(np.array(medium_novice_word_count).astype(np.float)) if len(medium_novice_word_count) > 0 else 0.00
	developers[developer]['word_count']['medium_beginner_mean'] = np.mean(np.array(medium_beginner_word_count).astype(np.float)) if len(medium_beginner_word_count) > 0 else 0.00
	developers[developer]['word_count']['medium_intermediate_mean'] = np.mean(np.array(medium_intermediate_word_count).astype(np.float)) if len(medium_intermediate_word_count) > 0 else 0.00
	developers[developer]['word_count']['medium_experienced_mean'] = np.mean(np.array(medium_experienced_word_count).astype(np.float)) if len(medium_experienced_word_count) > 0 else 0.00
	developers[developer]['word_count']['difficult_novice_mean'] = np.mean(np.array(difficult_novice_word_count).astype(np.float)) if len(difficult_novice_word_count) > 0 else 0.00
	developers[developer]['word_count']['difficult_beginner_mean'] = np.mean(np.array(difficult_beginner_word_count).astype(np.float)) if len(difficult_beginner_word_count) > 0 else 0.00
	developers[developer]['word_count']['difficult_intermediate_mean'] = np.mean(np.array(difficult_intermediate_word_count).astype(np.float)) if len(difficult_intermediate_word_count) > 0 else 0.00
	developers[developer]['word_count']['difficult_experienced_mean'] = np.mean(np.array(difficult_experienced_word_count).astype(np.float)) if len(difficult_experienced_word_count) > 0 else 0.00

for developer in developers:
	novice['easy']['subjectivity'].append(developers[developer]['subjectivity']['easy_novice_mean'])
	novice['medium']['subjectivity'].append(developers[developer]['subjectivity']['medium_novice_mean'])
	novice['difficult']['subjectivity'].append(developers[developer]['subjectivity']['difficult_novice_mean'])

	beginner['easy']['subjectivity'].append(developers[developer]['subjectivity']['easy_beginner_mean'])
	beginner['medium']['subjectivity'].append(developers[developer]['subjectivity']['medium_beginner_mean'])
	beginner['difficult']['subjectivity'].append(developers[developer]['subjectivity']['difficult_beginner_mean'])

	intermediate['easy']['subjectivity'].append(developers[developer]['subjectivity']['easy_intermediate_mean'])
	intermediate['medium']['subjectivity'].append(developers[developer]['subjectivity']['medium_intermediate_mean'])
	intermediate['difficult']['subjectivity'].append(developers[developer]['subjectivity']['difficult_intermediate_mean'])

	experienced['easy']['subjectivity'].append(developers[developer]['subjectivity']['easy_experienced_mean'])
	experienced['medium']['subjectivity'].append(developers[developer]['subjectivity']['medium_experienced_mean'])
	experienced['difficult']['subjectivity'].append(developers[developer]['subjectivity']['difficult_experienced_mean'])

	## Polarity
	novice['easy']['polarity'].append(developers[developer]['polarity']['easy_novice_mean'])
	novice['medium']['polarity'].append(developers[developer]['polarity']['medium_novice_mean'])
	novice['difficult']['polarity'].append(developers[developer]['polarity']['difficult_novice_mean'])

	beginner['easy']['polarity'].append(developers[developer]['polarity']['easy_beginner_mean'])
	beginner['medium']['polarity'].append(developers[developer]['polarity']['medium_beginner_mean'])
	beginner['difficult']['polarity'].append(developers[developer]['polarity']['difficult_beginner_mean'])

	intermediate['easy']['polarity'].append(developers[developer]['polarity']['easy_intermediate_mean'])
	intermediate['medium']['polarity'].append(developers[developer]['polarity']['medium_intermediate_mean'])
	intermediate['difficult']['polarity'].append(developers[developer]['polarity']['difficult_intermediate_mean'])

	experienced['easy']['polarity'].append(developers[developer]['polarity']['easy_experienced_mean'])
	experienced['medium']['polarity'].append(developers[developer]['polarity']['medium_experienced_mean'])
	experienced['difficult']['polarity'].append(developers[developer]['polarity']['difficult_experienced_mean'])

	## Word Count
	novice['easy']['word_count'].append(developers[developer]['word_count']['easy_novice_mean'])
	novice['medium']['word_count'].append(developers[developer]['word_count']['medium_novice_mean'])
	novice['difficult']['word_count'].append(developers[developer]['word_count']['difficult_novice_mean'])

	beginner['easy']['word_count'].append(developers[developer]['word_count']['easy_beginner_mean'])
	beginner['medium']['word_count'].append(developers[developer]['word_count']['medium_beginner_mean'])
	beginner['difficult']['word_count'].append(developers[developer]['word_count']['difficult_beginner_mean'])

	intermediate['easy']['word_count'].append(developers[developer]['word_count']['easy_intermediate_mean'])
	intermediate['medium']['word_count'].append(developers[developer]['word_count']['medium_intermediate_mean'])
	intermediate['difficult']['word_count'].append(developers[developer]['word_count']['difficult_intermediate_mean'])

	experienced['easy']['word_count'].append(developers[developer]['word_count']['easy_experienced_mean'])
	experienced['medium']['word_count'].append(developers[developer]['word_count']['medium_experienced_mean'])
	experienced['difficult']['word_count'].append(developers[developer]['word_count']['difficult_experienced_mean'])

print('\tOn Subjectivity Score\n')
toUploaded = []
print('Novice Users')
p = mannwhitneyu(novice['easy']['subjectivity'], novice['medium']['subjectivity'])
if(p[1]< 0.005):
	print('Novice user easy vs medium differs by ', p[1])
	print(fxsize(novice['easy']['subjectivity'], novice['medium']['subjectivity']))

p = mannwhitneyu(novice['easy']['subjectivity'], novice['difficult']['subjectivity'])
if(p[1] < 0.05):
	print('Novice user easy vs difficult differs by ', p[1])
	print(fxsize(novice['easy']['subjectivity'], novice['difficult']['subjectivity']))

p = mannwhitneyu(novice['medium']['subjectivity'], novice['difficult']['subjectivity'])
if(p[1] < 0.05):
	print('Novice user medium vs difficult differs by ', p[1])
	print(fxsize(novice['medium']['subjectivity'], novice['difficult']['subjectivity']))

print('Beginner Users')
p = mannwhitneyu(beginner['easy']['subjectivity'], beginner['medium']['subjectivity'])
if(p[1] < 0.05):
	print('Beginner user easy vs medium differs by ', p[1])
	print(fxsize(beginner['easy']['subjectivity'], beginner['medium']['subjectivity']))

p = mannwhitneyu(beginner['easy']['subjectivity'], beginner['difficult']['subjectivity'])
if(p[1] < 0.05):
	print('Beginner user easy vs difficult differs by ', p[1])
	print(fxsize(beginner['easy']['subjectivity'], beginner['difficult']['subjectivity']))

p = mannwhitneyu(beginner['medium']['subjectivity'], beginner['difficult']['subjectivity'])
if(p[1] < 0.05):
	print('Beginner user medium vs difficult differs by ', p[1])
	print(fxsize(beginner['medium']['subjectivity'], beginner['difficult']['subjectivity']))

print('Intermediate Users')
p = mannwhitneyu(intermediate['easy']['subjectivity'], intermediate['medium']['subjectivity'])
if(p[1] < 0.05):
	print('Intermediate user easy vs medium differs by ', p[1])
	print(fxsize(intermediate['easy']['subjectivity'], intermediate['medium']['subjectivity']))

p = mannwhitneyu(intermediate['easy']['subjectivity'], intermediate['difficult']['subjectivity'])
if(p[1] < 0.05):
	print('Intermediate user easy vs difficult differs by ', p[1])
	print(fxsize(intermediate['easy']['subjectivity'], intermediate['difficult']['subjectivity']))

p = mannwhitneyu(intermediate['medium']['subjectivity'], intermediate['difficult']['subjectivity'])
if(p[1] < 0.05):
	print('Intermediate user medium vs difficult differs by ', p[1])
	print(fxsize(intermediate['medium']['subjectivity'], intermediate['difficult']['subjectivity']))

print('Experienced Users')
p = mannwhitneyu(experienced['easy']['subjectivity'], experienced['medium']['subjectivity'])
if(p[1] < 0.05):
	print('Experienced user easy vs medium differs by ', p[1])
	print(fxsize(experienced['easy']['subjectivity'], experienced['medium']['subjectivity']))

p = mannwhitneyu(experienced['easy']['subjectivity'], experienced['difficult']['subjectivity'])
if(p[1] < 0.05):
	print('Experienced user easy vs difficult differs by ', p[1])
	print(fxsize(experienced['easy']['subjectivity'], experienced['difficult']['subjectivity']))

p = mannwhitneyu(experienced['medium']['subjectivity'], experienced['difficult']['subjectivity'])
if(p[1] < 0.05):
	print('Experienced user medium vs difficult differs by ', p[1])
	print(fxsize(experienced['medium']['subjectivity'], experienced['difficult']['subjectivity']))

print('\tOn Polarity Score\n')
toUploaded = []
print('Novice Users')
p = mannwhitneyu(novice['easy']['polarity'], novice['medium']['polarity'])
if(p[1] < 0.05):
	print('Novice user easy vs medium differs by ', p[1])
	print(fxsize(novice['easy']['polarity'], novice['medium']['polarity']))

p = mannwhitneyu(novice['easy']['polarity'], novice['difficult']['polarity'])
if(p[1] < 0.05):
	print('Novice user easy vs difficult differs by ', p[1])
	print(fxsize(novice['easy']['polarity'], novice['difficult']['polarity']))

p = mannwhitneyu(novice['medium']['polarity'], novice['difficult']['polarity'])
if(p[1] < 0.05):
	print('Novice user medium vs difficult differs by ', p[1])
	print(fxsize(novice['medium']['polarity'], novice['difficult']['polarity']))

print('Beginner Users')
p = mannwhitneyu(beginner['easy']['polarity'], beginner['medium']['polarity'])
if(p[1] < 0.05):
	print('Beginner user easy vs medium differs by ', p[1])
	print(fxsize(beginner['easy']['polarity'], beginner['medium']['polarity']))

p = mannwhitneyu(beginner['easy']['polarity'], beginner['difficult']['polarity'])
if(p[1] < 0.05):
	print('Beginner user easy vs difficult differs by ', p[1])
	print(fxsize(beginner['easy']['polarity'], beginner['difficult']['polarity']))

p = mannwhitneyu(beginner['medium']['polarity'], beginner['difficult']['polarity'])
if(p[1] < 0.05):
	print('Beginner user medium vs difficult differs by ', p[1])
	print(fxsize(beginner['medium']['polarity'], beginner['difficult']['polarity']))

print('Intermediate Users')
p = mannwhitneyu(intermediate['easy']['polarity'], intermediate['medium']['polarity'])
if(p[1] < 0.05):
	print('Intermediate user easy vs medium differs by ', p[1])
	print(fxsize(intermediate['easy']['polarity'], intermediate['medium']['polarity']))

p = mannwhitneyu(intermediate['easy']['polarity'], intermediate['difficult']['polarity'])
if(p[1] < 0.05):
	print('Intermediate user easy vs difficult differs by ', p[1])
	print(fxsize(intermediate['easy']['polarity'], intermediate['difficult']['polarity']))

p = mannwhitneyu(intermediate['medium']['polarity'], intermediate['difficult']['polarity'])
if(p[1] < 0.05):
	print('Intermediate user medium vs difficult differs by ', p[1])
	print(fxsize(intermediate['medium']['polarity'], intermediate['difficult']['polarity']))

print('Experienced Users')
p = mannwhitneyu(experienced['easy']['polarity'], experienced['medium']['polarity'])
if(p[1] < 0.05):
	print('Experienced user easy vs medium differs by ', p[1])
	print(fxsize(experienced['easy']['polarity'], experienced['medium']['polarity']))

p = mannwhitneyu(experienced['easy']['polarity'], experienced['difficult']['polarity'])
if(p[1] < 0.05):
	print('Experienced user easy vs difficult differs by ', p[1])
	print(fxsize(experienced['easy']['polarity'], experienced['difficult']['polarity']))

p = mannwhitneyu(experienced['medium']['polarity'], experienced['difficult']['polarity'])
if(p[1] < 0.05):
	print('Experienced user medium vs difficult differs by ', p[1])
	print(fxsize(experienced['medium']['polarity'], experienced['difficult']['polarity']))

print('\tOn Word Count\n')
toUploaded = []
print('Novice Users')
p = mannwhitneyu(novice['easy']['word_count'], novice['medium']['word_count'])
if(p[1] < 0.05):
	print('Novice user easy vs medium differs by ', p[1])
	print(fxsize(novice['easy']['word_count'], novice['medium']['word_count']))

p = mannwhitneyu(novice['easy']['word_count'], novice['difficult']['word_count'])
if(p[1] < 0.05):
	print('Novice user easy vs difficult differs by ', p[1])
	print(fxsize(novice['easy']['word_count'], novice['difficult']['word_count']))

p = mannwhitneyu(novice['medium']['word_count'], novice['difficult']['word_count'])
if(p[1] < 0.05):
	print('Novice user medium vs difficult differs by ', p[1])
	print(fxsize(novice['medium']['word_count'], novice['difficult']['word_count']))

print('Beginner Users')
p = mannwhitneyu(beginner['easy']['word_count'], beginner['medium']['word_count'])
if(p[1] < 0.05):
	print('Beginner user easy vs medium differs by ', p[1])
	print(fxsize(beginner['easy']['word_count'], beginner['medium']['word_count']))

p = mannwhitneyu(beginner['easy']['word_count'], beginner['difficult']['word_count'])
if(p[1] < 0.05):
	print('Beginner user easy vs difficult differs by ', p[1])
	print(fxsize(beginner['easy']['word_count'], beginner['difficult']['word_count']))

p = mannwhitneyu(beginner['medium']['word_count'], beginner['difficult']['word_count'])
if(p[1] < 0.05):
	print('Beginner user medium vs difficult differs by ', p[1])
	print(fxsize(beginner['medium']['word_count'], beginner['difficult']['word_count']))

print('Intermediate Users')
p = mannwhitneyu(intermediate['easy']['word_count'], intermediate['medium']['word_count'])
if(p[1] < 0.05):
	print('Intermediate user easy vs medium differs by ', p[1])
	print(fxsize(intermediate['easy']['word_count'], intermediate['medium']['word_count']))

p = mannwhitneyu(intermediate['easy']['word_count'], intermediate['difficult']['word_count'])
if(p[1] < 0.05):
	print('Intermediate user easy vs difficult differs by ', p[1])
	print(fxsize(intermediate['easy']['word_count'], intermediate['difficult']['word_count']))

p = mannwhitneyu(intermediate['medium']['word_count'], intermediate['difficult']['word_count'])
if(p[1] < 0.05):
	print('Intermediate user medium vs difficult differs by ', p[1])
	print(fxsize(intermediate['medium']['word_count'], intermediate['difficult']['word_count']))

print('Experienced Users')
p = mannwhitneyu(experienced['easy']['word_count'], experienced['medium']['word_count'])
if(p[1] < 0.05):
	print('Experienced user easy vs medium differs by ', p[1])
	print(fxsize(experienced['easy']['word_count'], experienced['medium']['word_count']))

p = mannwhitneyu(experienced['easy']['word_count'], experienced['difficult']['word_count'])
if(p[1] < 0.05):
	print('Experienced user easy vs difficult differs by ', p[1])
	print(fxsize(experienced['easy']['word_count'], experienced['difficult']['word_count']))

p = mannwhitneyu(experienced['medium']['word_count'], experienced['difficult']['word_count'])
if(p[1] < 0.05):
	print('Experienced user medium vs difficult differs by ', p[1])
	print(fxsize(experienced['medium']['word_count'], experienced['difficult']['word_count']))


# with open('./All_Java_Developer_Profiles_On_Weekly_Basis.csv', 'w') as csvfile:
#     output_writer = csv.writer(csvfile, delimiter=',',
#                             quotechar=' ', quoting=csv.QUOTE_MINIMAL)
#     output_writer.writerow(['Difficult level', 'Attribute', 'Experience1', 'Experience2', 'p value', 'cliff delta'])
#     for data in toUploaded:
#     	output_writer.writerow(data)