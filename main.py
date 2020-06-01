from settings import USERNAME, PASSWORD, VILLE, PAYS, FOLDER_COURSES, FILTER_TYPE
from read_gpx import read_gpx
from gen_route import gen_route
import os
import osmnx as ox


# Get gpx files from Garmin
#cmd="python src/gcexport3.py -d %s -c all -f gpx -u --username '%s' --password '%s'" % (FOLDER_COURSES, USERNAME, PASSWORD)
#os.system(cmd)

filepath = 'cartes/paris.graphml'
ox.utils.config(imgs_folder='.')
G = ox.load_graphml(filepath)

toutes_les_routes=[]
# Read gpx files
folder = os.listdir(FOLDER_COURSES)
for fichier in folder:
    if fichier.endswith(".gpx"):
        course=read_gpx(fichier)
        if VILLE in course['name'] and course['type'] in FILTER_TYPE:
            print(course['time'],course['name'])
            routes=gen_route(G,course['coordinates'])
            for route in routes:
                toutes_les_routes.append(route)

print(toutes_les_routes)
ox.plot_graph_routes(G, toutes_les_routes, node_size=0,edge_color='#999999', edge_linewidth=1, edge_alpha=1,route_color='#41a725',route_linewidth=1, route_alpha=1, orig_dest_node_size=0, show=True, save=True, close=True, file_format='svg', filename='run_city_challenge', dpi=300)
            
            

