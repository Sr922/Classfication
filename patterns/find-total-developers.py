import csv

analysis_reader = csv.reader(open('./DataSet/Mar-21/developer_ids.csv', 'rU'), delimiter= ",")

developers = []
for line in analysis_reader:
	developers.append(line)

developers = developers[0]
print len(developers)
# db = psycopg2.connect("host='localhost' dbname=stackoverflow user=postgres password='sindhu93'")
# cur = db.cursor()
# query = 'Select * from posts where owneruserid in ('+ (',').join(developers) +') order by creationdate'
# cur.execute(query)

# allPostsOfDevelopers = []
# for line in query:
# 	allPostsOfDevelopers.append(line)
