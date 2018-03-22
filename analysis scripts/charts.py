import csv
import statistics as statistics
from scipy.stats import mannwhitneyu
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
# matplotlib.use('GTK')
import matplotlib.pyplot as plt
import seaborn as sns




patterns = []
polarity = {}
wordCount = {}
subjectivity = {}

easy = {}
easy['novice'] = {}
easy['novice']['subjectivity'] = []
easy['novice']['polarity'] = []
easy['novice']['word_count'] = []

easy['beginner'] = {}
easy['beginner']['subjectivity'] = []
easy['beginner']['polarity'] = []
easy['beginner']['word_count'] = []

easy['intermediate'] = {}
easy['intermediate']['subjectivity'] = []
easy['intermediate']['polarity'] = []
easy['intermediate']['word_count'] = []

easy['experienced'] = {}
easy['experienced']['subjectivity'] = []
easy['experienced']['polarity'] = []
easy['experienced']['word_count'] = []

medium = {}
medium['novice'] = {}
medium['novice']['subjectivity'] = []
medium['novice']['polarity'] = []
medium['novice']['word_count'] = []

medium['beginner'] = {}
medium['beginner']['subjectivity'] = []
medium['beginner']['polarity'] = []
medium['beginner']['word_count'] = []

medium['intermediate'] = {}
medium['intermediate']['subjectivity'] = []
medium['intermediate']['polarity'] = []
medium['intermediate']['word_count'] = []

medium['experienced'] = {}
medium['experienced']['subjectivity'] = []
medium['experienced']['polarity'] = []
medium['experienced']['word_count'] = []

difficult = {}
difficult['novice'] = {}
difficult['novice']['subjectivity'] = []
difficult['novice']['polarity'] = []
difficult['novice']['word_count'] = []

difficult['beginner'] = {}
difficult['beginner']['subjectivity'] = []
difficult['beginner']['polarity'] = []
difficult['beginner']['word_count'] = []

difficult['intermediate'] = {}
difficult['intermediate']['subjectivity'] = []
difficult['intermediate']['polarity'] = []
difficult['intermediate']['word_count'] = []

difficult['experienced'] = {}
difficult['experienced']['subjectivity'] = []
difficult['experienced']['polarity'] = []
difficult['experienced']['word_count'] = []

analysis_reader = csv.reader(open('./DataSet/analysis.csv', 'rU'), delimiter= ",")
rows = []
for line in analysis_reader:
	if(len(line) >= 8):
		rows.append({'question_type' : line[1], 'wordCount' : line[3], 'polarity': line[4],'subjectivity' : line[5], 'developer' : line[6], 'developer experience' :line[7], 'question_id' : line[0]})

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
	easy['novice']['subjectivity'].append(developers[developer]['subjectivity']['easy_novice_mean'])
	easy['beginner']['subjectivity'].append(developers[developer]['subjectivity']['easy_beginner_mean'])
	easy['intermediate']['subjectivity'].append(developers[developer]['subjectivity']['easy_intermediate_mean'])
	easy['experienced']['subjectivity'].append(developers[developer]['subjectivity']['easy_experienced_mean'])
	medium['novice']['subjectivity'].append(developers[developer]['subjectivity']['medium_novice_mean'])
	medium['beginner']['subjectivity'].append(developers[developer]['subjectivity']['medium_beginner_mean'])
	medium['intermediate']['subjectivity'].append(developers[developer]['subjectivity']['medium_intermediate_mean'])
	medium['experienced']['subjectivity'].append(developers[developer]['subjectivity']['medium_experienced_mean'])
	difficult['novice']['subjectivity'].append(developers[developer]['subjectivity']['difficult_novice_mean'])
	difficult['beginner']['subjectivity'].append(developers[developer]['subjectivity']['difficult_beginner_mean'])
	difficult['intermediate']['subjectivity'].append(developers[developer]['subjectivity']['difficult_intermediate_mean'])
	difficult['experienced']['subjectivity'].append(developers[developer]['subjectivity']['difficult_experienced_mean'])

	## Polarity
	easy['novice']['polarity'].append(developers[developer]['polarity']['easy_novice_mean'])
	easy['beginner']['polarity'].append(developers[developer]['polarity']['easy_beginner_mean'])
	easy['intermediate']['polarity'].append(developers[developer]['polarity']['easy_intermediate_mean'])
	easy['experienced']['polarity'].append(developers[developer]['polarity']['easy_experienced_mean'])
	medium['novice']['polarity'].append(developers[developer]['polarity']['medium_novice_mean'])
	medium['beginner']['polarity'].append(developers[developer]['polarity']['medium_beginner_mean'])
	medium['intermediate']['polarity'].append(developers[developer]['polarity']['medium_intermediate_mean'])
	medium['experienced']['polarity'].append(developers[developer]['polarity']['medium_experienced_mean'])
	difficult['novice']['polarity'].append(developers[developer]['polarity']['difficult_novice_mean'])
	difficult['beginner']['polarity'].append(developers[developer]['polarity']['difficult_beginner_mean'])
	difficult['intermediate']['polarity'].append(developers[developer]['polarity']['difficult_intermediate_mean'])
	difficult['experienced']['polarity'].append(developers[developer]['polarity']['difficult_experienced_mean'])

	## Word Count
	easy['novice']['word_count'].append(developers[developer]['word_count']['easy_novice_mean'])
	easy['beginner']['word_count'].append(developers[developer]['word_count']['easy_beginner_mean'])
	easy['intermediate']['word_count'].append(developers[developer]['word_count']['easy_intermediate_mean'])
	easy['experienced']['word_count'].append(developers[developer]['word_count']['easy_experienced_mean'])
	medium['novice']['word_count'].append(developers[developer]['word_count']['medium_novice_mean'])
	medium['beginner']['word_count'].append(developers[developer]['word_count']['medium_beginner_mean'])
	medium['intermediate']['word_count'].append(developers[developer]['word_count']['medium_intermediate_mean'])
	medium['experienced']['word_count'].append(developers[developer]['word_count']['medium_experienced_mean'])
	difficult['novice']['word_count'].append(developers[developer]['word_count']['difficult_novice_mean'])
	difficult['beginner']['word_count'].append(developers[developer]['word_count']['difficult_beginner_mean'])
	difficult['intermediate']['word_count'].append(developers[developer]['word_count']['difficult_intermediate_mean'])
	difficult['experienced']['word_count'].append(developers[developer]['word_count']['difficult_experienced_mean'])

plt.style.use('seaborn-darkgrid')
sns.set(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=0.8)
fig, ax =plt.subplots(3,1)
plt.figure()
sns_plt = sns.kdeplot(easy['novice']['subjectivity'], shade=True, label="novice", ax=ax[0])
sns_plt = sns.kdeplot(easy['beginner']['subjectivity'], shade=True, label="beginner", ax=ax[0])
sns_plt = sns.kdeplot(easy['intermediate']['subjectivity'], shade=True, label="intermediate",  ax=ax[0])
sns_plt = sns.kdeplot(easy['experienced']['subjectivity'], shade=True, label="experienced",  ax=ax[0])
ax[0].set_title('Easy')
# sns_plt.figure.clf()

sns_plt = sns.kdeplot(medium['novice']['subjectivity'], shade=True, label="novice", ax=ax[1])
sns_plt = sns.kdeplot(medium['beginner']['subjectivity'], shade=True, label="beginner", ax=ax[1])
sns_plt = sns.kdeplot(medium['intermediate']['subjectivity'], shade=True, label="intermediate",  ax=ax[1])
sns_plt = sns.kdeplot(medium['experienced']['subjectivity'], shade=True, label="experienced",  ax=ax[1])
ax[1].set_title('Medium')
# sns_plt.figure.clf()

sns_plt = sns.kdeplot(difficult['novice']['subjectivity'], shade=True, label="novice", ax=ax[2])
sns_plt = sns.kdeplot(difficult['beginner']['subjectivity'], shade=True, label="beginner", ax=ax[2])
sns_plt = sns.kdeplot(difficult['intermediate']['subjectivity'], shade=True, label="intermediate",  ax=ax[2])
sns_plt = sns.kdeplot(difficult['experienced']['subjectivity'], shade=True, label="experienced",  ax=ax[2])
ax[2].set_title('Difficult')

fig.savefig('Subjectivity.png')

fig, ax =plt.subplots(3,1)
plt.figure()
sns_plt = sns.kdeplot(easy['novice']['polarity'], shade=True, label="novice", ax=ax[0])
sns_plt = sns.kdeplot(easy['beginner']['polarity'], shade=True, label="beginner", ax=ax[0])
sns_plt = sns.kdeplot(easy['intermediate']['polarity'], shade=True, label="intermediate",  ax=ax[0])
sns_plt = sns.kdeplot(easy['experienced']['polarity'], shade=True, label="experienced",  ax=ax[0])
ax[0].set_title('Easy')
# sns_plt.figure.clf()

sns_plt = sns.kdeplot(medium['novice']['polarity'], shade=True, label="novice", ax=ax[1])
sns_plt = sns.kdeplot(medium['beginner']['polarity'], shade=True, label="beginner", ax=ax[1])
sns_plt = sns.kdeplot(medium['intermediate']['polarity'], shade=True, label="intermediate",  ax=ax[1])
sns_plt = sns.kdeplot(medium['experienced']['polarity'], shade=True, label="experienced",  ax=ax[1])
ax[1].set_title('Medium')
# sns_plt.figure.clf()

sns_plt = sns.kdeplot(difficult['novice']['polarity'], shade=True, label="novice", ax=ax[2])
sns_plt = sns.kdeplot(difficult['beginner']['polarity'], shade=True, label="beginner", ax=ax[2])
sns_plt = sns.kdeplot(difficult['intermediate']['polarity'], shade=True, label="intermediate",  ax=ax[2])
sns_plt = sns.kdeplot(difficult['experienced']['polarity'], shade=True, label="experienced",  ax=ax[2])
ax[2].set_title('Difficult')

fig.savefig('Polarity.png')

fig, ax =plt.subplots(3,1)
plt.figure()
plt.tight_layout()
sns_plt = sns.kdeplot(easy['novice']['word_count'], shade=True, label="novice", ax=ax[0])
sns_plt = sns.kdeplot(easy['beginner']['word_count'], shade=True, label="beginner", ax=ax[0])
sns_plt = sns.kdeplot(easy['intermediate']['word_count'], shade=True, label="intermediate",  ax=ax[0])
sns_plt = sns.kdeplot(easy['experienced']['word_count'], shade=True, label="experienced",  ax=ax[0])
ax[0].set_title('Easy')
# sns_plt.figure.clf()

sns_plt = sns.kdeplot(medium['novice']['word_count'], shade=True, label="novice", ax=ax[1])
sns_plt = sns.kdeplot(medium['beginner']['word_count'], shade=True, label="beginner", ax=ax[1])
sns_plt = sns.kdeplot(medium['intermediate']['word_count'], shade=True, label="intermediate",  ax=ax[1])
sns_plt = sns.kdeplot(medium['experienced']['word_count'], shade=True, label="experienced",  ax=ax[1])
ax[1].set_title('Medium')
# sns_plt.figure.clf()

sns_plt = sns.kdeplot(difficult['novice']['word_count'], shade=True, label="novice", ax=ax[2])
sns_plt = sns.kdeplot(difficult['beginner']['word_count'], shade=True, label="beginner", ax=ax[2])
sns_plt = sns.kdeplot(difficult['intermediate']['word_count'], shade=True, label="intermediate",  ax=ax[2])
sns_plt = sns.kdeplot(difficult['experienced']['word_count'], shade=True, label="experienced",  ax=ax[2])
ax[2].set_title('Difficult')



fig.savefig('WordCount.png')



# print developers['38346']
# # df=pd.DataFrame({'x': range(1,, 'y1': np.random.randn(10), 'y2': np.random.randn(10)+range(1,11), 'y3': np.random.randn(10)+range(11,21), 'y4': np.random.randn(10)+range(6,16), 'y5': np.random.randn(10)+range(4,14)+(0,0,0,0,0,0,0,-3,-8,-6), 'y6': np.random.randn(10)+range(2,12), 'y7': np.random.randn(10)+range(5,15), 'y8': np.random.randn(10)+range(4,14), 'y9': np.random.randn(10)+range(4,14) })

# print(max( len(easy['novice']['subjectivity']),len(easy['beginner']['subjectivity']),len(easy['intermediate']['subjectivity']),len(easy['experienced']['subjectivity']) ))
# print(max( max(easy['novice']['subjectivity']), max(easy['beginner']['subjectivity']),max(easy['intermediate']['subjectivity']),max(easy['experienced']['subjectivity']) ))

# df=pd.DataFrame({'x': range(0,max( len(easy['novice']['subjectivity']),len(easy['beginner']['subjectivity']),len(easy['intermediate']['subjectivity']),len(easy['experienced']['subjectivity']) )), 
# 	'y1': easy['novice']['subjectivity'], 'y2': easy['beginner']['subjectivity'], 'y3': easy['intermediate']['subjectivity'], 'y4': easy['experienced']['subjectivity'] })



# # fig, ax =plt.subplots(1,3)

# # plt.figure()
# # sns_plt = sns.kdeplot(easy['novice']['subjectivity'], shade=True, label="novice", ax=ax[0])
# # sns_plt = sns.kdeplot(easy['beginner']['subjectivity'], shade=True, label="beginner", ax=ax[0])
# # sns_plt = sns.kdeplot(easy['intermediate']['subjectivity'], shade=True, label="intermediate",  ax=ax[0])
# # sns_plt = sns.kdeplot(easy['experienced']['subjectivity'], shade=True, label="experienced",  ax=ax[0])
# # # sns_plt.figure.savefig('subjectivity.png')
# # # sns_plt.figure.figure()
# # sns_plt.figure.clf()


# # sns_plt = sns.kdeplot(easy['novice']['polarity'], shade=True, label="novice",  ax=ax[1])
# # sns_plt = sns.kdeplot(easy['beginner']['polarity'], shade=True, label="beginner",  ax=ax[1])
# # sns_plt = sns.kdeplot(easy['intermediate']['polarity'], shade=True, label="intermediate",  ax=ax[1])
# # sns_plt = sns.kdeplot(easy['experienced']['polarity'], shade=True, label="experienced",  ax=ax[1])
# # # sns_plt.figure.savefig('polarity.png')
# # # sns_plt.figure.figure()
# # # sns_plt.figure.clf()
# # plt.gcf().clf()

# easy_word_count_fig, ax = plt.subplots()
# sns_plt = sns.kdeplot(easy['novice']['word_count'], shade=True, label="novice")#,  ax=ax[2])
# sns_plt = sns.kdeplot(easy['beginner']['word_count'], shade=True, label="beginner")#,  ax=ax[2])
# sns_plt = sns.kdeplot(easy['intermediate']['word_count'], shade=True, label="intermediate")#,  ax=ax[2])
# sns_plt = sns.kdeplot(easy['experienced']['word_count'], shade=True, label="experienced")#,  ax=ax[2])
# easy_word_count_fig.savefig('Easy_Word_Count.png')
# # # sns_plt.figure.savefig('word_count.png')

# # fig.savefig('Easy.png')

# # medium_fig, ax =plt.subplots(1,3)
# # # sns_plt.figure.clf()
# # plt.figure()
# # sns_plt = sns.kdeplot(medium['novice']['subjectivity'], shade=True, label="novice", ax=ax[0])
# # sns_plt = sns.kdeplot(medium['beginner']['subjectivity'], shade=True, label="beginner", ax=ax[0])
# # sns_plt = sns.kdeplot(medium['intermediate']['subjectivity'], shade=True, label="intermediate",  ax=ax[0])
# # sns_plt = sns.kdeplot(medium['experienced']['subjectivity'], shade=True, label="experienced",  ax=ax[0])
# # # sns_plt.figure.savefig('subjectivity.png')
# # # sns_plt.figure.figure()
# # # sns_plt.figure.clf()
# # plt.gcf().clf()

# # medium_polarity_fig, ax = plt.subplots()
# # sns_plt = sns.kdeplot(medium['novice']['polarity'], shade=True, label="novice")#,  ax=ax[1])
# # sns_plt = sns.kdeplot(medium['beginner']['polarity'], shade=True, label="beginner")#,  ax=ax[1])
# # sns_plt = sns.kdeplot(medium['intermediate']['polarity'], shade=True, label="intermediate")#,  ax=ax[1])
# # sns_plt = sns.kdeplot(medium['experienced']['polarity'], shade=True, label="experienced")#,  ax=ax[1])
# # medium_polarity_fig.savefig('Medium_Polarity.png')
# # # # sns_plt.figure.savefig('polarity.png')
# # sns_plt.figure.clf()
# # plt.gcf().clf()
# # plt.figure()

# medium_word_count_fig, ax = plt.subplots()
# sns_plt = sns.kdeplot(medium['novice']['word_count'], shade=True, label="novice")#,  ax=ax[2])
# sns_plt = sns.kdeplot(medium['beginner']['word_count'], shade=True, label="beginner")#,  ax=ax[2])
# sns_plt = sns.kdeplot(medium['intermediate']['word_count'], shade=True, label="intermediate")#,  ax=ax[2])
# sns_plt = sns.kdeplot(medium['experienced']['word_count'], shade=True, label="experienced")#,  ax=ax[2])
# # sns_plt.figure.savefig('word_count.png')

# medium_word_count_fig.savefig('Medium_Word_Count.png')

# difficult_word_count_fig, ax = plt.subplots()
# sns_plt = sns.kdeplot(difficult['novice']['word_count'], shade=True, label="novice")#,  ax=ax[2])
# sns_plt = sns.kdeplot(difficult['beginner']['word_count'], shade=True, label="beginner")#,  ax=ax[2])
# sns_plt = sns.kdeplot(difficult['intermediate']['word_count'], shade=True, label="intermediate")#,  ax=ax[2])
# sns_plt = sns.kdeplot(difficult['experienced']['word_count'], shade=True, label="experienced")#,  ax=ax[2])
# difficult_word_count_fig.savefig('Difficult_Word_Count.png')
# print difficult['novice']['polarity']
# print("\n\n")
# print difficult['novice']['subjectivity']

# plt.plot( 'x', 'y1', data=df, marker='', color='skyblue', linewidth=1, label="novice")
# plt.legend()
# plt.savefig("Easy_novice.png") 

# plt.plot( 'x', 'y2', data=df, marker='', color='olive', linewidth=1, label="beginner")
# plt.legend()
# plt.savefig("Easy_beginner.png") 

# plt.plot( 'x', 'y3', data=df, marker='', color='red', linewidth=1, label="intermediate")
# plt.legend()
# plt.savefig("Easy_intermediate.png") 

# plt.plot( 'x', 'y4', data=df, marker='', color='green', linewidth=1, label="experienced")
# plt.legend()
# plt.savefig("Easy_experienced.png") 

 

# print easy
# print max(easy['novice']['subjectivity'])
# trace1 = go.Histogram(
#     x=easy['novice']['subjectivity'],
#     opacity=0.75
# )
# trace2 = go.Histogram(
#     x=easy['beginner']['subjectivity'],
#     opacity=0.75
# )
# trace3 = go.Histogram(
#     x=easy['intermediate']['subjectivity'],
#     opacity=0.75
# )
# trace4 = go.Histogram(
#     x=easy['experienced']['subjectivity'],
#     opacity=0.75
# )

# data = [trace1, trace2, trace3, trace4]
# layout = go.Layout(barmode='overlay')
# fig = go.Figure(data=data, layout=layout)

# py.iplot(fig, filename='overlaid histogram')