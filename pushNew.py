import requests
import json
import time

url = 'https://perfsonar.nautilus.optiputer.net/esmond/perfsonar/archive/'
key = '589002f2b2931316ce79b7d9ac61ea363cfb6d75'
headers = {'Content-Type': 'application/json', 'Authorization': 'Token 589002f2b2931316ce79b7d9ac61ea363cfb6d75'}

payload = {
    "subject-type": "point-to-point",
    "source": "10.1.1.1",
    "destination": "10.1.1.2",
    "tool-name": "pscheduler/iperf3",
    "measurement-agent": "1.1.1.1",
    "input-source": "test1.net",
    "input-destination": "test2.net",
    "event-types": [{"event-type": "throughput","summaries":[{"summary-type": "aggregation","summary-window": 3600},{"summary-type": "aggregation","summary-window": 86400}]}]
}
m = requests.post(url, data=json.dumps(payload), headers=headers)

returnJSON = m.json()
metadataKey = returnJSON['metadata-key']

dat = {
    "ts": int(time.time()),
    "val": 1000000000
}
d = requests.post("{0}{1}/throughput/base".format(url,metadataKey), data=json.dumps(dat), headers=headers)