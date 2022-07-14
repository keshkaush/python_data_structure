from collections import deque
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

def person_is_seller(name):
    return name[-1] == "m"

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f"{person} is the mango seller.")
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")