 #!/usr/bin/python  
import csv, sys, time, datetime, json, elasticsearch  
from elasticsearch import helpers
from datetime import datetime
from csv import reader
es      = elasticsearch.Elasticsearch()  
source    = '/home/user/20150826'  
csvfile   = source + '.csv'  
jdata    = dict()  
actions   = list()  
i = 0  

with open(csvfile, 'rb') as file :
	line = csv.reader(file, delimiter = ',', skipinitialspace = True)
	for row in line : 
		if row[0] == ':' or isinstance(row[0], basestring):
			i +=1
		else:	
			dateof = str(row[1:23])
			ptime = datetime.strptime(dateof, "%Y-%m-%d %H:%M:%S.%f")  
			# ctime = datetime.strftime('%Y-%m-%d %H:%M:%S.%f', ptime)  
			jdata = { 'ts': ptime, 'byte': int(row[5]), 'sa': row[1], 'sp': int(float(row[2])), 'da': row[3], 'dp': int(float(row[4])), 'pkt': int(row[6]), 'out': int(row[7]), 'pr': row[8].strip() }  
			action = { '_index': 'netflowlab', '_type': 'fnf1x', '_source': json.dumps(jdata, separators=(',', ':','.'))}  
			actions.append(action)  
			i += 1  
			if i % 100000 == 0:  
				elasticsearch.helpers.bulk(es, actions)  
				print "Indexed %d, working on next 100000" %(i)  
				actions = list()
	elasticsearch.helpers.bulk(es, actions)
	print "Indexed %d, finishing." %(i)
		