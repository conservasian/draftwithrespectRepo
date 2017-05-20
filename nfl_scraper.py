# nfl_scraper.py

import requests

from bs4 import BeautifulSoup

pos = []
name = []
status = []
team = []


nfl_links = ["http://www.nfl.com/players/search?category=position&filter=quarterback&conferenceAbbr=null&playerType=current&conference=ALL",
			"http://www.nfl.com/players/search?category=position&playerType=current&d-447263-p=2&conference=ALL&filter=quarterback&conferenceAbbr=null",
			
			"http://www.nfl.com/players/search?category=position&filter=runningback&conferenceAbbr=null&playerType=current&conference=ALL",
			"http://www.nfl.com/players/search?category=position&playerType=current&d-447263-p=2&conference=ALL&filter=runningback&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=3&filter=runningback&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=4&filter=runningback&conferenceAbbr=null",
			
			"http://www.nfl.com/players/search?category=position&filter=widereceiver&conferenceAbbr=null&playerType=current&conference=ALL",
			"http://www.nfl.com/players/search?category=position&playerType=current&d-447263-p=2&conference=ALL&filter=widereceiver&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=3&filter=widereceiver&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=4&filter=widereceiver&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=5&filter=widereceiver&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=6&filter=widereceiver&conferenceAbbr=null",
			
			"http://www.nfl.com/players/search?category=position&filter=tightend&conferenceAbbr=null&playerType=current&conference=ALL",
			"http://www.nfl.com/players/search?category=position&playerType=current&d-447263-p=2&conference=ALL&filter=tightend&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=3&filter=tightend&conferenceAbbr=null",
			
			"http://www.nfl.com/players/search?category=position&filter=offensiveline&conferenceAbbr=null&playerType=current&conference=ALL",
			"http://www.nfl.com/players/search?category=position&playerType=current&d-447263-p=2&conference=ALL&filter=offensiveline&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=3&filter=offensiveline&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=4&filter=offensiveline&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=5&filter=offensiveline&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=6&filter=offensiveline&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=7&filter=offensiveline&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=8&filter=offensiveline&conferenceAbbr=null",
			
			"http://www.nfl.com/players/search?category=position&filter=defensivelineman&conferenceAbbr=null&playerType=current&conference=ALL",
			"http://www.nfl.com/players/search?category=position&playerType=current&d-447263-p=2&conference=ALL&filter=defensivelineman&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=3&filter=defensivelineman&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=4&filter=defensivelineman&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=5&filter=defensivelineman&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=6&filter=defensivelineman&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=7&filter=defensivelineman&conferenceAbbr=null",
			
			"http://www.nfl.com/players/search?category=position&filter=linebacker&conferenceAbbr=null&playerType=current&conference=ALL",
			"http://www.nfl.com/players/search?category=position&playerType=current&d-447263-p=2&conference=ALL&filter=linebacker&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=3&filter=linebacker&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=4&filter=linebacker&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=5&filter=linebacker&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=6&filter=linebacker&conferenceAbbr=null",
			
			"http://www.nfl.com/players/search?category=position&filter=defensiveback&conferenceAbbr=null&playerType=current&conference=ALL",
			"http://www.nfl.com/players/search?category=position&playerType=current&d-447263-p=2&conference=ALL&filter=defensiveback&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=3&filter=defensiveback&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=4&filter=defensiveback&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=5&filter=defensiveback&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=6&filter=defensiveback&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=7&filter=defensiveback&conferenceAbbr=null",
			"http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p=8&filter=defensiveback&conferenceAbbr=null",
			
			"http://www.nfl.com/players/search?category=position&filter=kicker&conferenceAbbr=null&playerType=current&conference=ALL",
			
			"http://www.nfl.com/players/search?category=position&filter=punter&conferenceAbbr=null&playerType=current&conference=ALL"]
			

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


# extract data from every NFL player roster link
for j in range(len(nfl_links)):
	pos, name, status, team = getPlayerData(nfl_links[j])
	print j


# write to ginormous json file
# make dictionary
import json
data = {}
data["name_pos_team"] = []

for k in range(len(name)):
    data["name_pos_team"].append({
    	"Name":name[k],
		"Position":pos[k],
		"Team":team[k],
		"Status":status[k],
    })

with open('playerTeams.json', 'w') as f:
     json.dump(data, f)