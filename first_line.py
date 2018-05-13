# first_line.py
# Patrick Ye

import json


# load list of looked-up players, from incidents2json.py
with open('lookedUpNames.json', 'r') as f:
	lookedUpNames = json.load(f)
	
# clean up periods, all lower case
lookedUpNames_clean = []
for a in range(len(lookedUpNames)):
	cleanedName = lookedUpNames[a]
	cleanedName = cleanedName.replace('.', '')
	cleanedName = cleanedName.lower()
	lookedUpNames_clean.append(cleanedName)


## defensive players

# load current first line defensive players, scraped from depth_scraper.py
with open('firstLine_defPlayers.json', 'r') as g:
	firstLine_playerNames = json.load(g)

# clean up periods, all lower case
fL_defNames = []
for b in range(len(firstLine_playerNames)):
	cleanedName = firstLine_playerNames[b]
	cleanedName = cleanedName.replace('.', '')
	cleanedName = cleanedName.lower()
	fL_defNames.append(cleanedName)	

# compare	
for i in range(len(fL_defNames)):
	if fL_defNames[i] not in lookedUpNames_clean:
		print(fL_defNames[i])
		
		
		
## offensive players

# load current first line defensive players, scraped from depth_scraper.py
with open('firstLine_offPlayers.json', 'r') as g:
	firstLine_playerNames = json.load(g)
	
# clean up periods, all lower case
fL_offNames = []
for b in range(len(firstLine_playerNames)):
	cleanedName = firstLine_playerNames[b]
	cleanedName = cleanedName.replace('.', '')
	cleanedName = cleanedName.lower()
	fL_offNames.append(cleanedName)	

# compare
for i in range(len(fL_offNames)):
	if fL_offNames[i] not in lookedUpNames_clean:
		print(fL_offNames[i])