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


#volcanoes.set_index("VOLCANX020")
for lt, ln, nm, elv in zip(lat, lon, name, elev):
    map.add_child(folium.Marker(location=[float(lt),float(ln)], popup=nm, icon=folium.Icon(color=color(elv))))
#for coordinates in [[38.2, -99.1],[37, -85], [44, -101]]:
#    map.add_child(folium.Marker(location=coordinates, popup="A spot", icon=folium.Icon(color='green')))

map.add_child(fg)
map.save("usa.html")
