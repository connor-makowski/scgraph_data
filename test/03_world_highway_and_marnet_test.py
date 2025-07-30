import time
from pamda import pamda
from scgraph import Graph
from scgraph_data.world_highways_and_marnet import world_highways_and_marnet_geograph

def validate(name, realized, expected):
    if realized == expected:
        print(f'{name}: PASS')
    else:
        print(f'{name}: FAIL')

def time_test(name, thunk):
    start = time.time()
    thunk()
    print(f"{name}: {round(time.time()-start, 4)}s")

print('\n===============\nWorld Highway and Marnet GeoGraph Tests:\n===============')

expected = {}


origin_node={
    "latitude": 42.29,
    "longitude": 25
}
destination_node={
    "latitude": 42.33,
    "longitude": -83.09
}


validate(
    name='Graph Validation',
    realized = world_highways_and_marnet_geograph.validate_graph(check_symmetry=True, check_connected=False),
    expected = None
)
validate(
    name='Node Validation',
    realized = world_highways_and_marnet_geograph.validate_nodes(),
    expected = None
)

print('\n===============\nWorld Highway and Marnet GeoGraph Time Tests:\n===============')

time_test('Graph Validation', pamda.thunkify(world_highways_and_marnet_geograph.validate_graph)(check_symmetry=True, check_connected=False))
time_test('Node Validation', pamda.thunkify(world_highways_and_marnet_geograph.validate_nodes))


def dijkstra_makowski():
    world_highways_and_marnet_geograph.get_shortest_path(
        origin_node=origin_node,
        destination_node=destination_node,
        algorithm_fn=Graph.dijkstra_makowski
    )

time_test('Dijkstra-Makowski', dijkstra_makowski)
# world_highways_and_marnet_geograph.save_as_geojson('world_highways.geojson')