import csv
import psycopg2

reader = csv.reader(open('./DataSet/Classified.csv', 'rU'), delimiter= ",")

db = psycopg2.connect("host='localhost' dbname=stackoverflow user=postgres password='sindhu93'")
cur = db.cursor()

for line in reader:
	if(line[0] != '' and line[0] != 'Id'):
		query = 'UPDATE posts SET difficulty_level = \''+line[3]+'\' WHERE id = '+line[0]+''
		print query
		cur.execute(query)
		db.commit()


