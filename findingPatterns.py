import csv

analysis_reader = csv.reader(open('./DataSet/ToFindPatterns.csv', 'rU'), delimiter= ",")

rows = []
for line in analysis_reader:
	rows.append({'question_type' : line[1], 'wordCount' : line[3], 'polarity': line[4],'subjectivity' : line[5], 'developer experience' :line[7]})

patterns = []
polarity = {}
wordCount = {}
subjectivity = {}
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
	if(row['question_type'] == 'Easy' and row['developer experience'] == 'Experienced'):
		polarity['Experienced']['Easy'] = float(polarity['Experienced']['Easy']) + float(row['polarity'])
		subjectivity['Experienced']['Easy'] = float(subjectivity['Experienced']['Easy']) + float(row['subjectivity'])
		wordCount['Experienced']['Easy'] = float(wordCount['Experienced']['Easy']) + float(row['wordCount'])
		easy_exp_count = easy_exp_count+1;
	if(row['question_type'] == 'Medium' and row['developer experience'] == 'Experienced'):
		polarity['Experienced']['Medium'] = float(polarity['Experienced']['Easy']) + float(row['polarity'])
		subjectivity['Experienced']['Medium'] = float(subjectivity['Experienced']['Easy']) + float(row['subjectivity'])
		wordCount['Experienced']['Medium'] = float(wordCount['Experienced']['Easy']) + float(row['wordCount'])
		medium_exp_count = medium_exp_count+1;
	if(row['question_type'] == 'Difficult' and row['developer experience'] == 'Experienced'):
		polarity['Experienced']['Difficult'] = float(polarity['Experienced']['Easy']) + float(row['polarity'])
		subjectivity['Experienced']['Difficult'] = float(subjectivity['Experienced']['Easy']) + float(row['subjectivity'])
		wordCount['Experienced']['Difficult'] = float(wordCount['Experienced']['Easy']) + float(row['wordCount'])
		difficult_exp_count = difficult_exp_count+1;

	if(row['question_type'] == 'Easy' and row['developer experience'] == 'Intermediate'):
		polarity['Intermediate']['Easy'] = float(polarity['Intermediate']['Easy']) + float(row['polarity'])
		subjectivity['Intermediate']['Easy'] = float(subjectivity['Intermediate']['Easy']) + float(row['subjectivity'])
		wordCount['Intermediate']['Easy'] = float(wordCount['Intermediate']['Easy']) + float(row['wordCount'])
		easy_int_count = easy_int_count+1;
	if(row['question_type'] == 'Medium' and row['developer experience'] == 'Intermediate'):
		polarity['Intermediate']['Medium'] = float(polarity['Intermediate']['Easy']) + float(row['polarity'])
		subjectivity['Intermediate']['Medium'] = float(subjectivity['Intermediate']['Easy']) + float(row['subjectivity'])
		wordCount['Intermediate']['Medium'] = float(wordCount['Intermediate']['Easy']) + float(row['wordCount'])
		medium_int_count = medium_int_count+1;
	if(row['question_type'] == 'Difficult' and row['developer experience'] == 'Intermediate'):
		polarity['Intermediate']['Difficult'] = float(polarity['Intermediate']['Easy']) + float(row['polarity'])
		subjectivity['Intermediate']['Difficult'] = float(subjectivity['Intermediate']['Easy']) + float(row['subjectivity'])
		wordCount['Intermediate']['Difficult'] = float(wordCount['Intermediate']['Easy']) + float(row['wordCount'])
		difficult_int_count = difficult_int_count+1;

	if(row['question_type'] == 'Easy' and row['developer experience'] == 'Beginner'):
		polarity['Beginner']['Easy'] = float(polarity['Beginner']['Easy']) + float(row['polarity'])
		subjectivity['Beginner']['Easy'] = float(subjectivity['Beginner']['Easy']) + float(row['subjectivity'])
		wordCount['Beginner']['Easy'] = float(wordCount['Beginner']['Easy']) + float(row['wordCount'])
		easy_beg_count = easy_beg_count+1;
	if(row['question_type'] == 'Medium' and row['developer experience'] == 'Beginner'):
		polarity['Beginner']['Medium'] = float(polarity['Beginner']['Easy']) + float(row['polarity'])
		subjectivity['Beginner']['Medium'] = float(subjectivity['Beginner']['Easy']) + float(row['subjectivity'])
		wordCount['Beginner']['Medium'] = float(wordCount['Beginner']['Easy']) + float(row['wordCount'])
		medium_beg_count = medium_beg_count+1;
	if(row['question_type'] == 'Difficult' and row['developer experience'] == 'Beginner'):
		polarity['Beginner']['Difficult'] = float(polarity['Beginner']['Easy']) + float(row['polarity'])
		subjectivity['Beginner']['Difficult'] = float(subjectivity['Beginner']['Easy']) + float(row['subjectivity'])
		wordCount['Beginner']['Difficult'] = float(wordCount['Beginner']['Easy']) + float(row['wordCount'])
		difficult_beg_count = difficult_beg_count+1;


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
    print('Avg subjectivity value of Beginner users answer to medium questions ', subjectivity['Beginner']['Difficult']/difficult_beg_count)
except ZeroDivisionError:
    print('Avg subjectivity value of Beginner users answer to medium questions ', 0)




