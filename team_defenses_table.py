# team_defenses_table.py
# Patrick Ye

import json

## initialize html
# open index.html
F = open("index.html", "r")
G = F.read()
idx_start = G.index('</nav>')


# initialize table html
table_html = ""


# open team_defenses.json to pull statistics
with open('team_defenses.json', 'r') as f:
	team_defenses = json.load(f)


# for every team, calculate
# - number of unique players with incidents
# - total number of unique players researched

team_abbrev = ['ARI', 'ATL', 'BAL', 'BUF', 'CAR', 'CHI', 'CIN', 'CLE', 'DAL', 'DEN', 'DET', 'GB', 'HOU', 'IND', 'JAX', 'KC', 'LAC', 'LA', 'MIA', 'MIN', 'NE', 'NOR', 'NYG', 'NYJ', 'OAK', 'PHI', 'PIT', 'SF', 'SEA', 'TB', 'TEN', 'WAS']
numUniquePlayersWithIncidents = []
numUniquePlayersTotal = []

for r in range(len(team_defenses["team_defenses"])):

	this_team = team_abbrev[r]
	
	this_team_namePos = []
	this_team_assaultRel = []
	this_team_nPaR = []
	
	for s in range(len(team_defenses["team_defenses"][this_team])):
	
		this_team_namePos.append(team_defenses["team_defenses"][this_team][s]["NamePos"])
		this_team_assaultRel.append(int(team_defenses["team_defenses"][this_team][s]["AssaultRelated"]))
		this_team_nPaR.append(team_defenses["team_defenses"][this_team][s]["NamePos"] + team_defenses["team_defenses"][this_team][s]["AssaultRelated"])
	
	
	numUniquePlayersTotal.append(len(set(this_team_namePos)))
	numIncidents = sum(this_team_assaultRel)
	
	numTotalReports = len(team_defenses["team_defenses"][this_team])
	numUniquePlayersIncidents = len(set(this_team_nPaR))
	numDuplicateIncidents = numTotalReports - numUniquePlayersIncidents
	
	numUniquePlayersWithIncidents.append(numIncidents - numDuplicateIncidents)
	

team_defenses = ["ARI defense (Cardinals)", "ATL defense (Falcons)", "BAL defense (Ravens)", "BUF defense (Bills)", "CAR defense (Panthers)", 
			  "CHI defense (Bears)", "CIN defense (Bengals)", "CLE defense (Browns)", "DAL defense (Cowboys)", "DEN defense (Broncos)", 
			  "DET defense (Lions)", "GB defense (Packers)", "HOU defense (Texans)", "IND defense (Colts)", "JAX defense (Jaguars)", 
			  "KC defense (Chiefs)", "LAC defense (Chargers)", "LAR defense (Rams)", "MIA defense (Dolphins)", "MIN defense (Vikings)", 
			  "NE defense (Patriots)", "NOR defense (Saints)", "NYG defense (Giants)", "NYJ defense (Jets)", "OAK defense (Raiders)", 
			  "PHI defense (Eagles)", "PIT defense (Steelers)", "SF defense (49ers)", "SEA defense (Seahawks)", "TB defense (Buccaneers)", 
			  "TEN defense (Titans)", "WAS defense (Redskins)"]
			  
			  
## make table

table_html += """
	<div id=\'table_div\' class=\'jumbotron text-center\'>
	<table class=\'table\'>
	<tbody>
	<tr>
		<td>Team defense</td>
		<td># of players with incidents</td>
		<td># of players looked up</td>
	</tr>
"""

for i in range(32):

	this_team_defense = team_defenses[i]
	this_team_defense_noSpace = this_team_defense.replace(" ", "+") 

	table_html += """
	<tr>
		<td><a href=/?query="""
				
	table_html += this_team_defense_noSpace
	table_html += ">"
	table_html += this_team_defense
	table_html += """</a></td>
		<td>"""
	table_html += str(numUniquePlayersWithIncidents[i])
	table_html += """</td>
		<td>"""
	table_html += str(numUniquePlayersTotal[i])
	table_html += """</td>
	</tr>"""

table_html += """
	</tbody>
	</table>
</div> 
"""


## add table to index.html template
H = G[0:idx_start+6] + table_html + G[idx_start+7:]

J = open("defenses.html", "w")
J.write(H)