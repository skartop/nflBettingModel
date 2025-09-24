# NFL Betting Model

## What It Does
This project scrapes current-season NFL statistics, transforms each matchup into feature differentials, and applies a trained neural network to estimate against-the-spread edges. The pipeline fetches weekly schedules from ESPN, lines up each team with season-to-date metrics from Pro Football Reference, runs the saved Keras model in `model/spreadpredictionmodel`, and outputs recommended wagers ranked by confidence and sized with the Kelly criterion.

## Data & Model Artifacts
- `data/games/` and `data/teams/` store historical box-score aggregates used for training.
- `DataPullers/` contains scrapers for games, spreads, weekly schedules, and team info. They rely on `requests` and `beautifulsoup4`.
- `model/` holds the serialized TensorFlow/Keras model. Re-training overwrites this directory.
- `predictions/spreads/` is where `main.py` writes weekly betting slips (one text file per NFL week).

## Quick Start
1. Create a virtual environment (`python -m venv venv`), activate it, and install dependencies: `pip install pandas numpy tensorflow keras scikit-learn requests beautifulsoup4`.
2. Ensure historical CSVs exist under `data/games` and `data/teams` (generate with `DataPullers/pullData.py` if missing).
3. Verify the trained model is present at `model/spreadpredictionmodel`. Use `trainModel.py` to rebuild it from the CSVs when you refresh data.

## Generating Weekly Picks
- Update the `week` variable in `main.py` and run `python main.py`.
- The script downloads the ESPN schedule for the chosen week, aligns team aliases through `findTeam`, and filters bets with model confidence above 74%.
- Output includes matchup, recommended side, confidence, and suggested stake as a fraction of the bankroll defined near the bottom of `main.py`.

## Retraining the Model
- Run `DataPullers/pullData.py` to scrape updated season statistics and spreads. This step hits public web endpoints; respect rate limits and terms of service.
- Execute `python trainModel.py` to build a new spread classifier. The script trains on seasons 2007–2019, uses validation accuracy to decide whether to replace the saved model, and logs the comparison to stdout.

## Project Layout
- `main.py` orchestrates scraping, inference, and bankroll sizing.
- `predictSpreads.py`, `bet.py`, `game.py`, and `team.py` define feature engineering, Kelly sizing, and prediction utilities.
- `spreadpredictionmodel/` contains supplementary notebooks or exports tied to older experiments.

> **Disclaimer:** Predictions are for research only. Use responsibly and understand the risks before staking real capital.
