# -*- coding: utf-8 -*-
from __future__ import print_function
import psycopg2, time


class Postgres:
    def __init__(self):
        self.db1 = psycopg2.connect("host='localhost' dbname=stackoverflow user=postgres password='sindhu93'")
        self.cur = self.db1.cursor()
	
    def save(self, statement):
        self.cur.execute(statement)
    	self.db1.commit()

    def read(self, query):
    	record = []
    	self.cur.execute(query)
    	for data in self.cur:
    		record.append(data)
    		#print data

	return record
