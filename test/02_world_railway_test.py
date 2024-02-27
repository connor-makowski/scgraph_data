import time
from pamda import pamda
from scgraph import Graph
from scgraph_data.world_railways import world_railways_geograph

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

print('\n===============\nWorld Railway GeoGraph Tests:\n===============')

expected = {
    'path': [274974, 25575, 25577, 34436, 34437, 34438, 25581, 25580, 25541, 25539, 25542, 37015, 25559, 25556, 25558, 39059, 39058, 37754, 37752, 37753, 38538, 38537, 38536, 38535, 36995, 36993, 25571, 25570, 25568, 25567, 25569, 20524, 20523, 20525, 20806, 20804, 20805, 28561, 20502, 20501, 20496, 20495, 20497, 28580, 28581, 20542, 20541, 20543, 28602, 28601, 20507, 20505, 20506, 20553, 20554, 20555, 20566, 20564, 20565, 20551, 19454, 20521, 20522, 20530, 20529, 20531, 28589, 274975], 
    'length': 226.7168, 
    'coordinate_path': [{'latitude': 42.29, 'longitude': -85.58}, {'longitude': -85.583, 'latitude': 42.296}, {'longitude': -85.578, 'latitude': 42.296}, {'longitude': -85.573, 'latitude': 42.296}, {'longitude': -85.569, 'latitude': 42.296}, {'longitude': -85.564, 'latitude': 42.294}, {'longitude': -85.546, 'latitude': 42.288}, {'longitude': -85.519, 'latitude': 42.289}, {'longitude': -85.337, 'latitude': 42.337}, {'longitude': -85.228, 'latitude': 42.331}, {'longitude': -85.194, 'latitude': 42.32}, {'longitude': -85.193, 'latitude': 42.32}, {'longitude': -85.172, 'latitude': 42.312}, {'longitude': -85.17, 'latitude': 42.312}, {'longitude': -85.15, 'latitude': 42.315}, {'longitude': -85.144, 'latitude': 42.315}, {'longitude': -85.141, 'latitude': 42.315}, {'longitude': -85.131, 'latitude': 42.302}, {'longitude': -84.959, 'latitude': 42.266}, {'longitude': -84.504, 'latitude': 42.254}, {'longitude': -84.483, 'latitude': 42.255}, {'longitude': -84.457, 'latitude': 42.254}, {'longitude': -84.444, 'latitude': 42.251}, {'longitude': -84.424, 'latitude': 42.253}, {'longitude': -84.409, 'latitude': 42.25}, {'longitude': -84.407, 'latitude': 42.25}, {'longitude': -84.406, 'latitude': 42.249}, {'longitude': -84.398, 'latitude': 42.247}, {'longitude': -84.361, 'latitude': 42.235}, {'longitude': -84.351, 'latitude': 42.233}, {'longitude': -84.348, 'latitude': 42.233}, {'longitude': -84.264, 'latitude': 42.243}, {'longitude': -83.892, 'latitude': 42.34}, {'longitude': -83.89, 'latitude': 42.34}, {'longitude': -83.755, 'latitude': 42.308}, {'longitude': -83.748, 'latitude': 42.303}, {'longitude': -83.661, 'latitude': 42.271}, {'longitude': -83.644, 'latitude': 42.267}, {'longitude': -83.633, 'latitude': 42.259}, {'longitude': -83.487, 'latitude': 42.261}, {'longitude': -83.397, 'latitude': 42.276}, {'longitude': -83.387, 'latitude': 42.278}, {'longitude': -83.386, 'latitude': 42.278}, {'longitude': -83.329, 'latitude': 42.288}, {'longitude': -83.31, 'latitude': 42.291}, {'longitude': -83.272, 'latitude': 42.298}, {'longitude': -83.258, 'latitude': 42.301}, {'longitude': -83.251, 'latitude': 42.303}, {'longitude': -83.242, 'latitude': 42.305}, {'longitude': -83.235, 'latitude': 42.307}, {'longitude': -83.221, 'latitude': 42.309}, {'longitude': -83.215, 'latitude': 42.31}, {'longitude': -83.193, 'latitude': 42.313}, {'longitude': -83.192, 'latitude': 42.313}, {'longitude': -83.176, 'latitude': 42.315}, {'longitude': -83.16, 'latitude': 42.318}, {'longitude': -83.158, 'latitude': 42.318}, {'longitude': -83.136, 'latitude': 42.321}, {'longitude': -83.114, 'latitude': 42.324}, {'longitude': -83.108, 'latitude': 42.325}, {'longitude': -83.107, 'latitude': 42.325}, {'longitude': -83.101, 'latitude': 42.326}, {'longitude': -83.1, 'latitude': 42.326}, {'longitude': -83.098, 'latitude': 42.327}, {'longitude': -83.094, 'latitude': 42.327}, {'longitude': -83.092, 'latitude': 42.327}, {'longitude': -83.09, 'latitude': 42.328}, {'latitude': 42.33, 'longitude': -83.09}]
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
    realized = world_railways_geograph.validate_graph(check_symmetry=True, check_connected=False),
    expected = None
)
validate(
    name='Node Validation',
    realized = world_railways_geograph.validate_nodes(),
    expected = None
)

validate(
    name='Dijkstra',
    realized = world_railways_geograph.get_shortest_path(
        origin_node=origin_node, 
        destination_node=destination_node,
        algorithm_fn=Graph.dijkstra
    ), 
    expected = expected
)

validate(
    name='Dijkstra-Makowski',
    realized = world_railways_geograph.get_shortest_path(
        origin_node=origin_node,
        destination_node=destination_node,
        algorithm_fn=Graph.dijkstra_makowski
    ), 
    expected = expected
)

print('\n===============\nWorld Railway GeoGraph Time Tests:\n===============')

time_test('Graph Validation', pamda.thunkify(world_railways_geograph.validate_graph)(check_symmetry=True, check_connected=False))
time_test('Node Validation', pamda.thunkify(world_railways_geograph.validate_nodes))

def dijkstra():
    world_railways_geograph.get_shortest_path(
        origin_node=origin_node, 
        destination_node=destination_node,
        algorithm_fn=Graph.dijkstra
    )

def dijkstra_makowski():
    world_railways_geograph.get_shortest_path(
        origin_node=origin_node,
        destination_node=destination_node,
        algorithm_fn=Graph.dijkstra_makowski
    )

time_test('Dijkstra', dijkstra)
time_test('Dijkstra-Makowski', dijkstra_makowski)
# world_railways_geograph.save_as_geojson('world_railways.geojson')