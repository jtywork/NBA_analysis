from nba_api.stats.endpoints import leaguegamefinder

def get_nba_data():
    # Set the season you're interested in
    season = "2022-23"  # Modify this according to the season you want to query

    # Create an instance of the LeagueGameFinder class
    gamefinder = leaguegamefinder.LeagueGameFinder(season_nullable=season)

    # Get the results as a DataFrame
    games = gamefinder.get_data_frames()[0]

    # Display some information about the games
    print(f"Number of games found: {len(games)}")
    print("Sample of game data:")
    print(games.head())

if __name__ == "__main__":
    get_nba_data()
