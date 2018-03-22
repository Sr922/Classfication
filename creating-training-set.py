import psycopg2
import csv
from bs4 import BeautifulSoup
from sklearn.cluster import KMeans
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

db = psycopg2.connect("host='localhost' dbname=stackoverflow user=postgres password='sindhu93'")
cur = db.cursor()
query = 'select id,title, body from posts p2 where p2.tags Like \'%<java>%\' and p2.posttypeid=1  and p2.difficulty_level is null LIMIT 40000'
cur.execute(query)

record = []
for line in cur:
	#record.append(data)
	body = line[1] + line[2]
	temp = []
	temp.append(line[0])
	#temp.append(line[2])
	temp.append(body)
	record.append(temp)
	
with open('./DataSet/toClassify.csv', 'w') as csvfile:
    output_writer = csv.writer(csvfile, delimiter=',',
                            )
    output_writer.writerow(['Id','Body'])

    for line in record:
    	output_writer.writerow(line)

# query = 'select id,title, body, difficulty_level from posts p2 where p2.tags Like \'%<java>%\' and p2.posttypeid=1  and p2.difficulty_level is not null'
# cur.execute(query)

# record = []
# for line in cur:
# 	#record.append(data)
# 	body = line[1] + line[2]
# 	temp = []
# 	temp.append(line[0])
# 	#temp.append(line[2])
# 	temp.append(line[3])
# 	temp.append(body)
# 	record.append(temp)
	
# with open('./DataSet/training-data.csv', 'w') as csvfile:
#     output_writer = csv.writer(csvfile, delimiter=',',
#                             )
#     output_writer.writerow(['Id','Body', 'Difficulty Level'])

#     for line in record:
#     	output_writer.writerow(line)


# reader = csv.reader(open('./DataSet/ForBasicStudy.csv', 'rU'), delimiter= ",")
# record = []
# for line in reader:
#     #output_writer.writerow(line)
#     record.append(line)

# print record[0]

# with open('./DataSet/toUpload.csv', 'w') as csvfile:
#     output_writer = csv.writer(csvfile, delimiter=',',
#                             )
#     output_writer.writerow(['Id','Text', 'Category'])

#     for line in record:
#     	if line[0] != 'Id':
#     		body = BeautifulSoup(line[2]).get_text().encode('utf-8', 'ignore')
#     		text = line[1] + body
#     		output_writer.writerow([line[0], text, line[4]])
#     	#print line
