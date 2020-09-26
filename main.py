from predictSpreads import findTeam, predictGame
from DataPullers.pullWeeklySchedule import pullSchedule

predictions = []
predictionstrings = []
week = 3
url = "https://www.espn.com/nfl/schedule/_/week/{}".format(week)


def predictGames(games):
    for game in games:
        away = findTeam(game[0])
        home = findTeam(game[1])
        spread = game[2]
        prediction = predictGame(away, home, spread)
        predictions.append(prediction)
        predictionstrings.append(prediction.predictionstring)
    fileName = 'predictions/spreads/week{}.txt'.format(week)
    with open(fileName, 'w') as f:
        f.writelines(predictionstrings)
    f.close()
    return predictions


predictions = predictGames(pullSchedule(url))
bankroll = 100
top_bets = []
for prediction in predictions:
    if prediction.confidence > 0.74:
        top_bets.append(prediction)

for bet in top_bets:
    print(bet.pick, "$" + str(round(bet.fraction_of_bankroll * bankroll / len(top_bets), 2)))
