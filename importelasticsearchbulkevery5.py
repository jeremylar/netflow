 #!/usr/bin/python  
import csv, sys, time, datetime, json, elasticsearch,subprocess, os
from elasticsearch import Elasticsearch, helpers
from elasticsearch.helpers import bulk
from csv import reader
elasticsearchhost = "192.168.40.50"  #enter in host IP address or use sys.argv to feed in IP
es=Elasticsearch([{'host':elasticsearchhost}])
loc = sys.argv[1]

def location(locs):
	if "by" in locs:
		loctype = "Bayside"
		router = "BY-XO-Router"
	elif "mn" in locs:
		loctype = "Manhattan"
		router = "MN-XO-Router"
	elif "bx" in locs:
		loctype = "Bronx"
		router = "BX-XO-Router"
	elif "fl" in locs:
		loctype = "Flushing"
		router = "FL-XO-Router"	
	return [loctype,router];
	
loctype = location(loc)[0]
router = location(loc)[1]

def csvfile(location):
	year = str(gettime()[0])
	month = str(gettime()[1])
	day = str(gettime()[2])
	hour = str(gettime()[3])
	newnowminutes = str(gettime()[5])
	csvfile = str("/data/nfsen/csvbackup/"+loctype+year+month+day+hour+newnowminutes+".csv")
	return csvfile;

def gettime():
	timenow = datetime.datetime.now() #find current time
	timebefore = timenow - datetime.timedelta(minutes=10) #find time five minutes ago
	timebeforestr = str(timebefore) #set time five minutes ago to string
	year = str(timebefore.year) #find year five mintues ago 
	month = str(timebefore.month) #find month five mintues ago 
	day = str(timebefore.day) #find day five mintues ago
	nowminutes = int(timebefore.minute) #find minutes five mintues ago 
	if (nowminutes-(nowminutes%5)) < 10:
		newnowminutes = ("0"+str(nowminutes-(nowminutes%5)))
	else:
		newnowminutes = str(nowminutes-(nowminutes%5)) #set time 5 minutes ago to minutes as 0 or 5 rounding down
	if (timebefore.hour) < 10:
		hour = ("0"+str(timebefore.hour))
	else:
		hour = str(timebefore.hour)#find hour five mintues ago 
	if (timebefore.day) < 10:
		day = ("0"+str(timebefore.day))
	else:
		day = str(timebefore.day)#find day five mintues ago	
	if (timebefore.month) < 10:
		month = ("0"+str(timebefore.month))
	else:
		month = str(timebefore.month)#find month five mintues ago 	
	return year,month,day,hour,nowminutes,newnowminutes;
	
def runnfdump(loc,loctype,router,saveloc):
	year = str(gettime()[0])
	month = str(gettime()[1])
	day = str(gettime()[2])
	hour = str(gettime()[3])
	newnowminutes = str(gettime()[5])
	prog = "/home/nfsen/nfdump/nfdump-1.6.13/bin/nfdump -r " #executable of nfdump
	startloc= str("/data/nfsen/profiles-data/live/"+router+"/"+year+"/"+month+"/"+day+"/nfcapd."+year+month+day+hour+newnowminutes) #location of file to be processed via nfdump
	nfdumpargs = " -o " #format of nfdump
	nfdumpargs2 = str("\"fmt:%ts, %sa, %sp, %da, %dp, %byt, %pkt, %out, %pr\" > ") #format of nfdump
	command = str(prog+startloc+nfdumpargs+nfdumpargs2+saveloc)  #execute shell command
	subprocess.call(command,shell=True)   #execute shell command
	time.sleep(20)
	return;

def export(csvfilesave,loctype,elasticsearchhost,es):
	i = 0
	jdata = dict()  
	actions = list()
	year = str(gettime()[0])
	month = str(gettime()[1])
	day = str(gettime()[2])
	hour = str(gettime()[3])
	newnowminutes = str(gettime()[5])
	idstr = str(year+month+day+hour+newnowminutes+loctype)
	with open(csvfilesave, 'rb') as file :
		line = csv.reader(file, delimiter = ',', skipinitialspace = 'True')
		for row in line : 
			if len(row[0])== 23:
				if "M" in row[5]: 
					row51 = row[5].rstrip(' M')
					row5 = float(row51)*1000000
				elif "M" in row[6]:
					row61 = row[6].rstrip(' M')
					row6 = float(row61)*1000000
				elif "G" in row[5]:
					row51 = row[5].rstrip(' G')
					row5 = float(row51)*1000000000
				elif "G" in row[6]:
					row61 = row[6].rstrip(' G')
					row6 = float(row61)*1000000000
				else:
					row5 = row[5]
					row6 = row[6]
				i += 1
				index = (idstr) + str(i)
				initdate = datetime.datetime.strptime(str(row[0][0:19]),"%Y-%m-%d %H:%M:%S")
				dategmt = initdate + datetime.timedelta(hours=4)
				action = { '_index': 'netflow', '_type': 'Netflow', '_id': index, '_source': {"TimeofEvent": dategmt, "SourceAddress": row[1], "SourcePort": row[2], "DestinationAddress": row[3], "DestinationPort": row[4], "BytesTransferred": row5, "Packets": row6, "Output": row[7], "Protocol": row[8],"Location": loctype}}  
				actions.append(action)
			if i % 100000 == 0:
				elasticsearch.helpers.bulk(es,actions)
				actions = list()
		elasticsearch.helpers.bulk(es,actions)
	time.sleep(20)	
	return;	
	
csvfilesave = csvfile(loctype)
runnfdump(loc,loctype,router,csvfilesave);
export(csvfilesave,loctype,elasticsearchhost,es)
os.remove(csvfilesave)	#temp csvfile cleanup