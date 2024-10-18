import heapq
import matplotlib.pyplot as plt
import networkx as nx

def a_star(graph, heuristics, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristics.get(start), 0, start, []))
    came_from = {}
    cost_so_far = {start: 0}
    while open_list:
        f, current_cost, current_node, path = heapq.heappop(open_list)
        if current_node == goal:
            return path + [current_node]
        for neighbor, cost in graph.get(current_node, {}).items():
            new_cost = current_cost + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristics.get(neighbor)
                heapq.heappush(open_list, (priority, new_cost, neighbor, path + [current_node]))
                came_from[neighbor] = current_node
    return None

graph = {"Kudal":{"Sawantwadi":3,"Kankavli":4,"Vengurla":2,"Malvan":1},
         "Sawantwadi":{"Vengurla":2,"Dodamarg":5,"Kudal":3},
         "Kankavli":{"Malvan":1,"Devgad":7,"Kudal":8,"Vaibhavwadi":9},
         "Devgad":{"Kankavli":4,"Malvan":5,"Vaibhavwadi":6},
         "Malvan":{"Kankavli":3,"Kudal":8,"Devgad":5,"Vengurla":2},
         "Vengurla":{"Sawantwadi":9,"Kudal":5,"Malvan":2},
         "Dodamarg":{"Sawantwadi":1},
         "Vaibhavwadi":{"Kankavli":8}
         }

heuristics={"Kudal":7,
            "Sawantwadi":3,
            "Malvan":2,
            "Vengurla":1,"Dodamarg":0,"Devgad":6,"Kankavli":9,"Vaibhavwadi":3}

grp=nx.Graph(graph)
nx.draw(grp,with_labels=True,node_color="white",font_color="black")
plt.show()

start_node="Kudal"
goal_node="Dodamarg"
path=a_star(graph,heuristics,start_node,goal_node)
if path:
    print("The Path is ",path)
else:
    print("The Path not found")
