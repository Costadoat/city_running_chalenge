import osmnx as ox
import networkx as nx
from progress.bar import Bar

def gen_route(G,points_list):
    bar = Bar('Processing', max=len(points_list), suffix='%(index)d/%(max)d - %(percent).1f%% - %(eta)ds')
    routes=[]
    route=[]
    for point1, point2 in zip(points_list[:-1], points_list[1:]):
        bar.next()
        orig = ox.get_nearest_node(G, point1) #reverse coordinates for (lat, lng)
        dest = ox.get_nearest_node(G, point2)
        try:
            intermediate_route = nx.shortest_path(G, orig, dest, weight='length')
            route.extend(intermediate_route[:-1]) #drop the endpoint of each intermediate route to not duplicate it (because it's also the start point of the next intermediate route)
        except:
            route.append(orig)
            routes.append(route)
            route=[]
    route.append(dest) # add the endpoint of the final intermediate route as it is the end of the route
    routes.append(route)
    bar.finish()
    return routes


