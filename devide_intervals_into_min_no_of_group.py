"""
    You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].
    You have to divide the intervals into one or more groups such that each interval is in exactly one group, 
    and no two intervals that are in the same group intersect each other.
    Return the minimum number of groups you need to make.
    Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.
"""
def minGroups(intervals):
    events = []
    
    # Add start and end events for each interval
    for left, right in intervals:
        events.append((left, 1))   # Start of an interval
        events.append((right + 1, -1))  # End of an interval (right+1 because it is inclusive)
    
    # Sort events, first by time, then by type (-1 before +1 if they are the same)
    events.sort()
    
    max_groups = 0
    current_groups = 0
    
    # Sweep through the events
    for event in events:
        current_groups += event[1]
        max_groups = max(max_groups, current_groups)
    
    return max_groups

intervals = [[1, 3], [2, 4], [3, 5], [7, 9]]
print(minGroups(intervals))