 #!/usr/bin/python  
import csv, sys, time, datetime, json, elasticsearch
from elasticsearch import Elasticsearch, helpers
from elasticsearch.helpers import bulk
from datetime import datetime,timedelta
from csv import reader
elasticsearchhost = sys.argv[2]
es=Elasticsearch([{'host':elasticsearchhost}])
csvfile = sys.argv[1]  
jdata = dict()  
actions = list()  
i = 0  
with open(csvfile, 'rb') as file :
	line = csv.reader(file, delimiter = ',', skipinitialspace = 'True')
	for row in line : 
		if len(row[0])== 23:
			if "M" in row[5]: 
				row51 = row[5].rstrip(' M')
				row5 = float(row51)*1000000
			elif "G" in row[5]:
				row51 = row[5].rstrip(' G')
				row5 = float(row51)*1000000000
			else:
				row5 = row[5]
			i += 1
			initdate = datetime.strptime(str(row[0][0:19]),"%Y-%m-%d %H:%M:%S")
			dategmt = initdate + timedelta(hours=4)
			action = { '_index': 'netflow', '_type': 'Manhattan', '_id': i, '_source': {"TimeofEvent": dategmt, "SourceAddress": row[1], "SourcePort": row[2], "DestinationAddress": row[3], "DestinationPort": row[4], "BytesTransferred": row5, "Packets": row[6], "Output": row[7], "Protocol": row[8]}}  
			actions.append(action)
		if i % 100000 == 0:
			elasticsearch.helpers.bulk(es,actions)
			actions = list()
	elasticsearch.helpers.bulk(es,actions)