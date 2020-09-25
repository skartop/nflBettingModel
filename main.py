import requests
from bs4 import BeautifulSoup

from predictSpreads import findTeam, predictGame
from test import pullSchedule

predictions = []
week = 3
url = "https://www.espn.com/nfl/schedule/_/week/{}".format(week)

games = pullSchedule(url)

for game in games:
    away = findTeam(game[0])
    home = findTeam(game[1])
    spread = game[2]
    print(away.name, home.name, spread)
    predictions.append(predictGame(away, home, spread))

# for game in schedule
#
# team1 = findTeam("neworleans")
# team2 = findTeam("greenbay")
#
# predictions.append(predictGame(team1, team2, -3))
#
#
fileName = 'predictions/spreads/week{}.txt'.format(week)

with open(fileName, 'w') as f:
    f.writelines(predictions)
f.close()
