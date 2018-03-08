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

#print fxsize(control,pilot)

def cliffsDelta(lst1,lst2,
                dull = [0.147, # small
                        0.33,  # medium
                        0.474 # large
                        ][0] ): 
  "Returns true if there are more than 'dull' differences"
  m, n = len(lst1), len(lst2)
  lst2 = sorted(lst2)
  j = more = less = 0
  for repeats,x in runs(sorted(lst1)):
    while j <= (n - 1) and lst2[j] <  x: 
      j += 1
    more += j*repeats
    while j <= (n - 1) and lst2[j] == x: 
      j += 1
    less += (n - j)*repeats
  d= (more - less) / (m*n) 
  return d
  #return abs(d)  > dull
   
def runs(lst):
  "Iterator, chunks repeated values"
  for j,two in enumerate(lst):
    if j == 0:
      one,i = two,0
    if one!=two:
      yield j - i,one
      i = j
    one=two
  yield j - i + 1,two

analysis_reader = csv.reader(open('./DataSet/analysis.csv', 'rU'), delimiter= ",")

rows = []
for line in analysis_reader:
	rows.append({'question_type' : line[1], 'wordCount' : line[3], 'polarity': line[4],'subjectivity' : line[5], 'developer experience' :line[7], 'question_id' : line[0]})

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


easy_exp_count = 0;
medium_exp_count = 0;
difficult_exp_count = 0;

easy_int_count = 0;
medium_int_count = 0;
difficult_int_count = 0;

easy_beg_count = 0;
medium_beg_count = 0;
difficult_beg_count = 0;

easy_nov_count = 0;
medium_nov_count = 0;
difficult_nov_count = 0;

polarity['Experienced']= {}
polarity['Experienced']['Easy'] = 0.00;
polarity['Experienced']['Medium'] = 0.00;
polarity['Experienced']['Difficult'] = 0.00;

polarity['Intermediate']= {}
polarity['Intermediate']['Easy'] = 0.00;
polarity['Intermediate']['Medium'] = 0.00;
polarity['Intermediate']['Difficult'] = 0.00;

polarity['Beginner']= {}
polarity['Beginner']['Easy'] = 0.00;
polarity['Beginner']['Medium'] = 0.00;
polarity['Beginner']['Difficult'] = 0.00;

polarity['Novice']= {}
polarity['Novice']['Easy'] = 0.00;
polarity['Novice']['Medium'] = 0.00;
polarity['Novice']['Difficult'] = 0.00;

wordCount['Experienced']= {}
wordCount['Experienced']['Easy'] = 0.00;
wordCount['Experienced']['Medium'] = 0.00;
wordCount['Experienced']['Difficult'] = 0.00;

wordCount['Intermediate']= {}
wordCount['Intermediate']['Easy'] = 0.00;
wordCount['Intermediate']['Medium'] = 0.00;
wordCount['Intermediate']['Difficult'] = 0.00;

wordCount['Beginner']= {}
wordCount['Beginner']['Easy'] = 0.00;
wordCount['Beginner']['Medium'] = 0.00;
wordCount['Beginner']['Difficult'] = 0.00;

wordCount['Novice']= {}
wordCount['Novice']['Easy'] = 0.00;
wordCount['Novice']['Medium'] = 0.00;
wordCount['Novice']['Difficult'] = 0.00;

subjectivity['Experienced']= {}
subjectivity['Experienced']['Easy'] = 0.00;
subjectivity['Experienced']['Medium'] = 0.00;
subjectivity['Experienced']['Difficult'] = 0.00;

subjectivity['Intermediate']= {}
subjectivity['Intermediate']['Easy'] = 0.00;
subjectivity['Intermediate']['Medium'] = 0.00;
subjectivity['Intermediate']['Difficult'] = 0.00;

subjectivity['Beginner']= {}
subjectivity['Beginner']['Easy'] = 0.00;
subjectivity['Beginner']['Medium'] = 0.00;
subjectivity['Beginner']['Difficult'] = 0.00;

subjectivity['Novice']= {}
subjectivity['Novice']['Easy'] = 0.00;
subjectivity['Novice']['Medium'] = 0.00;
subjectivity['Novice']['Difficult'] = 0.00;

for row in rows:
	
	#### Experienced Users #####

	if(row['question_type'] == 'Easy' and row['developer experience'] == 'Experienced'):
		polarity['Experienced']['Easy'] = float(polarity['Experienced']['Easy']) + float(row['polarity'])
		subjectivity['Experienced']['Easy'] = float(subjectivity['Experienced']['Easy']) + float(row['subjectivity'])
		wordCount['Experienced']['Easy'] = float(wordCount['Experienced']['Easy']) + float(row['wordCount'])
		easy_exp_count = easy_exp_count+1;

		easy['experienced']['subjectivity'].append(float(row['subjectivity']))
		easy['experienced']['polarity'].append(float(row['polarity']))
		easy['experienced']['word_count'].append(float(row['wordCount']))

	if(row['question_type'] == 'Medium' and row['developer experience'] == 'Experienced'):
		polarity['Experienced']['Medium'] = float(polarity['Experienced']['Easy']) + float(row['polarity'])
		subjectivity['Experienced']['Medium'] = float(subjectivity['Experienced']['Easy']) + float(row['subjectivity'])
		wordCount['Experienced']['Medium'] = float(wordCount['Experienced']['Easy']) + float(row['wordCount'])
		medium_exp_count = medium_exp_count+1;

		medium['experienced']['subjectivity'].append(float(row['subjectivity']))
		medium['experienced']['polarity'].append(float(row['polarity']))
		medium['experienced']['word_count'].append(float(row['wordCount']))
	
	if(row['question_type'] == 'Difficult' and row['developer experience'] == 'Experienced'):
		polarity['Experienced']['Difficult'] = float(polarity['Experienced']['Easy']) + float(row['polarity'])
		subjectivity['Experienced']['Difficult'] = float(subjectivity['Experienced']['Easy']) + float(row['subjectivity'])
		wordCount['Experienced']['Difficult'] = float(wordCount['Experienced']['Easy']) + float(row['wordCount'])
		difficult_exp_count = difficult_exp_count+1;

		difficult['experienced']['subjectivity'].append(float(row['subjectivity']))
		difficult['experienced']['polarity'].append(float(row['polarity']))
		difficult['experienced']['word_count'].append(float(row['wordCount']))

	
	###### Intermediate Users ####

	if(row['question_type'] == 'Easy' and row['developer experience'] == 'Intermediate'):
		polarity['Intermediate']['Easy'] = float(polarity['Intermediate']['Easy']) + float(row['polarity'])
		subjectivity['Intermediate']['Easy'] = float(subjectivity['Intermediate']['Easy']) + float(row['subjectivity'])
		wordCount['Intermediate']['Easy'] = float(wordCount['Intermediate']['Easy']) + float(row['wordCount'])
		easy_int_count = easy_int_count+1;

		easy['intermediate']['subjectivity'].append(float(row['subjectivity']))
		easy['intermediate']['polarity'].append(float(row['polarity']))
		easy['intermediate']['word_count'].append(float(row['wordCount']))


	if(row['question_type'] == 'Medium' and row['developer experience'] == 'Intermediate'):
		polarity['Intermediate']['Medium'] = float(polarity['Intermediate']['Easy']) + float(row['polarity'])
		subjectivity['Intermediate']['Medium'] = float(subjectivity['Intermediate']['Easy']) + float(row['subjectivity'])
		wordCount['Intermediate']['Medium'] = float(wordCount['Intermediate']['Easy']) + float(row['wordCount'])
		medium_int_count = medium_int_count+1;

		medium['intermediate']['subjectivity'].append(float(row['subjectivity']))
		medium['intermediate']['polarity'].append(float(row['polarity']))
		medium['intermediate']['word_count'].append(float(row['wordCount']))

	if(row['question_type'] == 'Difficult' and row['developer experience'] == 'Intermediate'):
		polarity['Intermediate']['Difficult'] = float(polarity['Intermediate']['Easy']) + float(row['polarity'])
		subjectivity['Intermediate']['Difficult'] = float(subjectivity['Intermediate']['Easy']) + float(row['subjectivity'])
		wordCount['Intermediate']['Difficult'] = float(wordCount['Intermediate']['Easy']) + float(row['wordCount'])
		difficult_int_count = difficult_int_count+1;

		difficult['intermediate']['subjectivity'].append(float(row['subjectivity']))
		difficult['intermediate']['polarity'].append(float(row['polarity']))
		difficult['intermediate']['word_count'].append(float(row['wordCount']))

		
	##### Beginner Users #############

	if(row['question_type'] == 'Easy' and row['developer experience'] == 'Beginner'):
		polarity['Beginner']['Easy'] = float(polarity['Beginner']['Easy']) + float(row['polarity'])
		subjectivity['Beginner']['Easy'] = float(subjectivity['Beginner']['Easy']) + float(row['subjectivity'])
		wordCount['Beginner']['Easy'] = float(wordCount['Beginner']['Easy']) + float(row['wordCount'])
		easy_beg_count = easy_beg_count+1;

		easy['beginner']['subjectivity'].append(float(row['subjectivity']))
		easy['beginner']['polarity'].append(float(row['polarity']))
		easy['beginner']['word_count'].append(float(row['wordCount']))

	if(row['question_type'] == 'Medium' and row['developer experience'] == 'Beginner'):
		polarity['Beginner']['Medium'] = float(polarity['Beginner']['Easy']) + float(row['polarity'])
		subjectivity['Beginner']['Medium'] = float(subjectivity['Beginner']['Easy']) + float(row['subjectivity'])
		wordCount['Beginner']['Medium'] = float(wordCount['Beginner']['Easy']) + float(row['wordCount'])
		medium_beg_count = medium_beg_count+1;

		medium['beginner']['subjectivity'].append(float(row['subjectivity']))
		medium['beginner']['polarity'].append(float(row['polarity']))
		medium['beginner']['word_count'].append(float(row['wordCount']))

	if(row['question_type'] == 'Difficult' and row['developer experience'] == 'Beginner'):
		polarity['Beginner']['Difficult'] = float(polarity['Beginner']['Easy']) + float(row['polarity'])
		subjectivity['Beginner']['Difficult'] = float(subjectivity['Beginner']['Easy']) + float(row['subjectivity'])
		wordCount['Beginner']['Difficult'] = float(wordCount['Beginner']['Easy']) + float(row['wordCount'])
		difficult_beg_count = difficult_beg_count+1;

		difficult['beginner']['subjectivity'].append(float(row['subjectivity']))
		difficult['beginner']['polarity'].append(float(row['polarity']))
		difficult['beginner']['word_count'].append(float(row['wordCount']))


	############# Novice Users ###################

	if(row['question_type'] == 'Easy' and row['developer experience'] == 'Novice'):
		polarity['Novice']['Easy'] = float(polarity['Novice']['Easy']) + float(row['polarity'])
		subjectivity['Novice']['Easy'] = float(subjectivity['Novice']['Easy']) + float(row['subjectivity'])
		wordCount['Novice']['Easy'] = float(wordCount['Novice']['Easy']) + float(row['wordCount'])
		easy_nov_count = easy_nov_count+1;

		easy['novice']['subjectivity'].append(float(row['subjectivity']))
		easy['novice']['polarity'].append(float(row['polarity']))
		easy['novice']['word_count'].append(float(row['wordCount']))


	if(row['question_type'] == 'Medium' and row['developer experience'] == 'Novice'):
		polarity['Novice']['Medium'] = float(polarity['Novice']['Easy']) + float(row['polarity'])
		subjectivity['Novice']['Medium'] = float(subjectivity['Novice']['Easy']) + float(row['subjectivity'])
		wordCount['Novice']['Medium'] = float(wordCount['Novice']['Easy']) + float(row['wordCount'])
		medium_nov_count = medium_nov_count+1;

		medium['novice']['subjectivity'].append(float(row['subjectivity']))
		medium['novice']['polarity'].append(float(row['polarity']))
		medium['novice']['word_count'].append(float(row['wordCount']))

	if(row['question_type'] == 'Difficult' and row['developer experience'] == 'Novice'):
		polarity['Novice']['Difficult'] = float(polarity['Novice']['Easy']) + float(row['polarity'])
		subjectivity['Novice']['Difficult'] = float(subjectivity['Novice']['Easy']) + float(row['subjectivity'])
		wordCount['Novice']['Difficult'] = float(wordCount['Novice']['Easy']) + float(row['wordCount'])
		difficult_nov_count = difficult_nov_count+1;

		difficult['novice']['subjectivity'].append(float(row['subjectivity']))
		difficult['novice']['polarity'].append(float(row['polarity']))
		difficult['novice']['word_count'].append(float(row['wordCount']))

print('Avg wordCount value of Experienced users answer to easy questions ', wordCount['Experienced']['Easy']/easy_exp_count)
print('Avg wordCount value of Experienced users answer to medium questions ', wordCount['Experienced']['Medium']/medium_exp_count)
print('Avg wordCount value of Experienced users answer to difficult questions ', wordCount['Experienced']['Difficult']/difficult_exp_count)
print("-----------------------------------------------\n")
print('Avg polarity value of Experienced users answer to easy questions ', polarity['Experienced']['Easy']/easy_exp_count)
print('Avg polarity value of Experienced users answer to medium questions ', polarity['Experienced']['Medium']/medium_exp_count)
print('Avg polarity value of Experienced users answer to difficult questions ', polarity['Experienced']['Difficult']/difficult_exp_count)
print("-----------------------------------------------\n")
print('Avg subjectivity value of Experienced users answer to easy questions ', subjectivity['Experienced']['Easy']/easy_exp_count)
print('Avg subjectivity value of Experienced users answer to medium questions ', subjectivity['Experienced']['Medium']/medium_exp_count)
print('Avg subjectivity value of Experienced users answer to difficult questions ', subjectivity['Experienced']['Difficult']/difficult_exp_count)

print("\n******Intermediate experience level****************\n")
print('Avg wordCount value of Intermediate users answer to easy questions ', wordCount['Intermediate']['Easy']/easy_exp_count)
print('Avg wordCount value of Intermediate users answer to medium questions ', wordCount['Intermediate']['Medium']/medium_exp_count)
print('Avg wordCount value of Intermediate users answer to difficult questions ', wordCount['Intermediate']['Difficult']/difficult_exp_count)
print("-----------------------------------------------\n")
print('Avg polarity value of Intermediate users answer to easy questions ', polarity['Intermediate']['Easy']/easy_int_count)
try:
    print('Avg polarity value of Intermediate users answer to medium questions ', polarity['Intermediate']['Medium']/medium_int_count)
except ZeroDivisionError:
    print('Avg polarity value of Intermediate users answer to medium questions ', 0)
print('Avg polarity value of Intermediate users answer to difficult questions ', polarity['Intermediate']['Difficult']/difficult_exp_count)
print("-----------------------------------------------\n")
print('Avg subjectivity value of Intermediate users answer to easy questions ', subjectivity['Intermediate']['Easy']/easy_exp_count)
try:
    print('Avg subjectivity value of Intermediate users answer to medium questions ', subjectivity['Intermediate']['Medium']/medium_int_count)
except ZeroDivisionError:
    print('Avg subjectivity value of Intermediate users answer to medium questions ', 0)
try:
    print('Avg subjectivity value of Intermediate users answer to difficult questions ', subjectivity['Intermediate']['Difficult']/difficult_int_count)
except ZeroDivisionError:
    print('Avg subjectivity value of Intermediate users answer to difficult questions ', 0)

print("\n******Beginner experience level****************\n")
print('Avg wordCount value of Beginner users answer to easy questions ', wordCount['Beginner']['Easy']/easy_beg_count)
try:
    print('Avg wordCount value of Beginner users answer to medium questions ', wordCount['Beginner']['Medium']/medium_beg_count)
except ZeroDivisionError:
    print('Avg subjectivity value of Beginner users answer to medium questions ', 0)
try:
    print('Avg wordCount value of Beginner users answer to difficult questions ', wordCount['Beginner']['Difficult']/difficult_beg_count)
except ZeroDivisionError:
    print('Avg wordCount value of Beginner users answer to difficult questions ', 0)

print("-----------------------------------------------\n")
print('Avg polarity value of Beginner users answer to easy questions ', polarity['Beginner']['Easy']/easy_beg_count)
try:
    print('Avg polarity value of Beginner users answer to medium questions ', polarity['Beginner']['Medium']/medium_beg_count)
except ZeroDivisionError:
    print('Avg polarity value of Beginner users answer to medium questions ', 0)
try:
    print('Avg polarity value of Beginner users answer to difficult questions ', polarity['Beginner']['Difficult']/difficult_beg_count)
except ZeroDivisionError:
    print('Avg polarity value of Beginner users answer to difficult questions ', 0)
print("-----------------------------------------------\n")
print('Avg subjectivity value of Beginner users answer to easy questions ', subjectivity['Beginner']['Easy']/easy_beg_count)
try:
    print('Avg subjectivity value of Beginner users answer to medium questions ', subjectivity['Beginner']['Medium']/medium_beg_count)
except ZeroDivisionError:
    print('Avg subjectivity value of Beginner users answer to medium questions ', 0)
try:
    print('Avg subjectivity value of Beginner users answer to difficult questions ', subjectivity['Beginner']['Difficult']/difficult_beg_count)
except ZeroDivisionError:
    print('Avg subjectivity value of Beginner users answer to difficult questions ', 0)

print("\n******Novice experience level****************\n")
print('Avg wordCount value of Novice users answer to easy questions ', wordCount['Novice']['Easy']/easy_nov_count)
try:
    print('Avg wordCount value of Novice users answer to medium questions ', wordCount['Novice']['Medium']/medium_nov_count)
except ZeroDivisionError:
    print('Avg subjectivity value of Novice users answer to medium questions ', 0)
try:
    print('Avg wordCount value of Novice users answer to difficult questions ', wordCount['Novice']['Difficult']/difficult_nov_count)
except ZeroDivisionError:
    print('Avg wordCount value of Novice users answer to difficult questions ', 0)

print("-----------------------------------------------\n")
print('Avg polarity value of Novice users answer to easy questions ', polarity['Novice']['Easy']/easy_nov_count)
try:
    print('Avg polarity value of Novice users answer to medium questions ', polarity['Novice']['Medium']/medium_nov_count)
except ZeroDivisionError:
    print('Avg polarity value of Novice users answer to medium questions ', 0)
try:
    print('Avg polarity value of Novice users answer to difficult questions ', polarity['Novice']['Difficult']/difficult_nov_count)
except ZeroDivisionError:
    print('Avg polarity value of Novice users answer to difficult questions ', 0)
print("-----------------------------------------------\n")
print('Avg subjectivity value of Novice users answer to easy questions ', subjectivity['Novice']['Easy']/easy_nov_count)
try:
    print('Avg subjectivity value of Novice users answer to medium questions ', subjectivity['Novice']['Medium']/medium_nov_count)
except ZeroDivisionError:
    print('Avg subjectivity value of Novice users answer to medium questions ', 0)
try:
    print('Avg subjectivity value of Novice users answer to difficult questions ', subjectivity['Novice']['Difficult']/difficult_nov_count)
except ZeroDivisionError:
    print('Avg subjectivity value of Novice users answer to difficult questions ', 0)

print('*********************** Man Whitney U Test Starts ***********************************')

print('\tOn Subjectivity Score\n')
print('Easy') 
p = mannwhitneyu(easy['novice']['subjectivity'], easy['beginner']['subjectivity'])
p
if(p[1] <= 0.05):
	print('Novice vs Beginner differs significantly ',p[1])
	print(fxsize(easy['beginner']['subjectivity'],easy['intermediate']['subjectivity']))
p = mannwhitneyu(easy['novice']['subjectivity'], easy['intermediate']['subjectivity'])
print p
if(p[1] <= 0.05):
	print('Novice vs Intermediate differs significantly ',p[1])
	print(fxsize(easy['novice']['subjectivity'],easy['intermediate']['subjectivity']))
p = mannwhitneyu(easy['novice']['subjectivity'], easy['experienced']['subjectivity'])
print p
if(p[1] <= 0.05):
	print('Novice vs Experienced differs significantly ',p[1])
	print(fxsize(easy['novice']['subjectivity'],easy['experienced']['subjectivity']))
print('\n')
p = mannwhitneyu(easy['beginner']['subjectivity'], easy['intermediate']['subjectivity'])
print p
if(p[1] <= 0.05):
	print('Beginner vs Intermediate differs significantly ',p[1])
	print(fxsize(easy['beginner']['subjectivity'],easy['intermediate']['subjectivity']))
	print(cliffsDelta(easy['beginner']['subjectivity'], easy['intermediate']['subjectivity']))
p = mannwhitneyu(easy['beginner']['subjectivity'], easy['experienced']['subjectivity'])
print p
if(p[1] <= 0.05):
	print('Beginner vs Experienced differs significantly ',p[1])
	print(fxsize(easy['beginner']['subjectivity'],easy['experienced']['subjectivity']))
print('\n')
p = mannwhitneyu(easy['intermediate']['subjectivity'], easy['experienced']['subjectivity'])
print p
if(p[1] <= 0.05):
	print('Intermediate vs Experienced differs significantly ',p[1])
	print(fxsize(easy['intermediate']['subjectivity'],easy['experienced']['subjectivity']))


print('\n\nMedium') 
p = mannwhitneyu(medium['novice']['subjectivity'], medium['beginner']['subjectivity'])
print p
if(p[1] <= 0.05):
	print('Novice vs Beginner differs significantly ',p[1])
	print(fxsize(medium['novice']['subjectivity'],medium['intermediate']['subjectivity']))
p = mannwhitneyu(medium['novice']['subjectivity'], medium['intermediate']['subjectivity'])
print p
if(p[1] <= 0.05):
	print('Novice vs Intermediate differs significantly ',p[1])
	print(fxsize(medium['novice']['subjectivity'],medium['intermediate']['subjectivity']))
p = mannwhitneyu(medium['novice']['subjectivity'], medium['experienced']['subjectivity'])
print p
if(p[1] <= 0.05):
	print('Novice vs Experienced differs significantly ',p[1])
	print(fxsize(medium['novice']['subjectivity'],medium['experienced']['subjectivity']))
print('\n')
p = mannwhitneyu(medium['beginner']['subjectivity'], medium['intermediate']['subjectivity'])
print p
if(p[1] <= 0.05):
	print('Beginner vs Intermediate differs significantly ',p[1])
	print(fxsize(medium['beginner']['subjectivity'],medium['intermediate']['subjectivity']))
p = mannwhitneyu(medium['beginner']['subjectivity'], medium['experienced']['subjectivity'])
print p
if(p[1] <= 0.05):
	print('Beginner vs Experienced differs significantly ',p[1])
	print(fxsize(medium['beginner']['subjectivity'],medium['experienced']['subjectivity']))
print('\n')
p = mannwhitneyu(medium['intermediate']['subjectivity'], medium['experienced']['subjectivity'])
print p
if(p[1] <= 0.05):
	print('Intermediate vs Experienced differs significantly ',p[1])
	print(fxsize(medium['intermediate']['subjectivity'],medium['experienced']['subjectivity']))

print('\n\nDifficult') 
p = mannwhitneyu(difficult['novice']['subjectivity'], difficult['beginner']['subjectivity'])
print p
if(p[1] <= 0.05):
	print('Novice vs Beginner differs significantly ',p[1])
	print(fxsize(difficult['novice']['subjectivity'],difficult['beginner']['subjectivity']))
p = mannwhitneyu(difficult['novice']['subjectivity'], difficult['intermediate']['subjectivity'])
print p
if(p[1] <= 0.05):
	print('Novice vs Intermediate differs significantly ',p[1])
	print(fxsize(difficult['novice']['subjectivity'],difficult['intermediate']['subjectivity']))
p = mannwhitneyu(difficult['novice']['subjectivity'], difficult['experienced']['subjectivity'])
print p
if(p[1] <= 0.05):
	print('Novice vs Experienced differs significantly ',p[1])
	print(fxsize(difficult['novice']['subjectivity'],difficult['experienced']['subjectivity']))
print('\n')
p = mannwhitneyu(difficult['beginner']['subjectivity'], difficult['intermediate']['subjectivity'])
print p
if(p[1] <= 0.05):
	print('Beginner vs Intermediate differs significantly ',p[1])
	print(fxsize(difficult['beginner']['subjectivity'],difficult['intermediate']['subjectivity']))
p = mannwhitneyu(difficult['beginner']['subjectivity'], difficult['experienced']['subjectivity'])
print p
if(p[1] <= 0.05):
	print('Beginner vs Experienced differs significantly ',p[1])
	print(fxsize(difficult['beginner']['subjectivity'],difficult['experienced']['subjectivity']))
print('\n')
p = mannwhitneyu(difficult['intermediate']['subjectivity'], difficult['experienced']['subjectivity'])
print p
if(p[1] <= 0.05):
	print('Intermediate vs Experienced differs significantly ',p[1])
	print(fxsize(difficult['intermediate']['subjectivity'],medium['experienced']['subjectivity']))

print('\n\t----------------On Polarity Score------------------\n')
print('Easy') 
p = mannwhitneyu(easy['novice']['polarity'], easy['beginner']['polarity'])
print p
if(p[1] <= 0.05):
	print('Novice vs Beginner differs significantly ',p[1])
	print(fxsize(easy['novice']['polarity'],easy['beginner']['polarity']))
p = mannwhitneyu(easy['novice']['polarity'], easy['intermediate']['polarity'])
print p
if(p[1] <= 0.05):
	print('Novice vs Intermediate differs significantly ',p[1])
	print(fxsize(easy['novice']['polarity'],easy['intermediate']['polarity']))
p = mannwhitneyu(easy['novice']['polarity'], easy['experienced']['polarity'])
print p
if(p[1] <= 0.05):
	print('Novice vs Experienced differs significantly ',p[1])
	print(fxsize(easy['novice']['polarity'],easy['experienced']['polarity']))
print('\n')
p = mannwhitneyu(easy['beginner']['polarity'], easy['intermediate']['polarity'])
print p
if(p[1] <= 0.05):
	print('Beginner vs Intermediate differs significantly ',p[1])
	print(fxsize(easy['beginner']['polarity'],easy['intermediate']['polarity']))
p = mannwhitneyu(easy['beginner']['polarity'], easy['experienced']['polarity'])
print p
if(p[1] <= 0.05):
	print('Beginner vs Experienced differs significantly ',p[1])
	print(fxsize(easy['beginner']['polarity'],easy['experienced']['polarity']))
print('\n')
p = mannwhitneyu(easy['intermediate']['polarity'], easy['experienced']['polarity'])
print p
if(p[1] <= 0.05):
	print('Intermediate vs Experienced differs significantly ',p[1])
	print(fxsize(easy['intermediate']['polarity'],easy['experienced']['polarity']))


print('\n\nMedium') 
p = mannwhitneyu(medium['novice']['polarity'], medium['beginner']['polarity'])
print p
if(p[1] <= 0.05):
	print('Novice vs Beginner differs significantly ',p[1])
	print(fxsize(medium['novice']['polarity'],medium['beginner']['polarity']))
p = mannwhitneyu(medium['novice']['polarity'], medium['intermediate']['polarity'])
print p
if(p[1] <= 0.05):
	print('Novice vs Intermediate differs significantly ',p[1])
	print(fxsize(medium['novice']['polarity'],medium['intermediate']['polarity']))
p = mannwhitneyu(medium['novice']['polarity'], medium['experienced']['polarity'])
print p
if(p[1] <= 0.05):
	print('Novice vs Experienced differs significantly ',p[1])
	print(fxsize(medium['novice']['polarity'],medium['experienced']['polarity']))
print('\n')
p = mannwhitneyu(medium['beginner']['polarity'], medium['intermediate']['polarity'])
print p
if(p[1] <= 0.05):
	print('Beginner vs Intermediate differs significantly ',p[1])
	print(fxsize(medium['beginner']['polarity'],medium['intermediate']['polarity']))
p = mannwhitneyu(medium['beginner']['polarity'], medium['experienced']['polarity'])
print p
if(p[1] <= 0.05):
	print('Beginner vs Experienced differs significantly ',p[1])
	print(fxsize(medium['beginner']['polarity'],medium['experienced']['polarity']))
print('\n')
p = mannwhitneyu(medium['intermediate']['polarity'], medium['experienced']['polarity'])
print p
if(p[1] <= 0.05):
	print('Intermediate vs Experienced differs significantly ',p[1])
	print(fxsize(medium['intermediate']['polarity'],medium['intermediate']['polarity']))

print('\n\nDifficult') 
# p = mannwhitneyu([np.mean(difficult['novice']['polarity'])], [np.mean(difficult['beginner']['polarity'])])
# print p
p = mannwhitneyu(difficult['novice']['polarity'], difficult['beginner']['polarity'])
print p
if(p[1] <= 0.05):
	print('Novice vs Beginner differs significantly ',p[1])
	print(fxsize(difficult['novice']['polarity'],difficult['beginner']['polarity']))
p = mannwhitneyu(difficult['novice']['polarity'], difficult['intermediate']['polarity'])
print p
if(p[1] <= 0.05):
	print('Novice vs Intermediate differs significantly ',p[1])
	print(fxsize(difficult['novice']['polarity'],difficult['intermediate']['polarity']))
p = mannwhitneyu(difficult['novice']['polarity'], difficult['experienced']['polarity'])
print p
if(p[1] <= 0.05):
	print('Novice vs Experienced differs significantly ',p[1])
	print(fxsize(difficult['novice']['polarity'],difficult['experienced']['polarity']))
print('\n')
p = mannwhitneyu(difficult['beginner']['polarity'], difficult['intermediate']['polarity'])
print p
if(p[1] <= 0.05):
	print('Beginner vs Intermediate differs significantly ',p[1])
	print(fxsize(difficult['beginner']['polarity'],difficult['intermediate']['polarity']))
p = mannwhitneyu(difficult['beginner']['polarity'], difficult['experienced']['polarity'])
print p
if(p[1] <= 0.05):
	print('Beginner vs Experienced differs significantly ',p[1])
	print(fxsize(difficult['beginner']['polarity'],difficult['experienced']['polarity']))
print('\n')
p = mannwhitneyu(difficult['intermediate']['polarity'], difficult['experienced']['polarity'])
print p
if(p[1] <= 0.05):
	print('Intermediate vs Experienced differs significantly ',p[1])
	print(fxsize(difficult['intermediate']['polarity'],difficult['experienced']['polarity']))

print('\n\t----------------On No of Words---------------------\n')
print('Easy') 
p = mannwhitneyu(easy['novice']['word_count'], easy['beginner']['word_count'])
print p
if(p[1] <= 0.05):
	print('Novice vs Beginner differs significantly ',p[1])
	print(fxsize(easy['novice']['word_count'],easy['beginner']['word_count']))
p = mannwhitneyu(easy['novice']['word_count'], easy['intermediate']['word_count'])
print p
if(p[1] <= 0.05):
	print('Novice vs Intermediate differs significantly ',p[1])
	print(fxsize(easy['novice']['word_count'],easy['intermediate']['word_count']))
p = mannwhitneyu(easy['novice']['word_count'], easy['experienced']['word_count'])
print p
if(p[1] <= 0.05):
	print('Novice vs Experienced differs significantly ',p[1])
	print(fxsize(easy['novice']['word_count'],easy['experienced']['word_count']))
print('\n')
p = mannwhitneyu(easy['beginner']['word_count'], easy['intermediate']['word_count'])
print p
if(p[1] <= 0.05):
	print('Beginner vs Intermediate differs significantly ',p[1])
	print(fxsize(easy['beginner']['word_count'],easy['intermediate']['word_count']))
p = mannwhitneyu(easy['beginner']['word_count'], easy['experienced']['word_count'])
print p
if(p[1] <= 0.05):
	print('Beginner vs Experienced differs significantly ',p[1])
	print(fxsize(easy['beginner']['word_count'],easy['experienced']['word_count']))
print('\n')
p = mannwhitneyu(easy['intermediate']['word_count'], easy['experienced']['word_count'])
print p
if(p[1] <= 0.05):
	print('Intermediate vs Experienced differs significantly ',p[1])
	print(fxsize(easy['intermediate']['word_count'],easy['experienced']['word_count']))


print('\n\nMedium') 
p = mannwhitneyu(medium['novice']['word_count'], medium['beginner']['word_count'])
print p
if(p[1] <= 0.05):
	print('Novice vs Beginner differs significantly ',p[1])
	print(fxsize(medium['novice']['word_count'],medium['beginner']['word_count']))
p = mannwhitneyu(medium['novice']['word_count'], medium['intermediate']['word_count'])
print p
if(p[1] <= 0.05):
	print('Novice vs Intermediate differs significantly ',p[1])
	print(fxsize(medium['novice']['word_count'],medium['intermediate']['word_count']))
p = mannwhitneyu(medium['novice']['word_count'], medium['experienced']['word_count'])
print p
if(p[1] <= 0.05):
	print('Novice vs Experienced differs significantly ',p[1])
	print(fxsize(medium['novice']['word_count'],medium['experienced']['word_count']))
print('\n')
p = mannwhitneyu(medium['beginner']['word_count'], medium['intermediate']['word_count'])
print p
if(p[1] <= 0.05):
	print('Beginner vs Intermediate differs significantly ',p[1])
	print(fxsize(medium['beginner']['word_count'],medium['intermediate']['word_count']))
p = mannwhitneyu(medium['beginner']['word_count'], medium['experienced']['word_count'])
print p
if(p[1] <= 0.05):
	print('Beginner vs Experienced differs significantly ',p[1])
	print(fxsize(medium['beginner']['word_count'],medium['experienced']['word_count']))
print('\n')
p = mannwhitneyu(medium['intermediate']['word_count'], medium['experienced']['word_count'])
print p
if(p[1] <= 0.05):
	print('Intermediate vs Experienced differs significantly ',p[1])
	print(fxsize(medium['intermediate']['word_count'],medium['experienced']['word_count']))

print('\n\nDifficult') 
# p = mannwhitneyu([np.mean(difficult['novice']['polarity'])], [np.mean(difficult['beginner']['polarity'])])
# print p
p = mannwhitneyu(difficult['novice']['word_count'], difficult['beginner']['word_count'])
print p
if(p[1] <= 0.05):
	print('Novice vs Beginner differs significantly ',p[1])
	print(fxsize(difficult['novice']['word_count'],difficult['beginner']['word_count']))
p = mannwhitneyu(difficult['novice']['word_count'], difficult['intermediate']['word_count'])
print p
if(p[1] <= 0.05):
	print('Novice vs Intermediate differs significantly ',p[1])
	print(fxsize(difficult['novice']['word_count'],difficult['intermediate']['word_count']))
p = mannwhitneyu(difficult['novice']['word_count'], difficult['experienced']['word_count'])
print p
if(p[1] <= 0.05):
	print('Novice vs Experienced differs significantly ',p[1])
	print(fxsize(difficult['novice']['word_count'],difficult['experienced']['word_count']))
print('\n')
p = mannwhitneyu(difficult['beginner']['word_count'], difficult['intermediate']['word_count'])
print p
if(p[1] <= 0.05):
	print('Beginner vs Intermediate differs significantly ',p[1])
	print(fxsize(difficult['beginner']['word_count'],difficult['intermediate']['word_count']))
p = mannwhitneyu(difficult['beginner']['word_count'], difficult['experienced']['word_count'])
print p
if(p[1] <= 0.05):
	print('Beginner vs Experienced differs significantly ',p[1])
	print(fxsize(difficult['beginner']['word_count'],difficult['experienced']['word_count']))
print('\n')
p = mannwhitneyu(difficult['intermediate']['word_count'], difficult['experienced']['word_count'])
print p
if(p[1] <= 0.05):
	print('Intermediate vs Experienced differs significantly ',p[1])
	print(fxsize(difficult['intermediate']['word_count'],difficult['experienced']['word_count']))




