# check_incident_positions.py
# Patrick Ye
#
# good for checking if players' positions have changed and if players' names have been misspelled in incidents database


import json


#### Initialization ####
#
# load data


# load incident data (incidents.json)
with open('incidents.json', 'r') as g:
	incidents = json.load(g)
	

# load active player roster	
with open('roster.json', 'r') as f:
	roster = json.load(f)

roster_name = []
roster_namePos = []
roster_status = []
for r in range(len(roster["name_pos_team"])):
	roster_name.append(roster["name_pos_team"][r]["Name"])
	roster_namePos.append(roster["name_pos_team"][r]["NamePos"])
	roster_status.append(roster["name_pos_team"][r]["Status"])
	

# check each namePos in incidents and see if there is a match in the roster database	
for i in range(len(incidents["incidents"])):
	this_player_namePos = incidents["incidents"][i]["NamePos"]
	if (this_player_namePos not in roster_namePos):
		print(this_player_namePos)
		
		# check if name is on active roster, maybe position has changed?
		# don't forget some players share same names
		this_player_name = incidents["incidents"][i]["Name"]
		if (this_player_name in roster_name):
			idx_name = roster_name.index(this_player_name)
			print("name active, position changed?")
			print("possibly " + roster_namePos[idx_name])
		
		print("")
