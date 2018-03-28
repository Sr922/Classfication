import csv
import psycopg2

class Generation:
	# def __init__(self):

	def generate_developers_ids(self):
		analysis_reader = csv.reader(open('./DataSet/Mar-21/analysis.csv', 'rU'), delimiter= ",")

		answers = []
		for line in analysis_reader:
			if(len(line) >= 7):
				answers.append({'question_type' : line[1], 'wordCount' : line[3], 'polarity': line[4],'subjectivity' : line[5], 'developer' : line[6], 'developer experience' :line[7], 'question_id' : line[0]})

		developers = []
		for answer in answers:
			if answer['developer'] not in developers:
				developers.append(answer['developer'])

		with open('./DataSet/Mar-21/developer_ids.csv', 'w') as csvfile:
		    output_writer = csv.writer(csvfile, delimiter=',')
		    output_writer.writerow(developers)

	def generate_developers_all_posts(self):
		analysis_reader = csv.reader(open('./DataSet/Mar-21/developer_ids.csv', 'rU'), delimiter= ",")

		developers = []
		for line in analysis_reader:
			developers.append(line)

		developers = developers[0]
		db = psycopg2.connect("host='localhost' dbname=stackoverflow user=postgres password='sindhu93'")
		cur = db.cursor()
		query = 'Select * from posts where owneruserid in ('+ (',').join(developers) +') order by creationdate'
		cur.execute(query)

		with open('./DataSet/Mar-21/developers_all_posts.csv', 'w') as csvfile:
		    output_writer = csv.writer(csvfile, delimiter=',')
		    for line in cur:
		    	output_writer.writerow(line)

	def generate_all_developers_rofile_to_check_my_claim(self):
		db = psycopg2.connect("host='localhost' dbname=stackoverflow user=postgres password='sindhu93'")
		cur = db.cursor()
		query = 'Select id, reputation, creationdate, lastaccessdate, upvotes, downvotes, views from users LIMIT 200000'
		cur.execute(query)

		with open('../my_separate_experiments/DataSet/Mar-21/developers_all_posts.csv', 'w') as csvfile:
		    output_writer = csv.writer(csvfile, delimiter=',')
		    for line in cur:
		    	output_writer.writerow(line)

# generate_developers_ids()
# generate_developers_all_posts()
