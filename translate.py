from scgraph_data.world_railways import graph, nodes

graph = list(graph.values())
nodes = [[i['latitude'], i['longitude']] for i in nodes.values()]

out_string = f"""
from scgraph.core import GeoGraph
graph={str(graph)}
nodes={str(nodes)}
world_railways_geograph = GeoGraph(graph=graph, nodes=nodes)
"""

with open("scgraph_data/world_railways.py", "w") as f:
    f.write(out_string)