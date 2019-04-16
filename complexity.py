#!/usr/bin/python3

from functools import total_ordering
import numpy as np
import itertools

from graphs import *

@total_ordering
class Infinity:
    # A simple representation of infinity
    # Its sole purpose is to be larger than any number
    def __eq__(self, other):
        # Infinity only equals other infinities
        return type(self) == type(other)

    def __ge__(self, other):
        # Infinity is always greater than or equal to
        return True

    def __add__(self, other):
        # Infinity plus anything is infinity
        return self
    def __radd__(self, other):
        return self

inf = Infinity()

def shortest_paths(graph):
    """
    Computes the shortest paths between any pair of vertices in the
    graph. It takes the input in adjacency-matrix form, and outputs
    another matrix.
    
    The computation is done via the Floyd-Warshall algorithm, which
    runs in O(V^3)."""
    n = len(graph)
    dists = [[graph[i][j] or inf for j in range(n)] for i in range(n)]
    for i in range(n):
        dists[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])
    return dists

def path_lengths(graph, reweight=True):
    """
    Computes a numpy array of the lengths of paths which are present in
    the graph. It takes the input in adjacency-matrix form, and outputs
    another matrix.
    
    If reweight is true, it then divides the lengths by the maximum
    minimum length that is found."""
    dists = shortest_paths(graph)
    ans = []
    n = len(graph)
    for i in range(n):
        for j in range(i):
            ans.append(dists[i][j])
    if reweight:
        return np.array(ans)/max(ans)
    else:
        return np.array(ans)

def exists_clique(graph, size):
    """
    Returns true iff there exists a clique of the given size in the
    graph"""
    for vs in itertools.combinations(range(len(graph)), size):
        for i,j in itertools.combinations(vs, 2):
            if not graph[i][j]:
                break
        else:
            return True
    return False

def max_clique_size(graph):
    """Computes the size of the largest clique in the graph."""
    for i in range(len(graph)):
        if not exists_clique(graph, i):
            return i-1
    return len(graph)

def complexity(graph):
    """Returns the complexity of the graph."""
    return np.var(path_lengths(graph))*max_clique_size(graph)
