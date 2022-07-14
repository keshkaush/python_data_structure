# breadth first search answer 2 type of questions:
# 1. is there a path from node A to node B.
# 2. if there a path then find the shortest path from node A to B.
# it does not take weighted graph that is for diskastra algorithm
# basically it gives a path with that contains the less number of edges or nodes.
# directed graph put restriction on nodes meanwhile in undirected graph data can flow in any direction.

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["thom"] = []
graph["jonny"] = []
graph["anuj"] = []
graph["peggy"] = []

