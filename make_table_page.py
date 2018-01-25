# make_table_page.py
# Patrick Ye

import json
import math

## make list of all active players (all draftable offensive players)
# start with only players I've looked up
# eventually add defensive teams


# load incidents (incidents.json)
with open('incidents.json', 'r') as g:
	incidents = json.load(g)


all_QB_names = []
all_QB_color = []
all_QB_lastNames = []

# for each quarterback in the incidents database, update green or red
# NOTE: does not account for multiple conflicting incidents
for i in range(len(incidents["incidents"])):
	
	this_player_position = incidents["incidents"][i]["Position"]
	
	if (this_player_position == 'QB'):
	
		this_player_name = incidents["incidents"][i]["Name"]	
		
		if (this_player_name in all_QB_names):
			idx_name = all_QB_names.index(this_player_name)

			this_inc_status = incidents["incidents"][i]["AssaultRelated"]
			current_status = all_QB_color[idx_name]
	
			if (this_inc_status):
				all_QB_color[idx_name] == 1
				# no change if 'no records found'
			
		
		else:
			all_QB_names.append(this_player_name)
		
			all_QB_lastNames.append(this_player_name.split(' ')[1])

			this_player_status = int(incidents["incidents"][i]["AssaultRelated"])

			all_QB_color.append(this_player_status)


all_QB_lastNames_sorted, all_QB_names_sorted = zip(*sorted(zip(all_QB_lastNames, all_QB_names)))
all_QB_lastNames_sorted, all_QB_color_sorted = zip(*sorted(zip(all_QB_lastNames, all_QB_color)))



## now add table to page

# open index.html
F = open("index.html", "r")
G = F.read()
idx_start = G.index('</nav>')


# create table
table_html = """
 
<div id=\'table_div\' class=\'jumbotron text-center\'>
	<h2>Active QBs</h2>
	<table class=\'table\'>
	<tbody>
"""

len_all_QB = len(all_QB_lastNames_sorted)
half = int(math.ceil(len_all_QB / 2))

for k in range(half):
	
	name_noSpace1 = all_QB_names_sorted[k].replace(' ', '+')
	
	table_html += """
	<tr>
		<td><a href=draftwithrespect.com/"""
	
	table_html += name_noSpace1
	table_html += ">"
	
	table_html += all_QB_names_sorted[k]
	table_html += """</a></td>
	"""	
	
	name_noSpace2 = all_QB_names_sorted[k+half].replace(' ', '+')
		
	# in case odd number
	if (k == half-1) & (len_all_QB % 2 == 1):
		table_html += '	<td>'	
		table_html += '</td>'
	else:			
		table_html += '	<td><a href=draftwithrespect.com/'
		table_html += name_noSpace2
		table_html += ">"	
		table_html += all_QB_names_sorted[k+half]
		table_html += '</a></td>'

	table_html += """
	</tr>"""
	
	
	
table_html += """
	</tbody>
	</table>
</div> 
"""


## add table to index.html template
H = G[0:idx_start+6] + table_html + G[idx_start+7:]

J = open("table.html", "w")
J.write(H)