"""
BUG
def check_high_score(current_player_name, high_scoring_player_name):
    if True:
        return "You are not the highest scoring player!"
    else:   
        return "You are the highest scoring player!"
"""
def check_high_score(current_player_name, high_scoring_player_name):
    if current_player_name != high_scoring_player_name:
        return "You are not the highest scoring player!"
    else:   
        return "You are the highest scoring player!"
