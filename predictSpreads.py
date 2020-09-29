import os
import keras
import pandas as pd
from game import Game
from DataPullers.teamPuller import pullTeams
from bet import Bet


def strip_first_col(fname, delimiter=None):
    with open(fname, 'r') as fin:
        for line in fin:
            try:
                yield line.split(delimiter, 2)[2]
            except IndexError:
                continue


def predictGame(team1, team2, spread):
    game = Game(team1, team2, spread=spread)
    os.remove('predictionGame.csv')
    header = "date,home_team,visitor_team,home_points,visitor_points,home_margin_of_victory,favorite,spread,total," \
             "cover,over,team_points,team_total_yards,team_plays_offense,team_yds_per_play_offense,team_turnovers," \
             "team_fumbles_lost,team_first_down,team_pass_cmp,team_pass_att,team_pass_yds,team_pass_td,team_pass_int," \
             "team_pass_net_yds_per_att,team_pass_fd,team_rush_att,team_rush_yds,team_rush_td,team_rush_yds_per_att," \
             "team_rush_fd,team_penalties,team_penalties_yds,team_pen_fd,team_drives,team_score_pct," \
             "team_turnover_pct,team_start_avg,team_time_avg,team_plays_per_drive,team_yds_per_drive,team_points_avg," \
             "opp_points,opp_total_yards,opp_plays_offense,opp_yds_per_play_offense,opp_turnovers,opp_fumbles_lost," \
             "opp_first_down,opp_pass_cmp,opp_pass_att,opp_pass_yds,opp_pass_td,opp_pass_int," \
             "opp_pass_net_yds_per_att,opp_pass_fd,opp_rush_att,opp_rush_yds,opp_rush_td,opp_rush_yds_per_att," \
             "opp_rush_fd,opp_penalties,opp_penalties_yds,opp_pen_fd,opp_drives,opp_score_pct,opp_turnover_pct," \
             "opp_start_avg,opp_time_avg,opp_plays_per_drive,opp_yds_per_drive,opp_points_avg" + '\n'
    with open('predictionGame.csv', 'a') as fd:
        fd.write(header)
        fd.write(game.getCSVString())
        fd.write(game.getCSVString())
    dataset = pd.read_csv('predictionGame.csv', delimiter=',')
    dataset = dataset.drop(['home_team',
                            'visitor_team',
                            'home_points',
                            'visitor_points',
                            'favorite',
                            'total',
                            'cover',
                            'home_margin_of_victory',
                            'over',
                            'date'], axis=1)
    dataset = dataset.to_numpy()
    predictions = model.predict_proba(dataset)
    return Bet(('%s %s %s \nPick: %s (%d' % (team1.name,
                                             spread,
                                             team2.name,
                                             team1.name if predictions[0][0] * 100 > 50 else team2.name,
                                                    predictions[0][0] * 100 if predictions[0][0] * 100 > 50 else 100 -
                                                                                                                 predictions[
                                                                                                                     0][
                                                                                                                     0] * 100) +
                       "%)\n\n"))


def findTeam(team_name):
    if team_name[-1] == '*':
        team_name = team_name[:-1]
    for team in league:
        if team_name.lower().replace(" ", "") in team.name.lower().replace(" ", ""):
            return team


model = keras.models.load_model('model/spreadpredictionmodel')
league = pullTeams(2020)
