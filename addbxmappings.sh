curl -XPUT 'localhost:9200/netflow/_mappings/Bronx' -d '
{  
"Bronx": {  
"_all" : {"enabled" : false},  
"_source" : {"enabled" : false},  
"properties": {  
    "TimeofEvent": {"type": "date", "format" : "date_hour_minute_second"},  
    "SourceAddress": {"type": "ip"},  
    "SourcePort": {"type": "integer", "index": "not_analyzed"},  
    "DestinationAddress": {"type": "ip"},  
    "DestinationPort": {"type": "float", "index": "not_analyzed"},  
    "BytesTransferred": {"type": "long"},  
    "Packets": {"type": "long"},  
    "Output": {"type": "integer"},  
    "Protocol": {"type": "string"}  
 }  
}  
}' 