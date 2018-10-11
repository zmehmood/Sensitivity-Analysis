# coding: utf-8

import json
import datetime


def handler(event, context):
    if event is not None:
        data = {
            'event': str(event['body']),
            'timestamp': datetime.datetime.utcnow().isoformat()
            
        }
    else:
        data = {
            'event': str(event),
            'timestamp': datetime.datetime.utcnow().isoformat()
            
        }
    
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
