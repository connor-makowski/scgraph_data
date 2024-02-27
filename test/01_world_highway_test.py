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
    'path': [560282, 251528, 226549, 172821, 172820, 172823, 172824, 226688, 226728, 226729, 226724, 226722, 226720, 226717, 226715, 226716, 226719, 226992, 226996, 185573, 185571, 185572, 185685, 185687, 185565, 185562, 185558, 185561, 185563, 185566, 185567, 185570, 185680, 185974, 185971, 185969, 185965, 185966, 185970, 185973, 185700, 185620, 185611, 185610, 185608, 185603, 185597, 185601, 185607, 185614, 185624, 185625, 185721, 185612, 185847, 185833, 185834, 185831, 185835, 185668, 185660, 185658, 185922, 185919, 560283], 
    'length': 230.665, 
    'coordinate_path': [{'latitude': 42.29, 'longitude': -85.58}, {'longitude': -85.625, 'latitude': 42.272}, {'longitude': -85.654, 'latitude': 42.269}, {'longitude': -85.637, 'latitude': 42.238}, {'longitude': -85.297, 'latitude': 42.273}, {'longitude': -85.295, 'latitude': 42.273}, {'longitude': -85.287, 'latitude': 42.271}, {'longitude': -85.179, 'latitude': 42.268}, {'longitude': -85.113, 'latitude': 42.29}, {'longitude': -85.086, 'latitude': 42.299}, {'longitude': -85.082, 'latitude': 42.3}, {'longitude': -84.997, 'latitude': 42.297}, {'longitude': -84.928, 'latitude': 42.283}, {'longitude': -84.8, 'latitude': 42.284}, {'longitude': -84.756, 'latitude': 42.264}, {'longitude': -84.708, 'latitude': 42.263}, {'longitude': -84.427, 'latitude': 42.272}, {'longitude': -84.308, 'latitude': 42.279}, {'longitude': -84.174, 'latitude': 42.292}, {'longitude': -84.07, 'latitude': 42.292}, {'longitude': -84.027, 'latitude': 42.295}, {'longitude': -83.832, 'latitude': 42.289}, {'longitude': -83.809, 'latitude': 42.289}, {'longitude': -83.8, 'latitude': 42.29}, {'longitude': -83.747, 'latitude': 42.3}, {'longitude': -83.745, 'latitude': 42.304}, {'longitude': -83.743, 'latitude': 42.31}, {'longitude': -83.735, 'latitude': 42.32}, {'longitude': -83.716, 'latitude': 42.323}, {'longitude': -83.708, 'latitude': 42.324}, {'longitude': -83.698, 'latitude': 42.324}, {'longitude': -83.646, 'latitude': 42.326}, {'longitude': -83.481, 'latitude': 42.383}, {'longitude': -83.469, 'latitude': 42.39}, {'longitude': -83.466, 'latitude': 42.391}, {'longitude': -83.437, 'latitude': 42.386}, {'longitude': -83.436, 'latitude': 42.386}, {'longitude': -83.421, 'latitude': 42.382}, {'longitude': -83.402, 'latitude': 42.382}, {'longitude': -83.362, 'latitude': 42.383}, {'longitude': -83.339, 'latitude': 42.383}, {'longitude': -83.276, 'latitude': 42.385}, {'longitude': -83.261, 'latitude': 42.386}, {'longitude': -83.255, 'latitude': 42.386}, {'longitude': -83.25, 'latitude': 42.385}, {'longitude': -83.241, 'latitude': 42.383}, {'longitude': -83.217, 'latitude': 42.379}, {'longitude': -83.194, 'latitude': 42.379}, {'longitude': -83.193, 'latitude': 42.379}, {'longitude': -83.186, 'latitude': 42.381}, {'longitude': -83.183, 'latitude': 42.382}, {'longitude': -83.176, 'latitude': 42.384}, {'longitude': -83.175, 'latitude': 42.383}, {'longitude': -83.152, 'latitude': 42.374}, {'longitude': -83.146, 'latitude': 42.372}, {'longitude': -83.146, 'latitude': 42.371}, {'longitude': -83.144, 'latitude': 42.37}, {'longitude': -83.139, 'latitude': 42.367}, {'longitude': -83.138, 'latitude': 42.367}, {'longitude': -83.126, 'latitude': 42.363}, {'longitude': -83.099, 'latitude': 42.35}, {'longitude': -83.097, 'latitude': 42.346}, {'longitude': -83.09, 'latitude': 42.336}, {'longitude': -83.087, 'latitude': 42.331}, {'latitude': 42.33, 'longitude': -83.09}]
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