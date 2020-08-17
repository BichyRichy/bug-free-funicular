import requests
import json
import time
import random

url = 'http://perfsonar.nautilus.optiputer.net/esmond/perfsonar/archive/'
usr = 'user'
key = '589002f2b2931316ce79b7d9ac61ea363cfb6d75'
headers = {'Content-Type': 'application/json', 'Authorization': 'Token 589002f2b2931316ce79b7d9ac61ea363cfb6d75'}

payload = {
    "subject-type": "point-to-point",
    "source": "1.1.1.1",
    "destination": "1.1.1.1",
    "tool_name": "pscheduler/iperf3",
    "measurement_agent": "1.1.1.1",
    "input_source": "src",
    "input_destination": "dest",
    "time_duration": 30,
    "ip_transport_protocol": "tcp",
    "event-types": [
        {
            "event-type": "throughput",
            "summaries": [
                {
                    "summary-type": "aggregation",
                    "summary-window": 3600
                },
                {
                    "summary-type": "aggregation",
                    "summary-window": 86400
                }
            ]
        }
    ]
}
m = requests.post(url, json=payload, headers=headers)
returnJSON = m.json()
metadataKey = returnJSON['metadata-key']

dat = {
    "ts": str(int(time.time())),
    "val": 1000000000
}
d = requests.post("{0}{1}/throughput/base".format(url,metadataKey), json=dat, headers=headers)

print "ni"