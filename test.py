import requests
from bs4 import BeautifulSoup

predictions = []
week = 3
url = "https://www.espn.com/nfl/schedule/_/week/{}".format(week)


def getGameInfo(url):
    response = requests.get("https://www.espn.com{}".format(url))
    soup = BeautifulSoup(response.text, "html.parser")
    soup.prettify()
    teams = soup.findAll('span', {'class': 'long-name'})
    away_team = teams[0].text.strip()
    home_team = teams[1].text.strip()
    spread = round(float(soup.findAll('tr', {'class': 'awayteam'})[0].contents[9].text.strip()), 1)
    return away_team, home_team, spread


def pullSchedule(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    soup.prettify()
    game_tables = soup.findAll('table')

    games = []

    for table in game_tables:
        for game_row in table.findAll('td', {'data-behavior': 'date_time'}):
            away, home, spread = getGameInfo(game_row.findAll('a', href=True)[0]['href'])
            games.append([away, home, spread])
    return games

games = pullSchedule(url)
x=3