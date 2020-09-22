import csv
from datetime import datetime

from predictSpreads import findTeam, predictGame

predictions = []
date = "2020-09-11"

team1 = findTeam("raptors")
team2 = findTeam("celtics")

predictions.append(predictGame(team1, team2, 2.5))

team1 = findTeam("clippers")
team2 = findTeam("nuggets")

predictions.append(predictGame(team1, team2, -8))

fileName = 'predictions/spreads/%s.txt' % date

with open(fileName, 'w') as f:
    f.writelines(predictions)
f.close()