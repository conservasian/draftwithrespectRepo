# make_side_pages.py
# Patrick Ye

F = open("index.html", "r")
G = F.read()

idx_start = G.index('</nav>')

thoughts = """
 
<div id=\'jumbotron6\' class=\'jumbotron text-center\'>
	<h2>Thoughts about using this site</h2>
	<p>It seems simple at first: figure out which NFL players have been accused of violent actions and list them on a website for fantasy league managers to look up. However, we acknowledge that there are details to be considered: the details of the incident, the player's response, and the judicial outcome. So how do you decide if a player is worthy of joining your fantasy team? We leave it up to you, the fan, to decide for yourself. We at #draftwithrespect aim to simply present the available data to the best of our ability. Our goal is to help you make your dream fantasy team, both on the field and off the field.</p>
	<p>That said, we also want to acknowledge that the criminal justice system is not optimal. Survivors of violence often do not find the protections and resources they deserve at every step of attempting to bring their abuser to justice. Only a small fraction of accusations result in trials, and even pursuing the legal action required for conviction can make a survivor's life more difficult instead of bringing closure.</p>
	<p>Our culture creates many obstacles for survivors stepping forward. When the accused perpetrators are beloved sports figures, it takes incredible courage to face the stigma and backlash that comes with going public. For survivors of all violence, no matter the circumstances, know that we are here in a humble attempt to elevate your voices and stories. #draftwithrespect stands with you.</p>
</div> 
"""
      

how_to_help = """

<div id=\"how_to_help\" class=\"jumbotron text-center\">
      <h2>How can I help?</h2>
      <br>
    <h3>Question whether you can support players with a record of violence.</h3>
    Would you feel comfortable earning fantasy points from someone who has abused victims?<br>
    <br>
    <h3>Speak up when violence happens</h3>
    Whether it's a player on your team or someone you know<br>
    <br>
    <h3>Support victims; listen to what they have to say</h3>
    More than half of victims do not report to police for fear of repercussions.
</div>
"""


H = G[0:idx_start+6] + thoughts + G[idx_start+7:]

L = G[0:idx_start+6] + how_to_help + G[idx_start+7:]


J = open("thoughts.html", "w")
J.write(H)

K = open("howtohelp.html", "w")
K.write(L)