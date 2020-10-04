import requests
import json
import time

url = 'https://perfsonar.nautilus.optiputer.net/esmond/perfsonar/archive/'
key = '589002f2b2931316ce79b7d9ac61ea363cfb6d75'
headers = {'Content-Type': 'application/json', 'Authorization': 'Token 589002f2b2931316ce79b7d9ac61ea363cfb6d75'}

payload = {
    "subject-type": "point-to-point",
    "source": "198.17.101.70",
    "destination": "67.58.53.201",
    "tool-name": "pscheduler/iperf3",
    "measurement-agent": "198.17.101.70",
    "input-source": "k8s-epyc-01.sdsc.optiputer.net",
    "input-destination": "k8s-gen4-01.calit2.optiputer.net",
    "event-types": [{"event-type": "histogram-owdelay","summaries":[{"summary-type": "aggregation","summary-window": 3600},{"summary-type": "aggregation","summary-window": 86400}]}]
}

m = requests.post(url, data=json.dumps(payload), headers=headers)

returnJSON = m.json()
metadataKey = returnJSON['metadata-key']

print(metadataKey)

dat = {
    "ts": int(time.time()),
    "val": {
        "100": 10,
        "150": 15
    }
}
d = requests.post("{0}{1}/histogram-owdelay/base".format(url,metadataKey), data=json.dumps(dat), headers=headers)