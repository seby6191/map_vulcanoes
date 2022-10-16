import folium
import pandas
data=pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation <3000:
        return "orange"
    else: return "red"
html = """<h4>Informatii vulcan:</h4>
Inaltime: %s m
"""
map = folium.Map(location=[38.50,-99.09], zoom_start=5, tiles = "Stamen Terrain")
fgv=folium.FeatureGroup(name="Vulcani")
for lt,ln,el in zip(lat,lon,elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=folium.Popup(iframe),icon=folium.Icon(color=color_producer(el)),
    fill_color = color_producer(el), color="grey", fill_opacity=0.7))
fgp = folium.FeatureGroup(name="Populatie")
fgp.add_child(folium.GeoJson(data=open("world.json","r", encoding="utf-8-sig").read(),
style_function=lambda x:{"fillColor":"yellow" if x["properties"]["POP2005"] < 10000000
else "orange" if 10000000<= x["properties"]["POP2005"]<20000000 else "red"}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")