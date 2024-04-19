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
    'length': 226.2816, 
    'coordinate_path': [[42.29, -85.58], [42.296, -85.578], [42.296, -85.573], [42.296, -85.569], [42.294, -85.564], [42.288, -85.546], [42.289, -85.519], [42.337, -85.337], [42.331, -85.228], [42.32, -85.194], [42.32, -85.193], [42.312, -85.172], [42.312, -85.17], [42.315, -85.15], [42.315, -85.144], [42.315, -85.141], [42.302, -85.131], [42.266, -84.959], [42.254, -84.504], [42.255, -84.483], [42.254, -84.457], [42.251, -84.444], [42.253, -84.424], [42.25, -84.409], [42.25, -84.407], [42.249, -84.406], [42.247, -84.398], [42.235, -84.361], [42.233, -84.351], [42.233, -84.348], [42.243, -84.264], [42.34, -83.892], [42.34, -83.89], [42.308, -83.755], [42.303, -83.748], [42.271, -83.661], [42.267, -83.644], [42.259, -83.633], [42.261, -83.487], [42.276, -83.397], [42.278, -83.387], [42.278, -83.386], [42.288, -83.329], [42.291, -83.31], [42.298, -83.272], [42.301, -83.258], [42.303, -83.251], [42.305, -83.242], [42.307, -83.235], [42.309, -83.221], [42.31, -83.215], [42.313, -83.193], [42.313, -83.192], [42.315, -83.176], [42.318, -83.16], [42.318, -83.158], [42.321, -83.136], [42.324, -83.114], [42.325, -83.108], [42.325, -83.107], [42.326, -83.101], [42.326, -83.1], [42.327, -83.098], [42.327, -83.094], [42.327, -83.092], [42.328, -83.09], [42.33, -83.09]]
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