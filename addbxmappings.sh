curl -XPUT 'localhost:9200/netflow/_mappings/Bronx' -d '
{  
"Bronx": {  
"_all" : {"enabled" : false},  
"_source" : {"enabled" : false},  
"properties": {  
    "TimeofEvent": {"type": "date", "format" : "yyyy-MM-dd HH:mm:ss.SSS"},  
    "SourceAddress": {"type": "ip"},  
    "SourcePort": {"type": "integer", "index": "not_analyzed"},  
    "DestinationAddress": {"type": "sip"},  
    "DestinationPort": {"type": "float", "index": "not_analyzed"},  
    "BytesTransferred": {"type": "long"},  
    "Packets": {"type": "long"},  
    "Output": {"type": "integer"},  
    "Protocol": {"type": "string"}  
 }  
}  
}' 