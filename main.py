from predictSpreads import findTeam, predictGame

predictions = []
date = "2020-09-25"

team1 = findTeam("neworleans")
team2 = findTeam("greenbay")

predictions.append(predictGame(team1, team2, -3))


fileName = 'predictions/spreads/%s.txt' % date

with open(fileName, 'w') as f:
    f.writelines(predictions)
f.close()