import constraint
import matplotlib.pyplot as plt
import networkx as nx

problem = constraint.Problem()

# Define the regions and their respective domains (colors)
regions = ['Kudal', 'Sawantwadi', 'Kankavli', 'Devgad', 'Malvan', 'Vengurla', 'Dodamarg','Vaibhavwadi']
colors = ['Red', 'Green', 'Blue','Pink','Black','Grey','Purple']
for region in regions:
    problem.addVariable(region, colors)
neighbors = {"Kudal":["Sawantwadi","Kankavli","Vengurla","Malvan"],
         "Sawantwadi":["Vengurla","Dodamarg","Kudal"],
         "Kankavli":["Malvan","Devgad","Kudal","Vaibhavwadi"],------
         "Devgad":["Kankavli","Malvan","Vaibhavwadi"],
         "Malvan":["Kankavli","Kudal","Devgad","Vengurla"],
         "Vengurla":["Sawantwadi","Kudal","Malvan"],
         "Dodamarg":["Sawantwadi"],
         "Vaibhavwadi":["Kankavli"] 
    }

for region, adjacent in neighbors.items():
    for neighbor in adjacent:
        problem.addConstraint(lambda region, neighbor: region != neighbor,(region,neighbor))
solution=problem.getSolution()
print(solution)

grp=nx.Graph(neighbors)
nx.draw(grp,with_labels=True,node_color="white",font_color="black")
plt.show()
