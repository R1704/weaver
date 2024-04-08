import numpy as np
import sys

# Use this from command line as such: python weaver.py <source> <target> 
# requirement: numpy

with open('words4.txt', 'r') as f:
    words = f.read().split()
N = len(words)

# checks if there is exactly one different character between two words
def one_diff(w1: str, w2: str) -> bool:
    return sum(1 for x, y in zip(list(w1), list(w2)) if x != y) == 1

# dictionary with words as keys and a list of words with one different character as values
neighbors = {i: 
[j for j in range(len(words)) if one_diff(words[i], words[j])]
 for i in range(len(words))}

# Dijkstra's algorithm to find a minimal path between two words
def dijkstra(source, target):
    dist = np.repeat(np.inf, N)
    prev = np.repeat(None, N)
    Q = np.arange(N)
    dist[source] = 0
    
    while len(Q) != 0:
        u = Q[np.argmin(dist[Q])]
        if u == target:
            return prev
        Q = Q[Q != u]
        for v in neighbors[u]:
            if v in Q:
                alt = dist[u] + 1
                if alt < dist[v] and dist[u] != np.inf:
                    dist[v] = alt
                    prev[v] = u
    return prev

def retrieve_path(source, target, prev):
    path = []
    u = target
    if prev[u] is not None or u == source:
        while u is not None:
            path.insert(0, u)
            u = prev[u]
    return path

# getting arguments from command line
def get_args():
    s, t = sys.argv[1:]
    return words.index(s), words.index(t) 

def main():
    source, target = get_args()
    prev = dijkstra(source, target)
    path = retrieve_path(source, target, prev)
    path = [words[p] for p in path]
    print(path)

main()
