# make_table_page.py
# Patrick Ye

import json
import math

## make list of all active players (all draftable offensive players)
# start with only players I've looked up
# eventually add defensive teams



#### Initialization ####
#
# load data
# specify which positions
# start the html file


# load data (incidents.json)
with open('incidents.json', 'r') as g:
	incidents = json.load(g)


# specify positions
positions = ['QB', 'RB']


# open index.html
F = open("index.html", "r")
G = F.read()
idx_start = G.index('</nav>')


# initialize table html
table_html = ""





#### for every position ####


for p in range(len(positions)):


	# initialize 
	all_XX_names = []
	all_XX_color = []
	all_XX_lastNames = []

	# for each quarterback in the incidents database, update green or red
	# NOTE: does not account for multiple conflicting incidents
	for i in range(len(incidents["incidents"])):
	
		this_player_position = incidents["incidents"][i]["Position"]
	
		if (this_player_position == positions[p]):
	
			this_player_name = incidents["incidents"][i]["Name"]	
		
			if (this_player_name in all_XX_names):
				idx_name = all_XX_names.index(this_player_name)

				this_inc_status = incidents["incidents"][i]["AssaultRelated"]
				current_status = all_XX_color[idx_name]
	
				if (this_inc_status):
					all_XX_color[idx_name] == 1
					# no change if 'no records found'
			
		
			else:
				all_XX_names.append(this_player_name)
		
				all_XX_lastNames.append(this_player_name.split(' ')[1])

				this_player_status = int(incidents["incidents"][i]["AssaultRelated"])

				all_XX_color.append(this_player_status)


	all_XX_lastNames_sorted, all_XX_names_sorted = zip(*sorted(zip(all_XX_lastNames, all_XX_names)))
	all_XX_lastNames_sorted, all_XX_color_sorted = zip(*sorted(zip(all_XX_lastNames, all_XX_color)))



	#### now add table to page ####

	## table header
	
	table_html += """
 
	<div id=\'table_div\' class=\'jumbotron text-center\'>"""
	
	
	table_html += """
		<h2>Active """
		
	table_html += positions[p]
	table_html += "s</h2>"
		
		
	table_html += """
		<table class=\'table\'>
		<tbody>
	"""


	## table content
	
	numCols = 3
	len_all_XX = len(all_XX_lastNames_sorted)
	Nrows = int(math.ceil(float(len_all_XX)/float(numCols)))

	# for every row (html writes tables every row)
	for k in range(Nrows):
		
		# first write html for column one	
		name_noSpace1 = all_XX_names_sorted[k].replace(' ', '+')
	
		if (all_XX_color_sorted[k]):
			table_html += """
			<tr>
				<td><a class='incident' href=/?query="""
	
		else:
			table_html += """
			<tr>
				<td><a href=/?query="""
	
		table_html += name_noSpace1
		table_html += ">"
	
		table_html += all_XX_names_sorted[k]
		table_html += """</a></td>
				"""	
		
		# then write html for subsequent columns
		# in case uneven division, leave last column extra cells blank 
		mod = len_all_XX % numCols
	
		for col in range(1, numCols):
	
			if (k+col*Nrows >= len_all_XX):
				table_html += '<td>'	
				table_html += """</td>
				"""
			else:			
				name_noSpaceX = all_XX_names_sorted[k+col*Nrows].replace(' ', '+')
				if (all_XX_color_sorted[k+col*Nrows]):
					table_html += """<td><a class='incident' href=/?query="""
				else:
					table_html += '<td><a href=/?query='
				table_html += name_noSpaceX
				table_html += ">"	
				table_html += all_XX_names_sorted[k+col*Nrows]
				table_html += """</a></td>
				"""

			if (col == numCols - 1):
				table_html += "</tr>"
	

	table_html += """
		</tbody>
		</table>
	</div> 
	"""


## add table to index.html template
H = G[0:idx_start+6] + table_html + G[idx_start+7:]

J = open("table.html", "w")
J.write(H)