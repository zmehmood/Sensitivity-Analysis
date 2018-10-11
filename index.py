# coding: utf-8

import json
import datetime


def handler(event, context):
    data = {
        'event': str(event),
        'timestamp': datetime.datetime.utcnow().isoformat()
        'context':str(context)
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
