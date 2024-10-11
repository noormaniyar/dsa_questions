"""
    There is a party where n friends numbered from 0 to n - 1 are attending. 
    There is an infinite number of chairs in this party that are numbered from 0 to infinity. 
    When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.
    For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.
    When a friend leaves the party, their chair becomes unoccupied at the moment they leave. 
    If another friend arrives at that same moment, they can sit in that chair.
    You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], indicating the arrival and leaving times 
    of the ith friend respectively, and an integer targetFriend. All arrival times are distinct.
    Return the chair number that the friend numbered targetFriend will sit on.
"""
import heapq

def smallestChair(times, targetFriend):
    # Step 1: Process events
    events = []
    for i, (arrival, leaving) in enumerate(times):
        events.append((arrival, 1, i))  # Arrival is marked by 1
        events.append((leaving, 0, i))  # Departure is marked by 0
    
    # Step 2: Sort events by time, with departure handled first when times are the same
    events.sort(key=lambda x: (x[0], x[1]))
    
    # Min-heap for available chairs
    available_chairs = []
    heapq.heapify(available_chairs)
    
    # Initially the smallest available chair is 0
    next_chair = 0
    
    # Keep track of which chair each friend is sitting on
    friend_to_chair = {}
    
    # Step 3: Process the events
    for time, event_type, friend_index in events:
        if event_type == 0:  # Friend is leaving
            # Add the chair they were using back to the available pool
            heapq.heappush(available_chairs, friend_to_chair[friend_index])
        else:  # Friend is arriving
            # Allocate the smallest available chair
            if available_chairs:
                chair = heapq.heappop(available_chairs)
            else:
                chair = next_chair
                next_chair += 1
            friend_to_chair[friend_index] = chair
            
            # If this is the target friend, return the chair number
            if friend_index == targetFriend:
                return chair
            
            
times = [[1, 4], [2, 3], [4, 6]]
targetFriend = 1
print(smallestChair(times, targetFriend))
