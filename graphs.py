"""
This module contains functions to build adjacency matrices for common
graph families that I may wish to use."""

import itertools
import random

def p(n):
    return [[int(abs(i-j) == 1) for j in range(n)] for i in range(n)]

def c(n):
    cycle = p(n)
    cycle[0][-1] = 1
    cycle[-1][0] = 1
    return cycle

def k(n):
    return [[int(i != j) for j in range(n)] for i in range(n)]

def tree(n):
    g = [[0 for i in range(n)] for j in range(n)]
    for i in range(1, n):
        add_edge(g, random.randrange(i), i)
    return g

def graph_edges(n, *edges):
    g = [[0 for i in range(n)] for j in range(n)]
    add_edges(g, *edges)
    return g

def add_edge(graph, i, j):
    graph[i][j] = 1
    graph[j][i] = 1
def add_edges(graph, *edges):
    for i, j in edges:
        add_edge(graph, i, j)

def remove_edge(graph, i, j):
    graph[i][j] = 0
    graph[j][i] = 0
def remove_edges(graph, *edges):
    for i, j in edges:
        remove_edge(graph, i, j)

def combine_graphs(g1, g2):
    c = [[0 for i in range(len(g1)+len(g2))] for j in range(len(g1)+len(g2))]
    for i in range(len(g1)):
        for j in range(len(g1)):
            c[i][j] = g1[i][j]
    for i in range(len(g2)):
        for j in range(len(g2)):
            c[i+len(g1)][j+len(g1)] = g2[i][j]
    return c

graph_a = k(8)
remove_edges(graph_a, (0, 1), (0, 2), (1, 2))

graph_b = graph_edges(8, (0, 1), (0, 2), (1, 4), (2, 3), (2, 6), (4, 6),
                         (5, 7), (6, 7))

