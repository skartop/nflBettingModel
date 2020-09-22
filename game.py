import os


class Game():
    def __init__(self, home_team, visitor_team, home_points, visitor_points, date):
        self.home_team = home_team
        self.visitor_team = visitor_team
        self.home_points = home_points
        self.visitor_points = visitor_points
        self.date = date
        self.home_margin_of_victory = home_points - visitor_points

        self.total = 0
        self.spread = 0
        self.favorite = 0
        self.cover = 0
        self.over = 0

        self.team_points_diff = self.home_team.team_points - self.visitor_team.team_points
        self.team_total_yards_diff = self.home_team.team_total_yards - self.visitor_team.team_total_yards
        self.team_plays_offense_diff = self.home_team.team_plays_offense - self.visitor_team.team_plays_offense
        self.team_yds_per_play_offense_diff = self.home_team.team_yds_per_play_offense - self.visitor_team.team_yds_per_play_offense
        self.team_turnovers_diff = self.home_team.team_turnovers - self.visitor_team.team_turnovers
        self.team_fumbles_lost_diff = self.home_team.team_fumbles_lost - self.visitor_team.team_fumbles_lost
        self.team_first_down_diff = self.home_team.team_first_down - self.visitor_team.team_first_down
        self.team_pass_cmp_diff = self.home_team.team_pass_cmp - self.visitor_team.team_pass_cmp
        self.team_pass_att_diff = self.home_team.team_pass_att - self.visitor_team.team_pass_att
        self.team_pass_yds_diff = self.home_team.team_pass_yds - self.visitor_team.team_pass_yds
        self.team_pass_td_diff = self.home_team.team_pass_td - self.visitor_team.team_pass_td
        self.team_pass_int_diff = self.home_team.team_pass_int - self.visitor_team.team_pass_int
        self.team_pass_net_yds_per_att_diff = self.home_team.team_pass_net_yds_per_att - self.visitor_team.team_pass_net_yds_per_att
        self.team_pass_fd_diff = self.home_team.team_pass_fd - self.visitor_team.team_pass_fd
        self.team_rush_att_diff = self.home_team.team_rush_att - self.visitor_team.team_rush_att
        self.team_rush_yds_diff = self.home_team.team_rush_yds - self.visitor_team.team_rush_yds
        self.team_rush_td_diff = self.home_team.team_rush_td - self.visitor_team.team_rush_td
        self.team_rush_yds_per_att_diff = self.home_team.team_rush_yds_per_att - self.visitor_team.team_rush_yds_per_att
        self.team_rush_fd_diff = self.home_team.team_rush_fd - self.visitor_team.team_rush_fd
        self.team_penalties_diff = self.home_team.team_penalties - self.visitor_team.team_penalties
        self.team_penalties_yds_diff = self.home_team.team_penalties_yds - self.visitor_team.team_penalties_yds
        self.team_pen_fd_diff = self.home_team.team_pen_fd - self.visitor_team.team_pen_fd
        self.team_drives_diff = self.home_team.team_drives - self.visitor_team.team_drives
        self.team_score_pct_diff = self.home_team.team_score_pct - self.visitor_team.team_score_pct
        self.team_turnover_pct_diff = self.home_team.team_turnover_pct - self.visitor_team.team_turnover_pct
        self.team_start_avg_diff = self.home_team.team_start_avg - self.visitor_team.team_start_avg
        self.team_time_avg_diff = self.home_team.team_time_avg - self.visitor_team.team_time_avg
        self.team_plays_per_drive_diff = self.home_team.team_plays_per_drive - self.visitor_team.team_plays_per_drive
        self.team_yds_per_drive_diff = self.home_team.team_yds_per_drive - self.visitor_team.team_yds_per_drive
        self.team_points_avg_diff = self.home_team.team_points_avg - self.visitor_team.team_points_avg
        self.opp_points_diff = self.home_team.opp_points - self.visitor_team.opp_points
        self.opp_total_yards_diff = self.home_team.opp_total_yards - self.visitor_team.opp_total_yards
        self.opp_plays_offense_diff = self.home_team.opp_plays_offense - self.visitor_team.opp_plays_offense
        self.opp_yds_per_play_offense_diff = self.home_team.opp_yds_per_play_offense - self.visitor_team.opp_yds_per_play_offense
        self.opp_turnovers_diff = self.home_team.opp_turnovers - self.visitor_team.opp_turnovers
        self.opp_fumbles_lost_diff = self.home_team.opp_fumbles_lost - self.visitor_team.opp_fumbles_lost
        self.opp_first_down_diff = self.home_team.opp_first_down - self.visitor_team.opp_first_down
        self.opp_pass_cmp_diff = self.home_team.opp_pass_cmp - self.visitor_team.opp_pass_cmp
        self.opp_pass_att_diff = self.home_team.opp_pass_att - self.visitor_team.opp_pass_att
        self.opp_pass_yds_diff = self.home_team.opp_pass_yds - self.visitor_team.opp_pass_yds
        self.opp_pass_td_diff = self.home_team.opp_pass_td - self.visitor_team.opp_pass_td
        self.opp_pass_int_diff = self.home_team.opp_pass_int - self.visitor_team.opp_pass_int
        self.opp_pass_net_yds_per_att_diff = self.home_team.opp_pass_net_yds_per_att - self.visitor_team.opp_pass_net_yds_per_att
        self.opp_pass_fd_diff = self.home_team.opp_pass_fd - self.visitor_team.opp_pass_fd
        self.opp_rush_att_diff = self.home_team.opp_rush_att - self.visitor_team.opp_rush_att
        self.opp_rush_yds_diff = self.home_team.opp_rush_yds - self.visitor_team.opp_rush_yds
        self.opp_rush_td_diff = self.home_team.opp_rush_td - self.visitor_team.opp_rush_td
        self.opp_rush_yds_per_att_diff = self.home_team.opp_rush_yds_per_att - self.visitor_team.opp_rush_yds_per_att
        self.opp_rush_fd_diff = self.home_team.opp_rush_fd - self.visitor_team.opp_rush_fd
        self.opp_penalties_diff = self.home_team.opp_penalties - self.visitor_team.opp_penalties
        self.opp_penalties_yds_diff = self.home_team.opp_penalties_yds - self.visitor_team.opp_penalties_yds
        self.opp_pen_fd_diff = self.home_team.opp_pen_fd - self.visitor_team.opp_pen_fd
        self.opp_drives_diff = self.home_team.opp_drives - self.visitor_team.opp_drives
        self.opp_score_pct_diff = self.home_team.opp_score_pct - self.visitor_team.opp_score_pct
        self.opp_turnover_pct_diff = self.home_team.opp_turnover_pct - self.visitor_team.opp_turnover_pct
        self.opp_start_avg_diff = self.home_team.opp_start_avg - self.visitor_team.opp_start_avg
        self.opp_time_avg_diff = self.home_team.opp_time_avg - self.visitor_team.opp_time_avg
        self.opp_plays_per_drive_diff = self.home_team.opp_plays_per_drive - self.visitor_team.opp_plays_per_drive
        self.opp_yds_per_drive_diff = self.home_team.opp_yds_per_drive - self.visitor_team.opp_yds_per_drive
        self.opp_points_avg_diff = self.home_team.opp_points_avg - self.visitor_team.opp_points_avg

    def printGameToCSV(self, year):
        writepath = "../data/games/%d.csv" % year
        mode = 'a' if os.path.exists(writepath) else 'w'
        with open(writepath, mode) as fd:
            fd.write(self.getCSVString())

    def getCSVString(self):
        return "" \
               "{},{},{},{},{},{},{},{},{},{}," \
               "{},{},{},{},{},{},{},{},{},{}," \
               "{},{},{},{},{},{},{},{},{},{}," \
               "{},{},{},{},{},{},{},{},{},{}," \
               "{},{},{},{},{},{},{},{},{},{}," \
               "{},{},{},{},{},{},{},{},{},{}," \
               "{},{},{},{},{},{},{},{},{},{},{}" \
               "\n".format(
                    str(self.date),
                    str(self.home_team.name),
                    str(self.visitor_team.name),
                    str(self.home_points),
                    str(self.visitor_points),
                    str(self.home_margin_of_victory),
                    str(self.favorite),
                    str(self.spread),
                    str(self.total),
                    str(self.cover),
                    str(self.over),
                    str(self.team_points_diff),
                    str(self.team_total_yards_diff),
                    str(self.team_plays_offense_diff),
                    str(self.team_yds_per_play_offense_diff),
                    str(self.team_turnovers_diff),
                    str(self.team_fumbles_lost_diff),
                    str(self.team_first_down_diff),
                    str(self.team_pass_cmp_diff),
                    str(self.team_pass_att_diff),
                    str(self.team_pass_yds_diff),
                    str(self.team_pass_td_diff),
                    str(self.team_pass_int_diff),
                    str(self.team_pass_net_yds_per_att_diff),
                    str(self.team_pass_fd_diff),
                    str(self.team_rush_att_diff),
                    str(self.team_rush_yds_diff),
                    str(self.team_rush_td_diff),
                    str(self.team_rush_yds_per_att_diff),
                    str(self.team_rush_fd_diff),
                    str(self.team_penalties_diff),
                    str(self.team_penalties_yds_diff),
                    str(self.team_pen_fd_diff),
                    str(self.team_drives_diff),
                    str(self.team_score_pct_diff),
                    str(self.team_turnover_pct_diff),
                    str(self.team_start_avg_diff),
                    str(self.team_time_avg_diff),
                    str(self.team_plays_per_drive_diff),
                    str(self.team_yds_per_drive_diff),
                    str(self.team_points_avg_diff),
                    str(self.opp_points_diff),
                    str(self.opp_total_yards_diff),
                    str(self.opp_plays_offense_diff),
                    str(self.opp_yds_per_play_offense_diff),
                    str(self.opp_turnovers_diff),
                    str(self.opp_fumbles_lost_diff),
                    str(self.opp_first_down_diff),
                    str(self.opp_pass_cmp_diff),
                    str(self.opp_pass_att_diff),
                    str(self.opp_pass_yds_diff),
                    str(self.opp_pass_td_diff),
                    str(self.opp_pass_int_diff),
                    str(self.opp_pass_net_yds_per_att_diff),
                    str(self.opp_pass_fd_diff),
                    str(self.opp_rush_att_diff),
                    str(self.opp_rush_yds_diff),
                    str(self.opp_rush_td_diff),
                    str(self.opp_rush_yds_per_att_diff),
                    str(self.opp_rush_fd_diff),
                    str(self.opp_penalties_diff),
                    str(self.opp_penalties_yds_diff),
                    str(self.opp_pen_fd_diff),
                    str(self.opp_drives_diff),
                    str(self.opp_score_pct_diff),
                    str(self.opp_turnover_pct_diff),
                    str(self.opp_start_avg_diff),
                    str(self.opp_time_avg_diff),
                    str(self.opp_plays_per_drive_diff),
                    str(self.opp_yds_per_drive_diff),
                    str(self.opp_points_avg_diff))
