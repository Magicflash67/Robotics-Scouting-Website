import ast
Value = [] #it does list things 
# KEY FOR POINT VALUES
AutoSpeakers = 3 # per
MovedInAutos = 1  # single
AutoPenalty = -2 # single
TeleopScoredAMP = 1 # per
ScoredInSpeaker =  2 # per
ScoredTrap = 5 # per max 3
## Parking
Failed = -2 # single
Parked = 1 # single
SoloDoublehang = 3 # single
### parking
### AIS ###
RobotOff = -10 # single
CommsLost = -5 # per
BrownOut = -10 # single
PowerFailure = -15 # single
MechanicalFail = -10 # single
YellowCard = -20 # single
RedCard = -40 # single !WILL BE FLAGGED IN SYSTEM!

def SortListByMaxValue(lst):
    # Extract the maximum value for each dictionary
    def GetMaxValue(dict_item):
        if isinstance(dict_item, dict):
            return max(dict_item.values(), default=0)
        return 0

    # Sort the list based on the maximum value in descending order
    return sorted(lst, key=GetMaxValue, reverse=True)


BigList = []
PointList = []
points = 0
OldValue = None

with open("data.txt", "r") as UnSplitData:
    AllData = UnSplitData.read()
    ListofAllSplitData = AllData.split("#")
    ListofAllSplitData.pop()

for x in range(len(ListofAllSplitData)):
    BigList.insert(0, ast.literal_eval(ast.literal_eval(ListofAllSplitData[x])))

sorted(BigList, key=lambda x: x['TeamNumber'], reverse=True)
OldValue = BigList[0]['TeamNumber']
PointList = [{'T'+BigList[0]['TeamNumber']: None}]
PointLists = 0


for x in range(len(BigList)):
    points = 0
    if BigList[x]['TeamNumber'] == OldValue:
        points = points + (int(BigList[x]['AutosScoredInSpeakers']) * AutoSpeakers) + (int(BigList[x]['TeleopScoredAMP']) * TeleopScoredAMP) + (int(BigList[x]['ScoredInSpeaker']) * ScoredInSpeaker) + (int(BigList[x]['ScoredTrap']) * ScoredTrap) + (int(BigList[x]['CommsLost']) * CommsLost)
        
        if BigList[x]['MovedInAutos'] == 'true':
            points = points + MovedInAutos
        if BigList[x]['AutoPenalty'] == 'true':
            points = points + AutoPenalty
        if BigList[x]['ParkingType'] == 'failed':
            points = points + Failed
        if BigList[x]['ParkingType'] == 'parked':
            points = points + Parked
        if BigList[x]['ParkingType'] in ['hanging', 'harmonized']:
            points = points + SoloDoublehang
        if BigList[x]['RobotOff'] == 'true':
            points = points + RobotOff
        if BigList[x]['BrownOut'] == 'true':
            points = points + BrownOut
        if BigList[x]['PowerFailure'] == 'true':
            points = points + PowerFailure
        if BigList[x]['MechanicalFail'] == 'true':
            points = points + MechanicalFail
        if BigList[x]['YellowCard'] == 'true':
            points = points + YellowCard
        if BigList[x]['RedCard'] == 'true':
            points = points + RedCard
        
        PointList[PointLists]['T' + BigList[x]['TeamNumber']] = points
    else:
        PointLists += 1
        points = points + (int(BigList[x]['AutosScoredInSpeakers']) * AutoSpeakers) + (int(BigList[x]['TeleopScoredAMP']) * TeleopScoredAMP) + (int(BigList[x]['ScoredInSpeaker']) * ScoredInSpeaker) + (int(BigList[x]['ScoredTrap']) * ScoredTrap) + (int(BigList[x]['CommsLost']) * CommsLost)
        
        if BigList[x]['MovedInAutos'] == 'true':
            points = points + MovedInAutos
        if BigList[x]['AutoPenalty'] == 'true':
            points = points + AutoPenalty
        if BigList[x]['ParkingType'] == 'failed':
            points = points + Failed
        if BigList[x]['ParkingType'] == 'parked':
            points = points + Parked
        if BigList[x]['ParkingType'] in ['hanging', 'harmonized']:
            points = points + SoloDoublehang
        if BigList[x]['RobotOff'] == 'true':
            points = points + RobotOff
        if BigList[x]['BrownOut'] == 'true':
            points = points + BrownOut
        if BigList[x]['PowerFailure'] == 'true':
            points = points + PowerFailure
        if BigList[x]['MechanicalFail'] == 'true':
            points = points + MechanicalFail
        if BigList[x]['YellowCard'] == 'true':
            points = points + YellowCard
        if BigList[x]['RedCard'] == 'true':
            points = points + RedCard

        PointList.append({'T' + BigList[x]['TeamNumber']: points})
        OldValue = BigList[x]['TeamNumber']

# Assuming 'my_list' is your list containing the dictionary
for dict_item in PointList:
    if isinstance(dict_item, dict):  # Check if the item is a dictionary
        for key, value in dict_item.items():
            print(f"Key: {key}, Value: {value}")
            Value.append(str({value}))

SortData = SortListByMaxValue(PointList)
print(SortData[0]['T930'])
Table = ""
HTML = open("LeaderBored.html", "w")
Start = """
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="Web.css">
<title>CORE SCOUTING SITE</title>
<link rel="icon" type="image/x-icon" href="/images/CORELogo.jpg">
<meta charset="UTF-8">
</head>
<body>
<div class="outline">
<h1 class="Tiltle">C.O.R.E.2062 SCOUTING WEBSITE </h1> 
<h3 class="UnderClass">Community Of Robotics Enginers</h3> 
<ul>
    <li><a href="./index.html"; class = "active";>HOME </a></li>
    <li><a href="./OurMatches.html">OUR MATCHES</a></li>
    <li><a href="./MatchAna.html">MATCH ANALYSIS NA</a></li>
    <li><a href="./TeamData.html">TEAM ANALYSIS NA</a></li>
    <li><a href="./RawData.html">RAW DATA NA </a></li>
    <li><a href="./LeaderBored.html">Leader Board </a></li>
    <li><a href="./form.html">FORM</a></li>
    <li><a href="./Arch.html">Archived Data NA </a></li>
    <li><a href="./Doc.html">Documentation NA</a></li>` 
</ul>
<br>
<h3 class="UnderClass">C.O.R.E. Leader Board</h3> 
<br>
<div class = table>
    <table style="width:100%" id="cssTable">
        <tr>
            <th>Postion</th>
            <th>Team Number</th>
            <th>Points</th>
          </tr>
          
"""

for x in range(len(SortData)):
    SortData[x].keys()
    Table = Table + """
        <tr>
        <td>"""+str(x+1)+"""</td>
        <td>"""+str(SortData[x].keys())+"""</td>
        <td>"""+Value[x]+"""</td>
        </tr>
        """

End = """
      </table>
</div>
</div>
<footer><br>this Page is powerd by github pages and the use of CORE2062 Scouting Viewer<br><br></footer>
</body>
</html> 
"""
HTML.write(Start+Table+End)
HTML.close()