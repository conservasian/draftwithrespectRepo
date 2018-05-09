# first_line.py
# Patrick Ye

import json

# load looked-up defensive players, from team_defenses.py (in incidents and on roster)
with open('defensive_playerNames.json', 'r') as f:
	def_playerNames = json.load(f)

# load current first line defensive players, scraped from depth_scraper.py
with open('firstLine_defPlayers.json', 'r') as g:
	firstLine_playerNames = json.load(g)

# clean up periods, all lower case
inc_playerNames = []
for a in range(len(def_playerNames)):
	cleanedName = def_playerNames[a]
	cleanedName = cleanedName.replace('.', '')
	cleanedName = cleanedName.lower()
	inc_playerNames.append(cleanedName)
	
fL_playerNames = []
for b in range(len(firstLine_playerNames)):
	cleanedName = firstLine_playerNames[b]
	cleanedName = cleanedName.replace('.', '')
	cleanedName = cleanedName.lower()
	fL_playerNames.append(cleanedName)	


# compare	
for i in range(len(fL_playerNames)):
	if fL_playerNames[i] not in inc_playerNames:
		print(fL_playerNames[i])
		
		
