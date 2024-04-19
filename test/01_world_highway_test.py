import time
from pamda import pamda
from scgraph import Graph
from scgraph_data.world_highways import world_highways_geograph

def validate(name, realized, expected):
    if realized == expected:
        print(f'{name}: PASS')
    else:
        print(f'{name}: FAIL')
        print('Expected:', expected)
        print('Realized:', realized)

def time_test(name, thunk):
    start = time.time()
    thunk()
    print(f"{name}: {round(time.time()-start, 4)}s")

print('\n===============\nWorld Highway GeoGraph Tests:\n===============')

expected = {
    'length': 230.665, 
    'coordinate_path': [[42.29, -85.58], [42.272, -85.625], [42.269, -85.654], [42.238, -85.637], [42.273, -85.297], [42.273, -85.295], [42.271, -85.287], [42.268, -85.179], [42.29, -85.113], [42.299, -85.086], [42.3, -85.082], [42.297, -84.997], [42.283, -84.928], [42.284, -84.8], [42.264, -84.756], [42.263, -84.708], [42.272, -84.427], [42.279, -84.308], [42.292, -84.174], [42.292, -84.07], [42.295, -84.027], [42.289, -83.832], [42.289, -83.809], [42.29, -83.8], [42.3, -83.747], [42.304, -83.745], [42.31, -83.743], [42.32, -83.735], [42.323, -83.716], [42.324, -83.708], [42.324, -83.698], [42.326, -83.646], [42.383, -83.481], [42.39, -83.469], [42.391, -83.466], [42.386, -83.437], [42.386, -83.436], [42.382, -83.421], [42.382, -83.402], [42.383, -83.362], [42.383, -83.339], [42.385, -83.276], [42.386, -83.261], [42.386, -83.255], [42.385, -83.25], [42.383, -83.241], [42.379, -83.217], [42.379, -83.194], [42.379, -83.193], [42.381, -83.186], [42.382, -83.183], [42.384, -83.176], [42.383, -83.175], [42.374, -83.152], [42.372, -83.146], [42.371, -83.146], [42.37, -83.144], [42.367, -83.139], [42.367, -83.138], [42.363, -83.126], [42.35, -83.099], [42.346, -83.097], [42.336, -83.09], [42.331, -83.087], [42.33, -83.09]]
}


origin_node={
    "latitude": 42.29,
    "longitude": -85.58
}
destination_node={
    "latitude": 42.33,
    "longitude": -83.09
}


validate(
    name='Graph Validation',
    realized = world_highways_geograph.validate_graph(check_symmetry=True, check_connected=False),
    expected = None
)
validate(
    name='Node Validation',
    realized = world_highways_geograph.validate_nodes(),
    expected = None
)

validate(
    name='Dijkstra',
    realized = world_highways_geograph.get_shortest_path(
        origin_node=origin_node, 
        destination_node=destination_node,
        algorithm_fn=Graph.dijkstra
    ), 
    expected = expected
)

validate(
    name='Dijkstra-Makowski',
    realized = world_highways_geograph.get_shortest_path(
        origin_node=origin_node,
        destination_node=destination_node,
        algorithm_fn=Graph.dijkstra_makowski
    ), 
    expected = expected
)

print('\n===============\nWorld Highway GeoGraph Time Tests:\n===============')

time_test('Graph Validation', pamda.thunkify(world_highways_geograph.validate_graph)(check_symmetry=True, check_connected=False))
time_test('Node Validation', pamda.thunkify(world_highways_geograph.validate_nodes))

def dijkstra():
    world_highways_geograph.get_shortest_path(
        origin_node=origin_node, 
        destination_node=destination_node,
        algorithm_fn=Graph.dijkstra
    )

def dijkstra_makowski():
    world_highways_geograph.get_shortest_path(
        origin_node=origin_node,
        destination_node=destination_node,
        algorithm_fn=Graph.dijkstra_makowski
    )

time_test('Dijkstra', dijkstra)
time_test('Dijkstra-Makowski', dijkstra_makowski)
# world_highways_geograph.save_as_geojson('world_highways.geojson')