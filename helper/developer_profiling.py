# -*- coding: utf-8 -*-
from __future__ import print_function
import urllib2
import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import datetime, date, time, timedelta
from connection import Postgres
from textblob import TextBlob


#answersReader = csv.reader(open('/home/ubuntu/Thesis/AnswersFor100KQuestions.csv', 'rU'), delimiter= ",")

# developersReader = csv.reader(open('/Volumes/SINDHU/Thesis/DevelopersIn100KDataSet.csv', 'rU'), delimiter= ",")
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

def getExperienceLevel(difference):
	if difference.years >= 0 and difference.years < 2:
		return 'Novice'
	elif difference.years >= 2 and difference.years < 5:
		return 'Beginner'
	elif difference.years >= 5 and difference.years < 7:
		return 'Intermediate'
	elif difference.years >= 7:
		return 'Experienced'
	else:
		return difference.years


ps = Postgres()
print('Loading Java Questions')
answersDetails = ps.getAnswers('java')
print('Loaded')

#print answersDetails
developers_details = {}
# # for line in developersReader:
# 	# if line[0] in developers_details:
# 	# 	developers_details[line[0]].append({'createdData' : line[2]})
# 	# else:
# 	# 	if line[0] != 'Id' and line[0] != ' ':
# 	# 		developers_details[line[0]] = []
# 	# 		developers_details[line[0]].append({'createdData' : line[2]})
# postgresCursor = Postgres()

profiles = {}

print('Structuring java answers and their developers details')
i=0
for answer in answersDetails:
 	if answer[8] in profiles:
 		profiles[answer[8]].append({'postedDate' : answer[4], 'answerId' : answer[0]})
 	else:
 		if answer[8] != 'OwnerUserId':
 			profiles[answer[8]] = []
 			profiles[answer[8]].append({'postedDate' : answer[4], 'answerId' : answer[0]})
			
	printProgressBar(i, len(answersDetails), prefix = 'Progress:', suffix = 'Complete', length = 50)
	i=i+1;
print('Structured java answers and their developers details')

# for developer in profiles:
# 	# print developer, 'has ', profiles[developer], '\n'
# 	# if developer == '':
# 	# 	print 'Something is wrong here'
# 	# else:
# 	# 	print developer, 'joined SO on ', developers_details[developer]

#  	for postsOfDev in profiles[developer]:
# # 		#print 'Post was created at ', postsOfDev['postedDate'];
#  		if developer != '' and developer != None:
#  			data = ps.read(developer)
#  			if(len(data)):
#  				start_date = data[0][4]
#  				end_date = postsOfDev['postedDate']
#  				difference = relativedelta(end_date, start_date)
# # 				# print 'experience while answering ', postsOfDev['answerId'], ' is ', difference.years, ' years ',difference.months,' months'  '\n'

#  				if difference.years >= 0 and difference.years < 2:
#  					postsOfDev['experienceLevel'] = 'Novice'
# # 					#developers_details[developer].append({'experienceLevel' : 'Novice'})
#  				elif difference.years >= 2 and difference.years < 5:
#  					postsOfDev['experienceLevel'] = 'Beginner'
# # 					#developers_details[developer].append({'experienceLevel' : 'Beginner'})
#  				elif difference.years >= 5 and difference.years < 7:
#  					postsOfDev['experienceLevel'] = 'Intermediate'
# # 					#developers_details[developer].append({'experienceLevel' : 'Intermediate'})
#  				elif difference.years >= 7:
#  					postsOfDev['experienceLevel'] = 'Experienced'
# # 					#developers_details[developer].append({'experienceLevel' : 'Experienced'})
#  				else:
#  					postsOfDev['experienceLevel'] = difference.years
#  			else:
#  				postsOfDev['experienceLevel'] = 'No record found for the developer'
#  		else:
#  			postsOfDev['experienceLevel'] = 'Cant be calculated since cant find the developer ID for these posts'

# # # Find when he first started writing posts in java
print('Calulating the date when the developer started posting stuffs on java domain')
i=0
for developer in profiles:
 	if developer != '':
 		minDate = profiles[developer][0]['postedDate']
 		for postsOfDev in profiles[developer]:
 			thisDate = postsOfDev['postedDate']
 			if( thisDate < minDate ):
 				minDate = thisDate
 		if developer in developers_details:
 			developers_details[developers_details].append({'javaExperienceStartsfrom' : minDate})
 		else:
 			developers_details[developer] = []
 			developers_details[developer].append({'javaExperienceStartsfrom' : minDate})
 	printProgressBar(i, len(profiles), prefix = 'Progress:', suffix = 'Complete', length = 50)
	i=i+1;

print('Found the date when the developer started posting stuffs on java domain')

# 		# developers_details[developer][0]['javaExperienceStartsfrom'] = minDate.strftime( "%m/%d/%Y %H:%M")

# for developer in developers_details:
#  	print developers_details[developer]

print('Starting to build the profiles.....')
with open('./All_Java_Developer_Profiles_On_Weekly_Basis.csv', 'w') as csvfile:
    output_writer = csv.writer(csvfile, delimiter=',',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    output_writer.writerow(['DeveloperId', 'Week', 'Start Date', 'End Date', 'Experience', '#Java ', '#Other Tech'])

    i=0;
    k=0;
    for developer in profiles:
		start_date = developers_details[developer][0]['javaExperienceStartsfrom']
		end_date = start_date + timedelta(days=7)

		weekCount = 0
		if(developer != None):
			while(end_date <= datetime.now()):
				tags = []
				javaCount = 0
				otherTechCount = 0
				weekCount = weekCount + 1
				# print("**************************")
				posts = ps.getPostsOfDeveoperInTimeFrame(developer, start_date, end_date) # I am considering only the answers now
				for post in posts:
					tags = ps.getTagsOfPost(post[1])
					# print(tags)
					# print("*************************")
					for tag in tags:
						if '<java>' in tag:
							javaCount = javaCount+1
						else:
							otherTechCount = otherTechCount + 1

				dev = ps.read(developer)
				#print(dev)
				if dev != None:
					developer_join_date = dev[0][2]
					difference = relativedelta(end_date, developer_join_date)
					experienceLevel = getExperienceLevel(difference)
				else:
					experienceLevel = 'No join date available'
				
				data = ([developer, weekCount, start_date, end_date, experienceLevel, javaCount, otherTechCount ])
				output_writer.writerow(data)
				start_date = end_date + timedelta(days=1)
				end_date = end_date + timedelta(days=7)
			

			if(end_date > datetime.now()):
				weekCount=weekCount+1
				end_date = datetime.now()
				# print("**************************")
				posts = ps.getPostsOfDeveoperInTimeFrame(developer, start_date, end_date) # I am considering only the answers now
				for post in posts:
					tags = ps.getTagsOfPost(post[1])
					# print(tags)
					# print('<java>' in tags)
					# print("*************************")
					for tag in tags:
						if '<java>' in tag:
							javaCount = javaCount+1
						else:
							otherTechCount = otherTechCount + 1

				dev = ps.read(developer)
				#print(dev)
				if dev != None:
					developer_join_date = dev[0][2]
					difference = relativedelta(end_date, developer_join_date)
					experienceLevel = getExperienceLevel(difference)
				else:
					experienceLevel = 'No join date available'
				
				data = ([developer, weekCount, start_date, end_date, experienceLevel, javaCount, otherTechCount ])
				output_writer.writerow(data)

			printProgressBar(i, len(profiles), prefix = 'Progress:', suffix = 'Complete', length = 50)
			i=i+1;
			k=k+1
		





