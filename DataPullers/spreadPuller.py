import os

import pandas as pd


def updateSpreads(year):
    spreadData = pd.read_csv("../data/spreads/%d.csv" % year)
    gameData = pd.read_csv("../data/games/%d.csv" % year)

    for i in range(int(len(spreadData) / 2)):
        team1_spread = spreadData.iloc[(i * 2)]
        team2_spread = spreadData.iloc[(i * 2 + 1)]
        favorite = team1_spread if float(team1_spread['ML']) < 0 else team2_spread
        dog = team1_spread if float(team1_spread['ML']) > 0 else team2_spread

        if str(favorite['Close']).lower() == 'pk':
            closingTotal = dog['Close']
            closingSpread = 0
        elif str(dog['Close']).lower() == 'pk':
            closingTotal = favorite['Close']
            closingSpread = 0
        elif float(favorite['Close']) < float(dog['Close']):
            closingTotal = dog['Close']
            closingSpread = favorite['Close']
        else:
            closingTotal = favorite['Close']
            closingSpread = dog['Close']

        date = team1_spread['Date']
        favorite_name = favorite['Team']
        dog_name = dog['Team']
        team1_game = gameData.loc[gameData['date'] == date]
        team1_game = team1_game.loc[team1_game['home_team'].str.contains(favorite_name.lower()) |
                                          team1_game['visitor_team'].str.contains(favorite_name.lower()) |
                                          team1_game['home_team'].str.contains(dog_name.lower()) |
                                          team1_game['visitor_team'].str.contains(dog_name.lower())].index.tolist()

        if len(gameData.loc[team1_game, 'home_team']) > 0:
            if favorite_name.lower() in gameData.loc[team1_game, 'home_team'].iloc[0]:
                closingSpread = 0 - float(closingSpread)

            gameData.loc[team1_game, 'favorite'] = favorite_name
            gameData.loc[team1_game, 'spread'] = closingSpread
            gameData.loc[team1_game, 'total'] = closingTotal
            if closingSpread != 0:
                gameData.loc[team1_game, 'cover'] = 1 if float(
                    gameData.loc[team1_game, 'home_margin_of_victory'].iloc[0]) + float(closingSpread) >= 0 else 0
            else:
                gameData.loc[team1_game, 'cover'] = 1 if float(
                    gameData.loc[team1_game, 'home_margin_of_victory'].iloc[0]) >= 0 else 0
            gameData.loc[team1_game, 'over'] = 1 if float(
                gameData.loc[team1_game, 'home_points'].iloc[0]) + float(
                gameData.loc[team1_game, 'visitor_points'].iloc[0]) >= float(closingTotal) else 0

    gameData.to_csv("../data/games/%d.csv" % year)


def convertXlsxToCsv(year):
    #2010 = nba odds 2009-10.xlsx
    read_file = pd.read_excel('../data/spreads/xlsx/nfl odds 20%s-%s.xlsx' % (str(year - 2000).zfill(2), str(year - 1999).zfill(2)))
    read_file.to_csv('../data/spreads/%d.csv' % year, index=None, header=True)

