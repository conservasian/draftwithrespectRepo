# make_table_page.py
# Patrick Ye

import json

## make list of all active players (all draftable offensive players)
# start with only players I've looked up
# eventually add defensive teams

with open('playerTeams.json', 'r') as f:
	roster = json.load(f)

	
# make parallel lists of names, teams, and status
draftable_names = []
draftable_teams = []
draftable_status = []
draftable_position = []

for r in range(len(roster["name_pos_team"])):

	this_position = roster["name_pos_team"][r]["Position"]
	
	# keep only offensive players
#	if (this_position == 'QB') | (this_position == 'RB') | (this_position == 'WR') | (this_position == 'TE') | (this_position == 'K'):
	if (this_position == 'QB'):
	
		draftable_names.append(roster["name_pos_team"][r]["Name"])
		draftable_teams.append(roster["name_pos_team"][r]["Team"])
		draftable_status.append(roster["name_pos_team"][r]["Status"])
		draftable_position.append(roster["name_pos_team"][r]["Position"])

# default assign each player to gray (-1, no information)
draftable_color = [-1]*len(draftable_names)


## for each quarterback in the incidents database, update green or red

# load incidents (incidents.json)
with open('incidents.json', 'r') as g:
	incidents = json.load(g)


for i in range(len(incidents["incidents"])):
	
	this_player_name = incidents["incidents"][i]["Name"]
	
	if (this_player_name in draftable_names):

		index_draftable = draftable_names.index(this_player_name)
	
		this_player_status = incidents["incidents"][i]["Status"]
		
		if (this_player_status == 'No records found'):
			draftable_color[index_draftable] = 0
			
		else:
			draftable_color[index_draftable] = 1

		
print draftable_names[0:39]
print draftable_color[0:39]
