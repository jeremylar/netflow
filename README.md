# netflow
netflow with mysql and elasticsearch
These scripts will aid with the creation of a mysql database for netflow/nfdump data as well as python script to import the data into the mysql db or elasticsearch instance.
nfdump -R /"Daily directory for nfdump files to go through" -o "fmt:%ts, %sa, %sp, %da, %dp, %byt, %pkt, %out, %pr" > "Name of file to output to".csv
