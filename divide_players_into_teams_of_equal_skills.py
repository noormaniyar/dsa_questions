"""
    You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. 
    Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.
    The chemistry of a team is equal to the product of the skills of the players on that team.
    Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams 
    such that the total skill of each team is equal.
"""
def divide_players(skill):
    skill.sort()
    n = len(skill)
    
    if n % 2 != 0:
        return -1  # If the number of players is odd, return -1
    
    target_sum = skill[0] + skill[-1]
    total_chemistry = 0
    
    for i in range(n // 2):
        # Check if each pair's sum is equal to the target_sum
        if skill[i] + skill[n - 1 - i] != target_sum:
            return -1
        
        # Calculate the chemistry for this pair
        total_chemistry += skill[i] * skill[n - 1 - i]
    
    return total_chemistry


skill = [3,2,5,1,3,4]
print(divide_players(skill))
