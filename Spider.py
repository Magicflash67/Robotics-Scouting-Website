import ast
def myFunc(e):
  return e['MatchNumber']
def TeamSort(e):
  return e['TeamNumber']

BigList = []
MiddleList = []
MatchdataList = []
TeamCode = { #these are examples 
    '930': [],
    '2062': [],
    '1741': [],
    '1892': [],
    '1': []
}
HTMLData = "" 
HTMLRed = ""
HTMLBlue = ""
CurrenMatchNumber = 1
OldNum = 1

with open("falseData.txt", "r") as UnSplitData: # replace with real data/txt files name
    AllData = UnSplitData.read()
ListofAllSplitData = AllData.split("~")
ListofAllSplitData.pop()
#enter the amount of ditnarys needed to be made
for x in range(len(ListofAllSplitData)):
	BigList.insert(0,ast.literal_eval((ListofAllSplitData[x])))
my_file = open("RawData.html", "w")
Start = """
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="Styles.css">
<title>CORE SCOUTING SITE</title>
<link rel="icon" type="image/x-icon" href="/images/CORELogo.jpg">
<meta charset="UTF-8">
</head>
<body>
<div class="outline">
<h1 class="Tiltle">C.O.R.E.2062 SCOUTING WEBSITE </h1> 
<h3 class="UnderClass">Community Of Robotics Enginers</h3> 
<ul>
    <li><a href="./index.html">HOME </a></li>
    <li><a href="./OurMatches.html">OUR MATCHES</a></li>
    <li><a href="./MatchAna.html">MATCH ANALYSIS</a></li>
    <li><a href="./TeamData.html">TEAM ANALYSIS</a></li>
    <li><a href="./RawData.html"; class = "active";>RAW DATA</a></li>
    <li><a href="./Arch.html">Archived Data </a></li>
    <li><a href="./Doc.html">Documentation</a></li>` 
</ul>
<br>
<h2 class="Sub">RAW DATA</h2> 
<div class = table>
    <table style="width:100%" id="cssTable ">
          <br>
            <table>
			<tr>
		    <th>Color</th>
		    <th>Pos</th>
		    <th>Match</th>
			<th>Team</th>
			<th>Scout name</th>
		    <th>AUTO</th>
		    <th>speaker</th>
            <th>Moved</th>
            <th>penataly</th>
            <th>TELOP</th>
            <th>AMP</th>
            <th>Speaker</th>
            <th>Amplified</th>
            <th>Co-Op point</th>
			<th>END GAME</th>
            <th>Trap</th>
            <th>high note</th>
            <th>Parking</th>
            <th>Comments</th>
		  </tr>
"""
for x in range(len(ListofAllSplitData)): # (BigListist[0]["COLOR"])
		Middle = """<tr>
		    <td> """+str(BigList[x]["COLOR"])+"""</th>     
		    <td>"""+str(BigList[x]["POS"])+"""</th>
		    <td>"""+str(BigList[x]["MatchNumber"])+"""</th>
			<td>"""+str(BigList[x]["TeamNumber"])+"""</th> 
			<td> <button class="textButton" name="""+str(BigList[x]["ScouterName"])+""">""" +str(BigList[x]["ScouterName"])+"""</button></th> 
		    <td>AUTO</th>
		    <td>"""+str(BigList[x]["AutosScoredInSpeakers"])+"""</th>
            <td>"""+str(BigList[x]['MovedInAutos'])+"""</th>
            <td>"""+str(BigList[x]['AutoPenalty'])+"""</th>
            <td>TELOP</th>
            <td>"""+str(BigList[x]["TeleopScoredAMP"])+"""</th>
            <td>"""+str(BigList[x]["ScoredInSpeaker"])+"""</th>
            <td>"""+str(BigList[x]["TimesAmplifiedTeleop"])+"""</th>
            <td>"""+str(BigList[x]["CoopPoint"])+"""</th>
            <td>END</th>
            <td>"""+str(BigList[x]["ScoredTrap"])+"""</th>
            <td>"""+str(BigList[x]["HighNote"])+"""</th>
            <td> <button class="textButton" name="""+str(BigList[x]["parkingType"])+""">""" +str(BigList[x]["parkingType"])+"""</button></th> 
            <td> <button class="textButton" name="""+str(BigList[x]["Comments"])+""">""" +str(BigList[x]["Comments"])+"""</button></th>
		 </tr>"""
		MiddleList.insert(x, Middle)
End = """      
</table> <!--TABLE ENDS HERE-->      
</div>
</div>
    <script>
        // Function to show the button's name in an alert
        function showButtonName(event) {
            var buttonName = event.target.name;
            alert(buttonName);
        }

        // Get all buttons with the class 'textButton'
        var buttons = document.querySelectorAll('.textButton');

        // Add click event listener to each button
        buttons.forEach(function(button) {
            button.addEventListener('click', showButtonName);
        });
    </script>
<footer><br>this Page is powerd by github pages and the use of CORE2062 Scouting Viewerr<br><br></footer>
</body>
</html> 
<!--END -->
"""
html = Start + ''.join(MiddleList) +End
my_file.write(html)
my_file.close()
my_file = open("MatchAna.html", "w")
for x in range(len(ListofAllSplitData)):
	BigList.sort(key=myFunc)
Start = """
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="Styles.css">
<title>CORE SCOUTING SITE</title>
<link rel="icon" type="image/x-icon" href="/images/CORELogo.jpg">
<meta charset="UTF-8">
</head>
<body>
<div class="outline">
<h1 class="Tiltle">C.O.R.E.2062 SCOUTING WEBSITE </h1> 
<h3 class="UnderClass">Community Of Robotics Enginers</h3> 
<ul>
    <li><a href="./index.html">HOME </a></li>
    <li><a href="./OurMatches.html">OUR MATCHES</a></li>
    <li><a href="./MatchAna.html" ; class = "active";>MATCH ANALYSIS</a></li>
    <li><a href="./TeamData.html">TEAM ANALYSIS</a></li>
    <li><a href="./RawData.html">RAW DATA</a></li>
    <li><a href="./Arch.html">Archived Data </a></li>
    <li><a href="./Doc.html">Documentation</a></li>` 
</ul>
<br>
<h2 class="Sub">RAW DATA</h2> 
<div class = table>
    <table style="width:100%" id="cssTable ">
		"""
MiddleList = []
SortedDataHold = []
middlepr1 = """<br>
            <table>
			<tr>
		    <th>Color</th>
		    <th>Pos</th>
		    <th>Match</th>
			<th>Team</th>
			<th>Scout name</th>
		    <th>AUTO</th>
		    <th>speaker</th>
            <th>Moved</th>
            <th>penataly</th>
            <th>TELOP</th>
            <th>AMP</th>
            <th>Speaker</th>
            <th>Amplified</th>
            <th>Co-Op point</th>
			<th>END GAME</th>
            <th>Trap</th>
            <th>high note</th>
            <th>Parking</th>
            <th>Comments</th>
		  </tr>"""
for x in range(len(ListofAllSplitData)): # print(BigList[0]["COLOR"])

		middlepr2= """<tr>
		    <td> """+str(BigList[x]["COLOR"])+"""</th>     
		    <td>"""+str(BigList[x]["POS"])+"""</th>
		    <td>"""+str(BigList[x]["MatchNumber"])+"""</th>
			<td>"""+str(BigList[x]["TeamNumber"])+"""</th> 
			<td> <button class="textButton" name="""+str(BigList[x]["ScouterName"])+""">""" +str(BigList[x]["ScouterName"])+"""</button></th> 
		    <td>AUTO</th>
		    <td>"""+str(BigList[x]["AutosScoredInSpeakers"])+"""</th>
            <td>"""+str(BigList[x]['MovedInAutos'])+"""</th>
            <td>"""+str(BigList[x]['AutoPenalty'])+"""</th>
            <td>TELOP</th>
            <td>"""+str(BigList[x]["TeleopScoredAMP"])+"""</th>
            <td>"""+str(BigList[x]["ScoredInSpeaker"])+"""</th>
            <td>"""+str(BigList[x]["TimesAmplifiedTeleop"])+"""</th>
            <td>"""+str(BigList[x]["CoopPoint"])+"""</th>
            <td>END</th>
            <td>"""+str(BigList[x]["ScoredTrap"])+"""</th>
            <td>"""+str(BigList[x]["HighNote"])+"""</th>
            <td> <button class="textButton" name="""+str(BigList[x]["parkingType"])+""">""" +str(BigList[x]["parkingType"])+"""</button></th> 
            <td> <button class="textButton" name="""+str(BigList[x]["Comments"])+""">""" +str(BigList[x]["Comments"])+"""</button></th>
		 </tr>"""
		if BigList[x]["MatchNumber"] == CurrenMatchNumber:
			if BigList[x]["COLOR"] == "Red":
					HTMLRed = HTMLRed + middlepr2
			else:
				if BigList[x]["COLOR"] == "Blue":
					HTMLBlue = HTMLBlue+middlepr2
		else:
			HTMLData = HTMLBlue + HTMLRed
			HTMLBlue = HTMLRed = ""
			if "Red" in str(HTMLData) or "Blue" in str(HTMLData):
				SortedDataHold.insert(x-1, middlepr1 + HTMLData + "</table>")
			else:
				print('MATCH ERROR: ',BigList[x-1]["MatchNumber"])
			HTMLData = middlepr2
			CurrenMatchNumber = BigList[x]["MatchNumber"]

			
End = """ </table> <!--TABLE ENDS HERE-->

      
</div>
</div>
<script>
        // Function to show the button's name in an alert
        function showButtonName(event) {
            var buttonName = event.target.name;
            alert(buttonName);
        }

        // Get all buttons with the class 'textButton'
        var buttons = document.querySelectorAll('.textButton');

        // Add click event listener to each button
        buttons.forEach(function(button) {
            button.addEventListener('click', showButtonName);
        });
    </script>
<footer><br>this Page is powerd by github pages and the use of CORE2062 Scouting Viewerr<br><br></footer>
</body>
</html> 
<!--END -->
"""
html = Start + ''.join(SortedDataHold) +End
my_file.write(html)
my_file.close()

BigList.sort(key=myFunc)
my_file = open("TeamData.html", "w")
for x in range(len(ListofAllSplitData)):
	BigList.sort(key=TeamSort)
BigList.reverse() 
start = ""
Start = """
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="Styles.css">
<title>CORE SCOUTING SITE</title>
<link rel="icon" type="image/x-icon" href="/images/CORELogo.jpg">
<meta charset="UTF-8">
</head>
<body>
<div class="outline">
<h1 class="Tiltle">C.O.R.E.2062 SCOUTING WEBSITE </h1> 
<h3 class="UnderClass">Community Of Robotics Enginers</h3> 
<ul>
    <li><a href="./index.html">HOME </a></li>
    <li><a href="./OurMatches.html">OUR MATCHES</a></li>
    <li><a href="./MatchAna.html">MATCH ANALYSIS</a></li>
    <li><a href="./TeamData.html"; class = "active";>TEAM ANALYSIS</a></li>
    <li><a href="./RawData.html">RAW DATA</a></li>
    <li><a href="./Arch.html">Archived Data </a></li>
    <li><a href="./Doc.html">Documentation</a></li>` 
</ul>
<br>
<h2 class="Sub">RAW DATA</h2> 
<div class = table>
"""
HTMLBlue = HTMLRed = ""
for x in range(len(ListofAllSplitData)): # print(BigList[0]["COLOR"])

		middlepr2= """<tr>
		    <tr>
		    <td> """+str(BigList[x]["COLOR"])+"""</th>     
		    <td>"""+str(BigList[x]["POS"])+"""</th>
		    <td>"""+str(BigList[x]["MatchNumber"])+"""</th>
			<td>"""+str(BigList[x]["TeamNumber"])+"""</th> 
			<td> <button class="textButton" name="""+str(BigList[x]["ScouterName"])+""">""" +str(BigList[x]["ScouterName"])+"""</button></th> 
		    <td>AUTO</th>
		    <td>"""+str(BigList[x]["AutosScoredInSpeakers"])+"""</th>
            <td>"""+str(BigList[x]['MovedInAutos'])+"""</th>
            <td>"""+str(BigList[x]['AutoPenalty'])+"""</th>
            <td>TELOP</th>
            <td>"""+str(BigList[x]["TeleopScoredAMP"])+"""</th>
            <td>"""+str(BigList[x]["ScoredInSpeaker"])+"""</th>
            <td>"""+str(BigList[x]["TimesAmplifiedTeleop"])+"""</th>
            <td>"""+str(BigList[x]["CoopPoint"])+"""</th>
            <td>END</th>
            <td>"""+str(BigList[x]["ScoredTrap"])+"""</th>
            <td>"""+str(BigList[x]["HighNote"])+"""</th>
            <td> <button class="textButton" name="""+str(BigList[x]["parkingType"])+""">""" +str(BigList[x]["parkingType"])+"""</button></th> 
            <td> <button class="textButton" name="""+str(BigList[x]["Comments"])+""">""" +str(BigList[x]["Comments"])+"""</button></th>
		 </tr>"""
		
		match BigList[x]["TeamNumber"]:
			case '930':
				TeamCode["930"].insert(0,middlepr2)
				TEAM930 = ' '.join(str(item) for item in TeamCode["930"])
			case '2062':
				TeamCode["2062"].insert(0,middlepr2)
				TEAM2062 = ' '.join(str(item) for item in TeamCode["2062"])
			case '1741':
				TeamCode["1741"].insert(0,middlepr2)
				TEAM1741 = ' '.join(str(item) for item in TeamCode["1741"])
			case '1892':
				TeamCode["1892"].insert(0,middlepr2)
				TEAM1892 = ' '.join(str(item) for item in TeamCode["1892"])
			case '1':
				TeamCode["1"].insert(0,middlepr2)
				TEAM1 = ' '.join(str(item) for item in TeamCode["1"])
			case _:
				print("UNKOWN TEAM:"+str(BigList[x]["TeamNumber"]))
TEAM930 = ' '.join(str(item) for item in TeamCode["930"])
TEAM2062 = ' '.join(str(item) for item in TeamCode["2062"])
TEAM1741 = ' '.join(str(item) for item in TeamCode["1741"])
TEAM1892 = ' '.join(str(item) for item in TeamCode["1892"])
TEAM1 = ' '.join(str(item) for item in TeamCode["1"])

HTMLData = Start + middlepr1 + TEAM1 + "</table>" + middlepr1 + TEAM930 + "</table>"+ middlepr1 + TEAM1741 +  "</table>" + middlepr1 + TEAM1892 +  "</table>" + middlepr1 + TEAM2062 +  "</table>"
html = HTMLData +End
my_file.write(html)
my_file.close()
teamList =[]