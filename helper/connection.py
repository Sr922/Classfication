# -*- coding: utf-8 -*-
from __future__ import print_function
import psycopg2, time

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

class Postgres:
    def __init__(self):
        self.db1 = psycopg2.connect("host='localhost' dbname=stackoverflow user=postgres password='sindhu93'")
        self.cur = self.db1.cursor()
	
    def save(self, statement):
        self.cur.execute(statement)
    	self.db1.commit()
    
    def getAnswers(self, domain):
    	record = []
    	print('Quering.....')
        #query = 'Select * from posts p2 where p2.parentid in (select p.id from posts p inner join PostTags pt on pt.postid = p.id inner join tags t on t.id = pt.TagId and ( t.tagname = \'java\')  where p.posttypeid = 1);'
    	query = 'SELECT * from posts p where p.parentid in (select id from posts p2 where p2.tags Like \'%<'+domain+'>%\') LIMIT 700000'
        print(query)
        self.cur.execute(query);
    	i=0;
        for data in self.cur:
            record.append(data)
            
        return record
  	
    def read(self, user_id):
    	record = []
        if user_id != '':
            query = 'SELECT * FROM users WHERE id ='+str(user_id)
            self.cur.execute(query)
            for data in self.cur:
        		record.append(data)
        		#print(data)
	return record

    def getPostsOfDeveoperInTimeFrame(self, user_id, start_date, end_date):
        record = []
        query = 'SELECT id, parentid from posts where creationdate between \''+str(start_date)+'\' and \''+str(end_date)+'\' and owneruserid = '+str(user_id)+' and posttypeid =2'
        print(query)
        self.cur.execute(query)
        for data in self.cur:
            record.append(data)

        print(record)
        return record

    def getTagsOfPost(self, parent_id):
        record = []
        #query = 'SELECT tagName from tags where id in (select tagid from posttags where postid in ('+str(parent_id)+'))'
        query = 'Select tags from posts where id = '+str(parent_id)
        self.cur.execute(query)
        for data in self.cur:
            record.append(data)

        return record
