 #!/usr/bin/python  
import csv, sys, time, datetime, json, elasticsearch
from elasticsearch import Elasticsearch
from datetime import datetime,timedelta
from csv import reader
es=Elasticsearch([{'host':'192.168.40.50'}])  
csvfile = '/data/nfsen/csvbackup/20151006MNALLDAY.csv'    
jdata = dict()  
actions = list()  
i = 0  
with open(csvfile, 'rb') as file :
	line = csv.reader(file, delimiter = ',', skipinitialspace = 'True')
	for row in line : 
		if len(row[0])== 23:
			if "M" in row[5]: 
				i += 1
				date = datetime.strptime(row[0],"%Y-%m-%d %H:%M:%S.%f")
				dategmt = initdate + timedelta(hours=4)
				row51 = row[5].rstrip(' M')
				row5 = float(row51)*1000000
				jdata = {'TimeofEvent': dategmt, 'SourceAddress': row[1], 'SourcePort': row[2], 'DestinationAddress': row[3], 'DestinationPort': row[4], 'BytesTransferred': row5, 'Packets': row[6], 'Output': row[7], 'Protocol': row[8]}
				#es.index(index:'netflow', doc_type:'Manhattan',id:i, body:jdata)
				es.index(index='netflow', doc_type='Manhattan',id=i, body=jdata)	
			else:
				i += 1
				date = datetime.strptime(row[0],"%Y-%m-%d %H:%M:%S.%f")
				dategmt = initdate + timedelta(hours=4)
				jdata = {'TimeofEvent': dategmt, 'SourceAddress': row[1], 'SourcePort': row[2], 'DestinationAddress': row[3], 'DestinationPort': row[4], 'BytesTransferred': row[5], 'Packets': row[6], 'Output': row[7], 'Protocol': row[8]}  
				#es.index(index:'netflow', doc_type:'Manhattan',id:i, body:jdata)
				es.index(index='netflow', doc_type='Manhattan',id=i, body=jdata)