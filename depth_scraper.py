# depth_scraper.py
# Patrick Ye

# import libraries
import requests
from bs4 import BeautifulSoup

import json


link = 'http://www.ourlads.com/nfldepthcharts/depthcharts.aspx'
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')

table_list = soup.find_all('table')
table0 = table_list[0]
rows = table0.find_all('tr')

starters = []
starters_def = []

for i in range(len(rows)):
	this_row = rows[i]
	cols = this_row.find_all('td')
	if len(cols) == 12:
		player0_col = cols[3]
		playerEntry = player0_col.get_text()
		if playerEntry != '\n\n':
			playerSplit = playerEntry.split(' ')
			namesOnly = playerSplit[:-1]
			namesOnly = ' '.join(namesOnly)
			nameSplit = namesOnly.split(',')
			lastName = nameSplit[0]
			lastName = lastName[1:]
			firstName = nameSplit[1]
			firstName = firstName[1:]
			playerName = firstName + ' ' + lastName
			playerName = playerName.replace('\n', '')
		
			starters.append(playerName)
	
	if len(cols) > 0:
		text = cols[0].get_text()
		text_split = text.split(' ')
		if text_split[0] == 'Defense':
			for j in range(12):
				this_row = rows[i+j+1]
				cols = this_row.find_all('td')
				if len(cols) == 12:
					player0_col = cols[3]
					playerEntry = player0_col.get_text()
					if playerEntry != '\n\n':
						playerSplit = playerEntry.split(' ')
						namesOnly = playerSplit[:-1]
						namesOnly = ' '.join(namesOnly)
						nameSplit = namesOnly.split(',')
						lastName = nameSplit[0]
						lastName = lastName[0:]
						firstName = nameSplit[1]
						firstName = firstName[1:]
						playerName = firstName + ' ' + lastName
						playerName = playerName.replace('\n', '')
		
						starters_def.append(playerName)
	
with open('firstLine_defPlayers.json', 'w') as e:
     json.dump(starters_def, e)
     
