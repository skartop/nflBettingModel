import os

import requests
from bs4 import BeautifulSoup


class Team:
    def __init__(self, year, name, url):
        self.year = year
        self.name = name.lower().replace(' ', '').replace('.', '')
        self.abbreviation = self.getabbreviation()
        self.url = url.format(self.abbreviation, self.year)

        self.team_stats = []
        self.opp_stats = []

        self.pullStats()

        self.team_points = float(self.team_stats[1].text.strip())
        self.team_total_yards = float(self.team_stats[2].text.strip())
        self.team_plays_offense = float(self.team_stats[3].text.strip())
        self.team_yds_per_play_offense = float(self.team_stats[4].text.strip())
        self.team_turnovers = float(self.team_stats[5].text.strip())
        self.team_fumbles_lost = float(self.team_stats[6].text.strip())
        self.team_first_down = float(self.team_stats[7].text.strip())
        self.team_pass_cmp = float(self.team_stats[8].text.strip())
        self.team_pass_att = float(self.team_stats[9].text.strip())
        self.team_pass_yds = float(self.team_stats[10].text.strip())
        self.team_pass_td = float(self.team_stats[11].text.strip())
        self.team_pass_int = float(self.team_stats[12].text.strip())
        self.team_pass_net_yds_per_att = float(self.team_stats[13].text.strip())
        self.team_pass_fd = float(self.team_stats[14].text.strip())
        self.team_rush_att = float(self.team_stats[15].text.strip())
        self.team_rush_yds = float(self.team_stats[16].text.strip())
        self.team_rush_td = float(self.team_stats[17].text.strip())
        self.team_rush_yds_per_att = float(self.team_stats[18].text.strip())
        self.team_rush_fd = float(self.team_stats[19].text.strip())
        self.team_penalties = float(self.team_stats[20].text.strip())
        self.team_penalties_yds = float(self.team_stats[21].text.strip())
        self.team_pen_fd = float(self.team_stats[22].text.strip())
        self.team_drives = float(self.team_stats[23].text.strip())
        self.team_score_pct = float(self.team_stats[24].text.strip())
        self.team_turnover_pct = float(self.team_stats[25].text.strip())
        self.team_start_avg = float(self.team_stats[26].text.strip().replace('Own ', ''))
        self.team_time_avg = float(self.team_stats[27].text.strip().replace(':', ''))
        self.team_plays_per_drive = float(self.team_stats[28].text.strip())
        self.team_yds_per_drive = float(self.team_stats[29].text.strip())
        self.team_points_avg = float(self.team_stats[30].text.strip())

        self.opp_points = float(self.opp_stats[1].text.strip())
        self.opp_total_yards = float(self.opp_stats[2].text.strip())
        self.opp_plays_offense = float(self.opp_stats[3].text.strip())
        self.opp_yds_per_play_offense = float(self.opp_stats[4].text.strip())
        self.opp_turnovers = float(self.opp_stats[5].text.strip())
        self.opp_fumbles_lost = float(self.opp_stats[6].text.strip())
        self.opp_first_down = float(self.opp_stats[7].text.strip())
        self.opp_pass_cmp = float(self.opp_stats[8].text.strip())
        self.opp_pass_att = float(self.opp_stats[9].text.strip())
        self.opp_pass_yds = float(self.opp_stats[10].text.strip())
        self.opp_pass_td = float(self.opp_stats[11].text.strip())
        self.opp_pass_int = float(self.opp_stats[12].text.strip())
        self.opp_pass_net_yds_per_att = float(self.opp_stats[13].text.strip())
        self.opp_pass_fd = float(self.opp_stats[14].text.strip())
        self.opp_rush_att = float(self.opp_stats[15].text.strip())
        self.opp_rush_yds = float(self.opp_stats[16].text.strip())
        self.opp_rush_td = float(self.opp_stats[17].text.strip())
        self.opp_rush_yds_per_att = float(self.opp_stats[18].text.strip())
        self.opp_rush_fd = float(self.opp_stats[19].text.strip())
        self.opp_penalties = float(self.opp_stats[20].text.strip())
        self.opp_penalties_yds = float(self.opp_stats[21].text.strip())
        self.opp_pen_fd = float(self.opp_stats[22].text.strip())
        self.opp_drives = float(self.opp_stats[23].text.strip())
        self.opp_score_pct = float(self.opp_stats[24].text.strip())
        self.opp_turnover_pct = float(self.opp_stats[25].text.strip())
        self.opp_start_avg = float(self.opp_stats[26].text.strip().replace('Own ', ''))
        self.opp_time_avg = float(self.opp_stats[27].text.strip().replace(':', ''))
        self.opp_plays_per_drive = float(self.opp_stats[28].text.strip())
        self.opp_yds_per_drive = float(self.opp_stats[29].text.strip())
        self.opp_points_avg = float(self.opp_stats[30].text.strip())

    def getabbreviation(self):
        switcher = {
            "arizona": "crd",
            "atlanta": "atl",
            "baltimore": "rav",
            "buffalo": "buf",
            "carolina": "car",
            "chicago": "chi",
            "cincinnati": "cin",
            "cleveland": "cle",
            "dallas": "dal",
            "denver": "den",
            "detroit": "det",
            "greenbay": "gnb",
            "houston": "htx",
            "indianapolis": "clt",
            "jacksonville": "jax",
            "kansascity": "kan",
            "lachargers": "sdg",
            "sandiego": "sdg",
            "larams": "ram",
            "stlouis": "ram",
            "miami": "mia",
            "minnesota": "min",
            "newengland": "nwe",
            "neworleans": "nor",
            "nygiants": "nyg",
            "nyjets": "nyj",
            "oakland": "rai",
            "lvraiders": "rai",
            "philadelphia": "phi",
            "pittsburgh": "pit",
            "sanfrancisco": "sfo",
            "seattle": "sea",
            "tampabay": "tam",
            "tennessee": "oti",
            "washington": "was",
        }
        return switcher.get(self.name)

    def pullStats(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        soup.prettify()
        game_table = soup.findAll('table', {"id": "team_stats"})[0]
        self.team_stats = game_table.contents[6].contents[1].contents
        self.opp_stats = game_table.contents[6].contents[3].contents

    def getStat(self, stats_list, stat):
        return float(stats_list[stat].text.strip().replace('Own ', '').replace(':', ''))

    def printGameToCSV(self, year):
        writepath = "../data/teams/%d.csv" % year
        mode = 'a' if os.path.exists(writepath) else 'w'
        with open(writepath, mode) as fd:
            fd.write(self.getCSVString())

    def getCSVString(self):
        return "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18},{19},{20},{21}," \
               "{22},{23},{24},{25},{26},{27},{28},{29},{30},{31},{32},{33},{34},{35},{36},{37},{38},{39},{40},{41}," \
               "{42},{43},{44},{45},{46},{47},{48},{49},{50},{51},{52},{53},{54},{55},{56},{57},{58},{59}," \
               "{60}\n".format(
            self.name,
            "{:.2f}".format(self.team_points),
            "{:.2f}".format(self.team_total_yards),
            "{:.2f}".format(self.team_plays_offense),
            "{:.2f}".format(self.team_yds_per_play_offense),
            "{:.2f}".format(self.team_turnovers),
            "{:.2f}".format(self.team_fumbles_lost),
            "{:.2f}".format(self.team_first_down),
            "{:.2f}".format(self.team_pass_cmp),
            "{:.2f}".format(self.team_pass_att),
            "{:.2f}".format(self.team_pass_yds),
            "{:.2f}".format(self.team_pass_td),
            "{:.2f}".format(self.team_pass_int),
            "{:.2f}".format(self.team_pass_net_yds_per_att),
            "{:.2f}".format(self.team_pass_fd),
            "{:.2f}".format(self.team_rush_att),
            "{:.2f}".format(self.team_rush_yds),
            "{:.2f}".format(self.team_rush_td),
            "{:.2f}".format(self.team_rush_yds_per_att),
            "{:.2f}".format(self.team_rush_fd),
            "{:.2f}".format(self.team_penalties),
            "{:.2f}".format(self.team_penalties_yds),
            "{:.2f}".format(self.team_pen_fd),
            "{:.2f}".format(self.team_drives),
            "{:.2f}".format(self.team_score_pct),
            "{:.2f}".format(self.team_turnover_pct),
            "{:.2f}".format(self.team_start_avg),
            "{:.2f}".format(self.team_time_avg),
            "{:.2f}".format(self.team_plays_per_drive),
            "{:.2f}".format(self.team_yds_per_drive),
            "{:.2f}".format(self.team_points_avg),
            "{:.2f}".format(self.opp_points),
            "{:.2f}".format(self.opp_total_yards),
            "{:.2f}".format(self.opp_plays_offense),
            "{:.2f}".format(self.opp_yds_per_play_offense),
            "{:.2f}".format(self.opp_turnovers),
            "{:.2f}".format(self.opp_fumbles_lost),
            "{:.2f}".format(self.opp_first_down),
            "{:.2f}".format(self.opp_pass_cmp),
            "{:.2f}".format(self.opp_pass_att),
            "{:.2f}".format(self.opp_pass_yds),
            "{:.2f}".format(self.opp_pass_td),
            "{:.2f}".format(self.opp_pass_int),
            "{:.2f}".format(self.opp_pass_net_yds_per_att),
            "{:.2f}".format(self.opp_pass_fd),
            "{:.2f}".format(self.opp_rush_att),
            "{:.2f}".format(self.opp_rush_yds),
            "{:.2f}".format(self.opp_rush_td),
            "{:.2f}".format(self.opp_rush_yds_per_att),
            "{:.2f}".format(self.opp_rush_fd),
            "{:.2f}".format(self.opp_penalties),
            "{:.2f}".format(self.opp_penalties_yds),
            "{:.2f}".format(self.opp_pen_fd),
            "{:.2f}".format(self.opp_drives),
            "{:.2f}".format(self.opp_score_pct),
            "{:.2f}".format(self.opp_turnover_pct),
            "{:.2f}".format(self.opp_start_avg),
            "{:.2f}".format(self.opp_time_avg),
            "{:.2f}".format(self.opp_plays_per_drive),
            "{:.2f}".format(self.opp_yds_per_drive),
            "{:.2f}".format(self.opp_points_avg))
