import folium
import pandas
#help:
#help(foilum.Map)
#initialize new folium map
map = folium.Map(location=[39, -98], zoom_start=4, tiles="Mapbox Bright")
#add markers
fg = folium.FeatureGroup(name="My Map")

volcanoes = pandas.read_csv("./data/Volcanoes.txt")
lat = list(volcanoes["LAT"])
lon = list(volcanoes["LON"])
name = list(volcanoes["NAME"])
elev = list(volcanoes["ELEV"])

def color(elevation):
    if elevation < 1600:
        return "green"
    elif elevation < 2600:
        return "orange"
    else:
        return "red"

def marker(elevation):
    return folium.map.CircleMarker(radius=3, color="blue")

#volcanoes.set_index("VOLCANX020")
for lt, ln, nm, elv in zip(lat, lon, name, elev):
    map.add_child(folium.CircleMarker(location=[float(lt),float(ln)], radius=5, popup=nm, fill_color=color(elv), color='grey', fill_opacity=0.7))
    #map.add_child(folium.Marker(location=[float(lt),float(ln)], popup=nm, icon=folium.Icon(color=color(elv))))

fg.add_child(folium.GeoJson(data=open("./data/world.json", 'r', encoding='utf-8-sig'),
style_function=lambda x: {'fillColor' : 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 15000000 <= x['properties']['POP2005'] < 40000000 else 'red'}))
map.add_child(fg)
map.add_child(folium.LayerControl()) #this needs to be added after the feature group
map.save("usa.html")
