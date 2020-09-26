class Prediction:
    def __init__(self, predictionstring):
        self.predictionstring = predictionstring
        self.confidence, self.pick, self.team1, self.team2, self.spread = self.parsepredictionstring(predictionstring)
        self.fraction_of_bankroll = self.kelly_criterion()

    def parsepredictionstring(self, predictionstring):
        split = predictionstring.replace('\n', '').split(' ')
        spread = round(float(split[1]), 2)
        team1 = split[0]
        team2 = split[2]
        confidence = int(split[-1].replace('(', '').replace(')', '').replace('%', '')) / 100
        pick = split[-2], spread if split[-2] == team1 else spread * -1
        return confidence, pick, team1, team2, spread

    def kelly_criterion(self, odds=1.91):
        b = odds - 1
        p = self.confidence
        q = 1 - self.confidence
        return (b * p - q) / b
