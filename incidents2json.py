# incidents2json.py
# Patrick Ye

import csv

playerName = []
position = []
assaultRelated = []
status = []
details = []
link = []

playerNamePos_hit = []

with open('#dwr - Incidents.csv', 'rb') as csvfile:
	filereader = csv.reader(csvfile)
	for row in filereader:
		playerName.append(row[0])
		position.append(row[2])
		assaultRelated.append(row[4])
		status.append(row[6])
		details.append(row[5])
		link.append(row[11])

		if row[4] == '1':
			playerNamePos_hit.append(row[0] + ' (' + row[2] + ')')



import json

## save list of all looked-up player names
with open('lookedUpNames.json', 'w') as t:
     json.dump(playerName, t)

## save list of player names with incidents
with open('incidentNamePos.json', 'w') as t:
     json.dump(playerNamePos_hit, t)


## save everything into json file
data = {}
data["incidents"] = []

for k in range(1, len(playerName)):
    data["incidents"].append({
    	"Name":playerName[k],
    	"Position":position[k],
    	"NamePos":playerName[k] + ' (' + position[k] + ')',
    	"AssaultRelated":assaultRelated[k],
		"Status":status[k],
		"Details":details[k],
		"Link":link[k],
    })

with open('incidents.json', 'w') as f:
     json.dump(data, f)
     
#print json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))