# team_defenses.py
# Patrick Ye

import json

## load roster (playerTeams.json)
with open('playerTeams.json', 'r') as f:
	roster = json.load(f)

	
## make parallel lists of names, teams, and status
roster_names = []
roster_teams = []
roster_status = []
roster_position = []

for r in range(len(roster["name_pos_team"])):
	roster_names.append(roster["name_pos_team"][r]["Name"])
	roster_teams.append(roster["name_pos_team"][r]["Team"])
	roster_status.append(roster["name_pos_team"][r]["Status"])
	roster_position.append(roster["name_pos_team"][r]["Position"])



## load incidents (incidents.json)
with open('incidents.json', 'r') as g:
	incidents = json.load(g)
	


## make list of non-cut defensive players in the incidents database
df_names = []
df_teams = []
df_positions = []
df_statuses = []
df_assaultRelated = []
df_details = []
df_links = []

for i in range(len(incidents["incidents"])):
	
	this_player_name = incidents["incidents"][i]["Name"]
	
	# find this player's name in the roster of names
	if (this_player_name in roster_names):
		roster_idx = roster_names.index(this_player_name)
		
		
		# screen by position for only defensive players
		this_player_position = roster_position[roster_idx]
		if (this_player_position == "DT") | (this_player_position == "DE") | (this_player_position == "NT") | ("LB" in this_player_position) | (this_player_position == "DB") | (this_player_position == "CB") | (this_player_position == "SS") | (this_player_position == "FS") | (this_player_position == "SAF"):
		
				
			# screen out cut players
			this_player_status = roster_status[roster_idx]
		
			if (this_player_status != 'CUT'):
		
				df_names.append(this_player_name)

				this_player_team = roster_teams[roster_idx]
				df_teams.append(this_player_team)
				
				df_positions.append(this_player_position)
				
				this_player_status = incidents["incidents"][i]["Status"]
				df_statuses.append(this_player_status)
				
				this_player_assaultRelated = incidents["incidents"][i]["AssaultRelated"]
				df_assaultRelated.append(this_player_assaultRelated)
				
				this_player_details = incidents["incidents"][i]["Details"]
				df_details.append(this_player_details)
				
				this_player_links = incidents["incidents"][i]["Link"]
				df_links.append(this_player_links)


## now sort out list of defensive players with incidents by team

team_abbrev = ['ARI', 'ATL', 'BAL', 'BUF', 'CAR', 'CHI', 'CIN', 'CLE', 'DAL', 'DEN', 'DET', 'GB', 'HOU', 'IND', 'JAX', 'KC', 'LAC', 'LA', 'MIA', 'MIN', 'NE', 'NOR', 'NYG', 'NYJ', 'OAK', 'PHI', 'PIT', 'SF', 'SEA', 'TB', 'TEN', 'WAS']

data = {}
data["team_defenses"] = {}

# for every team
for k in range(len(team_abbrev)):
	this_team_abbrev = team_abbrev[k]

	data["team_defenses"][this_team_abbrev] = []
	
	# go through list of defensive players with incidents
	for m in range(len(df_teams)):
		
		this_df_team = df_teams[m]
		if (this_df_team == this_team_abbrev):
		
			this_df_name = df_names[m]
			this_df_position = df_positions[m]
			this_df_status = df_statuses[m]
			this_df_assaultRelated = df_assaultRelated[m]
			this_df_details = df_details[m]
			this_df_links = df_links[m]
			
		
			data["team_defenses"][this_team_abbrev].append({
				"Name":this_df_name,
				"Position":this_df_position,
				"Team":this_df_team,
				"Status":this_df_status,
				"AssaultRelated":this_df_assaultRelated,
				"Details":this_df_details,
				"Link":this_df_links,
			})
				
with open('team_defenses.json', 'w') as d:
     json.dump(data, d)
		

