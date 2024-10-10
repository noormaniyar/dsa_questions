"""
    You are given a network of n nodes, labeled from 1 to n. You are also given times, 
    a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, 
    vi is the target node, and wi is the time it takes for a signal to travel from source to target.
    We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. 
    If it is impossible for all the n nodes to receive the signal, return -1.
"""
import heapq
import collections

def networkDelayTime(times, n, k):
    # Build the graph as an adjacency list
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    
    # Use a priority queue (min-heap) to store (travel_time, node)
    pq = [(0, k)]  # Starting with the source node k and 0 time
    dist = {i: float('inf') for i in range(1, n + 1)}  # Initialize distances
    dist[k] = 0  # Distance to the source is 0
    
    while pq:
        time, node = heapq.heappop(pq)
        
        # If we encounter a node with more time than the current distance, skip it
        if time > dist[node]:
            continue
        
        # Explore the neighbors
        for neighbor, weight in graph[node]:
            d = time + weight
            if d < dist[neighbor]:
                dist[neighbor] = d
                heapq.heappush(pq, (d, neighbor))
    
    # Get the maximum time taken to reach any node
    max_dist = max(dist.values())
    
    # If any node is unreachable, return -1
    return max_dist if max_dist < float('inf') else -1

times = [[1,2,1]] 
n = 2
k = 1
print(networkDelayTime(times, n, k))