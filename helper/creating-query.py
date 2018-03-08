import csv

def get_parent_id():
	questionsReader = csv.reader(open('./DataSet/100KJava Questions.csv', 'rU'), delimiter= ",")

	all_ids = []
	i = 0
	for line in questionsReader:
		# # print line[0] == 406533
		# # if(line[0] == '2724885'):
		# # 	print(i)
		# if(i >= 46103):
		all_ids.append(line[0])
		# i =i+1

	print len(all_ids)
	id_chunks = [all_ids[i:i+1500] for i in range(1, len(all_ids), 1500)]

	#print len(id_chunks)
	queries = []
	for ids in id_chunks:
		query = 'SELCT * FROM POSTS WHERE PARENTID IN ('+', '.join(ids)+');'
		queries.append([query])

	print queries

	with open('./DataSet/queries.csv', 'w') as csvfile:
	    output_writer = csv.writer(csvfile, delimiter=':',
	                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
	    for query in queries:
	    	output_writer.writerow(query)

def get_developers_id():
	answersReader = csv.reader(open('/Volumes/SINDHU/Thesis/AnswersFor100KQuestions.csv', 'rU'), delimiter= ",")
	all_ids = []
	for line in answersReader:
		if line[9] not in all_ids:
			all_ids.append(line[9])	

	print len(all_ids)

	query = 'SELECT * FROM USERS WHERE ID IN ('+', '.join(all_ids)+');'

	with open('./DataSet/queries.csv', 'w') as csvfile:
	    output_writer = csv.writer(csvfile, delimiter=':',
	                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
	    output_writer.writerow([query])
	 
get_developers_id()