import requests
from bs4 import BeautifulSoup, NavigableString

from team import Team

team_url = "https://www.pro-football-reference.com/teams/{}/{}.htm"
year_url = "https://www.pro-football-reference.com/years/{}/"


def pullTeams(year):
    response = requests.get(year_url.format(year))
    soup = BeautifulSoup(response.text, "html.parser")
    soup.prettify()
    afc_standings = soup.find_all('table', {"id": "AFC"})[0]
    nfc_standings = soup.find_all('table', {"id": "NFC"})[0]
    afcteams = afc_standings.contents[6]
    nfcteams = nfc_standings.contents[6]
    nameIndex = 0
    team_list = []
    for team in afcteams.contents:
        if not (isinstance(team, NavigableString)) and len(team.contents) > 1:
            teamName = getTeamName(team.contents[nameIndex].text.strip())
            team_list.append(teamName)
    for team in nfcteams.contents:
        if not (isinstance(team, NavigableString)) and len(team.contents) > 1:
            teamName = getTeamName(team.contents[nameIndex].text.strip())
            team_list.append(teamName)
    teams = []
    for team_name in team_list:
        teams.append(Team(year, team_name, team_url))
    return teams


def getTeamName(name):
    name = name.replace('New York Jets', 'nyjets') \
        .replace("New York Giants", 'nygiants') \
        .replace("Los Angeles Chargers", 'lachargers') \
        .replace("Los Angeles Rams", 'larams') \
        .replace('.', '') \
        .replace('+', '') \
        .replace('*', '')
    try:
        return name[:name.rindex(' ')].lower().replace(' ', '').replace('.', '')
    except:
        return name
