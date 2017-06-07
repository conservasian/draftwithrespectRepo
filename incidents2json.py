# incidents2json.py
# Patrick Ye

import csv

playerName = []
assaultRelated = []
status = []
details = []
link = []

with open('#dwr - Incidents.csv', 'rb') as csvfile:
	filereader = csv.reader(csvfile)
	for row in filereader:
		playerName.append(row[0])
		assaultRelated.append(row[4])
		status.append(row[6])
		details.append(row[5])
		link.append(row[11])


import json

data = {}
data["incidents"] = []

for k in range(1, len(playerName)):
    data["incidents"].append({
    	"Name":playerName[k],
    	"AssaultRelated":assaultRelated[k],
		"Status":status[k],
		"Details":details[k],
		"Link":link[k],
    })

with open('incidents.json', 'w') as f:
     json.dump(data, f)
     
print json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))