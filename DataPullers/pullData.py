import os

from DataPullers.gamePuller import pullGames
from DataPullers.spreadPuller import updateSpreads
from DataPullers.teamPuller import pullTeams


def saveTeams():
    global league, header, writepath, mode, fd
    # TEAMS
    try:
        os.remove("../data/teams/%d.csv" % year)
    except:
        pass
    league = pullTeams(year)
    header = \
        "name," + \
        "team_points," + \
        "team_total_yards," + \
        "team_plays_offense," + \
        "team_yds_per_play_offense," + \
        "team_turnovers," + \
        "team_fumbles_lost," + \
        "team_first_down," + \
        "team_pass_cmp," + \
        "team_pass_att," + \
        "team_pass_yds," + \
        "team_pass_td," + \
        "team_pass_int," + \
        "team_pass_net_yds_per_att," + \
        "team_pass_fd," + \
        "team_rush_att," + \
        "team_rush_yds," + \
        "team_rush_td," + \
        "team_rush_yds_per_att," + \
        "team_rush_fd," + \
        "team_penalties," + \
        "team_penalties_yds," + \
        "team_pen_fd," + \
        "team_drives," + \
        "team_score_pct," + \
        "team_turnover_pct," + \
        "team_start_avg," + \
        "team_time_avg," + \
        "team_plays_per_drive," + \
        "team_yds_per_drive," + \
        "team_points_avg," + \
        "opp_points," + \
        "opp_total_yards," + \
        "opp_plays_offense," + \
        "opp_yds_per_play_offense," + \
        "opp_turnovers," + \
        "opp_fumbles_lost," + \
        "opp_first_down," + \
        "opp_pass_cmp," + \
        "opp_pass_att," + \
        "opp_pass_yds," + \
        "opp_pass_td," + \
        "opp_pass_int," + \
        "opp_pass_net_yds_per_att," + \
        "opp_pass_fd," + \
        "opp_rush_att," + \
        "opp_rush_yds," + \
        "opp_rush_td," + \
        "opp_rush_yds_per_att," + \
        "opp_rush_fd," + \
        "opp_penalties," + \
        "opp_penalties_yds," + \
        "opp_pen_fd," + \
        "opp_drives," + \
        "opp_score_pct," + \
        "opp_turnover_pct," + \
        "opp_start_avg," + \
        "opp_time_avg," + \
        "opp_plays_per_drive," + \
        "opp_yds_per_drive," + \
        "opp_points_avg" + '\n'
    writepath = "../data/teams/{}.csv".format(year)
    mode = 'a' if os.path.exists(writepath) else 'w'
    with open(writepath, mode) as fd:
        fd.write(header)
    for team in league:
        team.printGameToCSV(year)
    return league


def saveGames(league):
    global writepath, mode, fd
    # GAMES
    try:
        os.remove("../data/games/%d.csv" % year)
    except:
        pass
    games = pullGames(year, league)
    header = "date," + \
             "home_team," + \
             "visitor_team," + \
             "home_points," + \
             "visitor_points," + \
             "home_margin_of_victory," + \
             "favorite," + \
             "spread," + \
             "total," + \
             "cover," + \
             "over," + \
             "team_points," + \
             "team_total_yards," + \
             "team_plays_offense," + \
             "team_yds_per_play_offense," + \
             "team_turnovers," + \
             "team_fumbles_lost," + \
             "team_first_down," + \
             "team_pass_cmp," + \
             "team_pass_att," + \
             "team_pass_yds," + \
             "team_pass_td," + \
             "team_pass_int," + \
             "team_pass_net_yds_per_att," + \
             "team_pass_fd," + \
             "team_rush_att," + \
             "team_rush_yds," + \
             "team_rush_td," + \
             "team_rush_yds_per_att," + \
             "team_rush_fd," + \
             "team_penalties," + \
             "team_penalties_yds," + \
             "team_pen_fd," + \
             "team_drives," + \
             "team_score_pct," + \
             "team_turnover_pct," + \
             "team_start_avg," + \
             "team_time_avg," + \
             "team_plays_per_drive," + \
             "team_yds_per_drive," + \
             "team_points_avg," + \
             "opp_points," + \
             "opp_total_yards," + \
             "opp_plays_offense," + \
             "opp_yds_per_play_offense," + \
             "opp_turnovers," + \
             "opp_fumbles_lost," + \
             "opp_first_down," + \
             "opp_pass_cmp," + \
             "opp_pass_att," + \
             "opp_pass_yds," + \
             "opp_pass_td," + \
             "opp_pass_int," + \
             "opp_pass_net_yds_per_att," + \
             "opp_pass_fd," + \
             "opp_rush_att," + \
             "opp_rush_yds," + \
             "opp_rush_td," + \
             "opp_rush_yds_per_att," + \
             "opp_rush_fd," + \
             "opp_penalties," + \
             "opp_penalties_yds," + \
             "opp_pen_fd," + \
             "opp_drives," + \
             "opp_score_pct," + \
             "opp_turnover_pct," + \
             "opp_start_avg," + \
             "opp_time_avg," + \
             "opp_plays_per_drive," + \
             "opp_yds_per_drive," + \
             "opp_points_avg" + '\n'
    writepath = "../data/games/%d.csv" % year
    mode = 'a' if os.path.exists(writepath) else 'w'
    with open(writepath, mode) as fd:
        fd.write(header)
    for game in games:
        game.printGameToCSV(year)

year = 2020
# for year in range(2007, 2021):
league = saveTeams()
saveGames(league)
# for year in range(2007, 2021):
updateSpreads(year)
