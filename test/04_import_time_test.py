from time import time

print('\n===============\nWorld Highway and Marnet GeoGraph Tests:\n===============')

start_time = time()
from scgraph_data.world_highways import world_highways_geograph
print(f'World Highways GeoGraph loaded in {(time() - start_time)*1000:.2f} ms')

start_time = time()
from scgraph_data.world_highways_and_marnet import world_highways_and_marnet_geograph
print(f'World Highways and Marnet GeoGraph loaded in {(time() - start_time)*1000:.2f} ms')

start_time = time()
from scgraph_data.world_railways import world_railways_geograph
print(f'World Railways GeoGraph loaded in {(time() - start_time)*1000:.2f} ms')