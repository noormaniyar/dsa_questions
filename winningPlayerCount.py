"""

You are given an integer n representing the number of players in a game and a 2D array pick where pick[i] = [xi, yi] represents that the player xi picked a ball of color yi.

Player i wins the game if they pick strictly more than i balls of the same color. In other words,

Player 0 wins if they pick any ball.
Player 1 wins if they pick at least two balls of the same color.
...
Player i wins if they pick at least i + 1 balls of the same color.
Return the number of players who win the game.

Note that multiple players can win the game.

"""

from collections import defaultdict

def count_winners(n, pick):
    # Initialize a list of dictionaries to count colors for each player
    player_color_count = [defaultdict(int) for _ in range(n)]
    print(player_color_count, '========================player_color_count======================')
    
    # Populate the color counts for each player
    for player, color in pick:
        print(player, color, '===========================player, color===================')
        player_color_count[player][color] += 1
        print(player_color_count[player][color], '-------------------player_color_count[player][color]---------------')
    
    # Count the number of winners
    winners = 0
    print(winners, '-------------------winners--------------------')
    for i in range(n):
        print(i, '---------------------------i-------------------')
        # Check if player i has picked at least i+1 balls of the same color
        if any(count >= i + 1 for count in player_color_count[i].values()):
            winners += 1
    print(winners, '--------------------------winners-------------------')
    return winners


n = 4
pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]
# pick = [[1,1],[1,2],[1,3],[1,4]]



count_winners(n, pick)