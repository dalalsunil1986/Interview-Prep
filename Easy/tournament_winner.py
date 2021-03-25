def tournamentWinner(competitions, results):
    best_team, max_wins = "", 0
    HOME, AWAY = 0, 1
    HOME_WON = 1
    team_wins = {}
    for idx, competition in enumerate(competitions):
        winner = competition[HOME] if results[idx] == HOME_WON else competition[AWAY]
        team_wins[winner] = team_wins.get(winner, 0) + 1
        if team_wins[winner] > max_wins:
            max_wins = team_wins[winner]
            best_team = winner

    return best_team
