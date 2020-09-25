import requests
from bs4 import BeautifulSoup

predictions = []
week = 3
url = "https://www.espn.com/nfl/schedule/_/week/{}".format(week)


def getGameInfo(url):
    response = requests.get("https://www.espn.com{}".format(url))
    soup = BeautifulSoup(response.text, "html.parser")
    soup.prettify()
    teams_long = soup.findAll('span', {'class': 'long-name'})
    teams_short = soup.findAll('span', {'class': 'short-name'})
    away_team = teams_long[0].text.strip()
    if away_team == 'Los Angeles':
        if teams_short[0].text.strip() == 'Rams':
            away_team = 'larams'
        else:
            away_team = 'lachargers'
    if away_team == 'New York':
        if teams_short[0].text.strip() == 'Giants':
            away_team = 'nygiants'
        else:
            away_team = 'nyjets'

    home_team = teams_long[1].text.strip()
    if home_team == 'Los Angeles':
        if teams_short[1].text.strip() == 'Rams':
            home_team = 'larams'
        else:
            home_team = 'lachargers'
    if home_team == 'New York':
        if teams_short[1].text.strip() == 'Giants':
            home_team = 'nygiants'
        else:
            home_team = 'nyjets'

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