import requests
import json
import csv

def get_creation_date(user_id):
	print user_id
	r = requests.get("https://api.stackexchange.com/2.2/users/"+str(user_id)+"?order=desc&sort=reputation&site=stackoverflow")
	dev = json.loads(r.content)
	print dev
	#print dev[0]['creation_date']
	return dev['items'][0]['creation_date']

answersReader = csv.reader(open('/Volumes/SINDHU/Thesis/AnswersFor100KQuestions.csv', 'rU'), delimiter= ",")

with open('/Volumes/SINDHU/Thesis/UpdatedAnswersFor100KQuestions.csv', 'w') as csvfile:
    output_writer = csv.writer(csvfile)
    output_writer.writerow(['Id','PostTypeId','AcceptedAnswerId','ParentId','CreationDate','DeletionDate','Score','ViewCount','Body','OwnerUserId','OwnerDisplayName','LastEditorUserId','LastEditorDisplayName','LastEditDate','LastActivityDate','Title','Tags','AnswerCount','CommentCount','FavoriteCount','ClosedDate','CommunityOwnedDate', 'MemberSince'])
    for line in answersReader:
    	if(line[9] != 'OwnerUserId'):
    		outputline = []
    		outputline = line
    		outputline.append(get_creation_date(line[9]))
    		output_writer.writerow(outputline)