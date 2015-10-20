curl -XDELETE 'localhost:9200/netflow'
curl -XPUT 'localhost:9200/netflow'
curl -XPUT 'localhost:9200/netflow/_mappings/Netflow' -d '
{  
"Netflow": {  
"_all" : {"enabled" : false},  
"_source" : {"enabled" : false},  
"properties": {  
    "TimeofEvent": {"type": "date", "format" : "date_hour_minute_second"},  
    "SourceAddress": {"type": "ip","index": "analyzed"},  
    "SourcePort": {"type": "integer", "index": "not_analyzed"},  
    "DestinationAddress": {"type": "ip","index": "analyzed"},  
    "DestinationPort": {"type": "float", "index": "not_analyzed"},  
    "BytesTransferred": {"type": "long"},  
    "Packets": {"type": "long"},  
    "Output": {"type": "integer"},  
    "Protocol": {"type": "string","index": "analyzed"},
	"Location": {"type": "string","index": "analyzed"}	
 }  
}  
}'