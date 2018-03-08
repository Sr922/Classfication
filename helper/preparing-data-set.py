import csv

for i in range(0,31):
	file_name = '/Volumes/SINDHU/Thesis/temp storage files/QueryResults ('+str(i)+').csv'
	answersReader = csv.reader(open(file_name, 'rU'), delimiter= ",")
	# print file_name
	with open('/Volumes/SINDHU/Thesis/AnswersFor100KQuestions.csv', 'a') as csvfile:
	    output_writer = csv.writer(csvfile)
	    for line in answersReader:
			output_writer.writerow(line)
