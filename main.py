from predictSpreads import findTeam, predictGame
from DataPullers.pullWeeklySchedule import pullSchedule

bets = []
betstrings = []
week = 6
url = "https://www.espn.com/nfl/schedule/_/week/{}".format(week)


def predictGames(games):
    for game in games:
        away = findTeam(game[0])
        home = findTeam(game[1])
        spread = game[2]
        bet = predictGame(away, home, spread)
        if bet != 'Game OTB':
            bets.append(bet)
            betstrings.append(bet.predictionstring)
    fileName = 'predictions/spreads/week{}.txt'.format(week)
    with open(fileName, 'w') as f:
        f.writelines(betstrings)
    f.close()
    return bets


bets = predictGames(pullSchedule(url))

bankroll = 192.67
top_bets = []
for bet in bets:
    if bet.confidence > 0.74:
        top_bets.append(bet)


for bet in top_bets:
    bet.wager = round(bet.fraction_of_bankroll * bankroll / len(top_bets), 2)

wageredamount = 0
for bet in top_bets:
    wageredamount += bet.wager
    print(bet.team1, bet.spread, bet.team2, "\nPick: "+str(bet.pick), "$"+str(bet.wager)+"\n")

print("Bet: $"+str(round(wageredamount, 2))+" to win: $"+str(round(wageredamount*1.91, 2)))

print("Remaining Bankroll: $"+str(round(bankroll-wageredamount, 2)))

