import MySQLdb
import csv,datetime,sys

nfdumploc = '/home/user/'
shortname = sys.argv[1]
filename = nfdumploc + shortname + '.csv'

if "MN" in shortname:
	dbdescriptor = "netflowMN"
elif "FL" in shortname:
	dbdescriptor = "netflowFL"
elif "BY" in shortname:
	dbdescriptor = "netflowBY"
elif "BX" in shortname:
	dbdescriptor = "netflowBX"		
print dbdescriptor
netflowdb = MySQLdb.connect(host="localhost", user="root", passwd="password", db="netflow")
cursor = netflowdb.cursor()
with open(filename, 'rb') as netflowin:
	reader = csv.reader(netflowin,delimiter=',', skipinitialspace='True')
	for row in reader:
		if len(row[0])== 23:
			if "M" in row[5]: 
				row5stripped = row[5].rstrip(' M')
				row5 = float(row5stripped)*1000000
				sql = "INSERT INTO "+dbdescriptor+"(timeofflow,sourceip,sourceport,destinationip,destinationport,bytes,packets,totaloutput,protocol) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);" 
				Data = (row[0],row[1],row[2],row[3],row[4],row5,row[6],row[7],row[8])
				cursor.execute(sql,Data)
			else:
				sql = "INSERT INTO "+dbdescriptor+"(timeofflow,sourceip,sourceport,destinationip,destinationport,bytes,packets,totaloutput,protocol) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
				#Data = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
				cursor.execute(sql,row)
        else:
            print row[0]
#netflowdb.commit()
#cursor.close()
#netflowdb.close()
print "Done"

