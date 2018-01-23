# nfl_scraper2.py
# Patrick Ye

# import libraries
import requests
from bs4 import BeautifulSoup

# initialize variables

pos = []
name = []
status = []
team = []

pos_initial_links = ["http://www.nfl.com/players/search?category=position&filter=quarterback&conferenceAbbr=null&playerType=current&conference=ALL",
					"http://www.nfl.com/players/search?category=position&filter=runningback&conferenceAbbr=null&playerType=current&conference=ALL",
					"http://www.nfl.com/players/search?category=position&filter=widereceiver&conferenceAbbr=null&playerType=current&conference=ALL",
					"http://www.nfl.com/players/search?category=position&filter=tightend&conferenceAbbr=null&playerType=current&conference=ALL",
					"http://www.nfl.com/players/search?category=position&filter=offensiveline&conferenceAbbr=null&playerType=current&conference=ALL",
					"http://www.nfl.com/players/search?category=position&filter=defensivelineman&conferenceAbbr=null&playerType=current&conference=ALL",
					"http://www.nfl.com/players/search?category=position&filter=linebacker&conferenceAbbr=null&playerType=current&conference=ALL",
					"http://www.nfl.com/players/search?category=position&filter=defensiveback&conferenceAbbr=null&playerType=current&conference=ALL",
					"http://www.nfl.com/players/search?category=position&filter=kicker&conferenceAbbr=null&playerType=current&conference=ALL",
					"http://www.nfl.com/players/search?category=position&filter=punter&conferenceAbbr=null&playerType=current&conference=ALL"]

pos_abbreviation = ["QB", "RB", "WR", "TE", "OL", "DL", "LB", "DB", "K", "P"]


##### functions #####

def getNumberPosLinks(initial_link):
	
	page = requests.get(initial_link)
	soup = BeautifulSoup(page.content, 'html.parser')
	
	# look above table where it looks like "1 | 2 | next"
	nav_span = soup.find_all('span', class_='linkNavigation')
	
	if len(nav_span) == 0:
		return 1
		
	else:
	
		# pull first hit (there is a navigation at top and bottom of table)
		nav_span_top = nav_span[0]
	
		# count number of links (in example, "2" and "next" will be links)
		num_links = len(nav_span_top.find_all('a'))
	
		num_pages_total = num_links
	
		return num_pages_total
			


def getPlayerData(link):
	
	page = requests.get(link)
	
	soup = BeautifulSoup(page.content, 'html.parser')

	table_list = soup.find_all('table')
	player_table = table_list[3]
	players_list = player_table.find_all('tr')

	Nplayers = len(players_list)-1

	# extract data
	for i in range(1, Nplayers+1):
		player = players_list[i]

		td_list = player.find_all('td')

		pos.append(td_list[0].get_text())
		status.append(td_list[3].get_text())
		team.append(td_list[12].get_text())

		# use "firstName lastName" format		
		nameLastFirst = td_list[2].get_text()
		numNameParts = len(nameLastFirst.rsplit(', '))
		if (numNameParts == 2):
			[lastName, firstName] = nameLastFirst.rsplit(', ')
			name.append(firstName + " " + lastName)
		elif (numNameParts == 3):
			[lastName, firstName, suffix] = nameLastFirst.rsplit(', ')
			name.append(firstName + " " + lastName + " " + suffix)

	return pos, name, status, team



###### script ######

# determine number of links for each position
nfl_links_all = []
for h in range(len(pos_initial_links)):
	
	print "looking up number of " + pos_abbreviation[h] + " pages"
	
	this_initial_link = pos_initial_links[h]
	
	# append initial link to list of all links
	nfl_links_all.append(this_initial_link)
	
	# determine number of links for each position	
	num_pages_total = getNumberPosLinks(this_initial_link)

	# append additional links if more than 1 page
	if (num_pages_total > 1):
		for g in range(2, num_pages_total+1):
			nfl_links_all.append(this_initial_link + "&d-447263-p=" + str(g))

print "Total pages to scrape: " + str(len(nfl_links_all))

# extract data from every NFL player roster link
for j in range(len(nfl_links_all)):
	pos, name, status, team = getPlayerData(nfl_links_all[j])
	print j

# for bad apples who are not currently playing, index.html can find position, defaults team to "not active"


# write to ginormous json file
# make dictionary
import json
data = {}
data["name_pos_team"] = []

for k in range(len(name)):
	
	# exclude players who are cut, on the development team, or not with team
	if (status[k] != 'CUT') & (status[k] != 'DEV') & (status[k] != 'NWT'):

		data["name_pos_team"].append({
			"Name":name[k],
			"Position":pos[k],
			"Team":team[k],
			"Status":status[k],
		})

with open('playerTeams.json', 'w') as f:
     json.dump(data, f)

# add team defenses under "name" variable
team_defenses = ["ARI defense (Cardinals)", "ATL defense (Falcons)", "BAL defense (Ravens)", "BUF defense (Bills)", "CAR defense (Panthers)", 
			  "CHI defense (Bears)", "CIN defense (Bengals)", "CLE defense (Browns)", "DAL defense (Cowboys)", "DEN defense (Broncos)", 
			  "DET defense (Lions)", "GB defense (Packers)", "HOU defense (Texans)", "IND defense (Colts)", "JAX defense (Jaguars)", 
			  "KC defense (Chiefs)", "LAC defense (Chargers)", "LAR defense (Rams)", "MIA defense (Dolphins)", "MIN defense (Vikings)", 
			  "NE defense (Patriots)", "NOR defense (Saints)", "NYG defense (Giants)", "NYJ defense (Jets)", "OAK defense (Raiders)", 
			  "PHI defense (Eagles)", "PIT defense (Steelers)", "SF defense (49ers)", "SEA defense (Seahawks)", "TB defense (Buccaneers)", 
			  "TEN defense (Titans)", "WAS defense (Redskins)"]
			  
name_list = name + team_defenses

with open('names.json', 'w') as f:
     json.dump(name_list, f)