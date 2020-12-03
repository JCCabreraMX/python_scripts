from sys import argv
from os.path import exists
import simplejson as json 
 
script, in_file, out_file = argv
 
data = json.load(open(in_file))
 
geojson = {
    "type": "FeatureCollection",
    "name": "layername",
    "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:EPSG::4326" } },
    "features": [
    {"type": "Feature","properties": d, "geometry" : { "type": "MultiPoint", "coordinates": [d["lon"], d["lat"]]}} for d in data]
}
