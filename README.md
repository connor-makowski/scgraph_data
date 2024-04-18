# scgraph_data
[![PyPI version](https://badge.fury.io/py/scgraph_data.svg)](https://badge.fury.io/py/scgraph_data)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Large geograph data for the [scgraph](https://github.com/connor-makowski/scgraph) package. This package includes larger geographs that would be too large to include in the main scgraph package. These geographs include larger and more complete networks like the world highway and world railway networks. 

Please note that these geographs are simplified and are not 100% accurate. They are also not directional geographs and should not be used for navigation or any other safety critical applications.


## Setup

Make sure you have Python 3.6.x (or higher) installed on your system. You can download it [here](https://www.python.org/downloads/).

## Installation

```
pip install scgraph_data
```

## Included GeoGraphs

- world_highways_geograph:
    - What: World highway network from OpenStreetMap
    - Use: `from scgraph_data.world_highways import world_highways_geograph`
    - Attribution: [OpenStreetMaps](https://www.openstreetmap.org/)
    - Length Measurement: Kilometers
    - [World Highways Picture](https://raw.githubusercontent.com/connor-makowski/scgraph_data/main/static/world_highways.png)
- world_railways_geograph:
    - What: World railway network from OpenStreetMap
    - Use: `from scgraph_data.world_railways import world_railways_geograph`
    - Attribution: [OpenStreetMaps](https://www.openstreetmap.org/)
    - Length Measurement: Kilometers
    - [World Railways Picture](https://raw.githubusercontent.com/connor-makowski/scgraph_data/main/static/world_railways.png)
- world_highways_and_marnet_geograph:
    - What: World highway and marnet network joined by ports
    - Use: `from scgraph_data.world_highways_and_marnet import world_highways_and_marnet_geograph`
    - Attribution: [OpenStreetMaps](https://www.openstreetmap.org/)
    - Attribution: [searoute](https://github.com/genthalili/searoute-py)
    - Length Measurement: Kilometers
    - [World Highways and Marnet Picture](https://raw.githubusercontent.com/connor-makowski/scgraph_data/main/static/world_highways_and_marnet.png)
    - Note: These two networks are connected by ports, where each port is joined to each respective network by using the closest euclidian entry point.
    - [Used Ports Picture](https://raw.githubusercontent.com/connor-makowski/scgraph_data/main/static/world_highway_and_marnet_port_connections.png)