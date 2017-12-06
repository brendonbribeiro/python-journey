import folium
import pandas

def get_icon_color(elev):
    if elev < 1000:
        return "green"
    elif 1000 <= elev < 3000:
        return "orange"
    else:
        return "red"

def get_country_color(pop):
    ten_mi = 10**7
    if pop < ten_mi:
        return "blue"
    elif ten_mi <= pop < 3.5 * ten_mi:
        return "green"
    elif 3.5 * ten_mi <= pop < 10 * ten_mi:
        return "orange"
    else:
        return "red"

#GET LAT_LNG FROM CSV FILE
volcanoes_df = pandas.read_csv("Volcanoes_USA.txt")[['LAT','LON', 'ELEV']]
volcanoes_dict = volcanoes_df.to_dict('records')

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles='openstreetmap')

volcanos_fg = folium.FeatureGroup(name="USA Volcanos")
for volcano in volcanoes_dict:
    marker = folium.CircleMarker(location=[volcano["LAT"], volcano["LON"]], popup="Elevation: " + str(volcano["ELEV"]) + "m",
        fill_color=get_icon_color(volcano["ELEV"]), color = "grey", radius=6, fill_opacity = 0.6, fill = True)
    ##fg.add_child(folium.Marker(location=[volcano["LAT"], volcano["LON"]], popup="Elevation: " + str(volcano["ELEV"]) + "m",
        ##icon=folium.Icon(color=get_icon_color(volcano["ELEV"]))))
    volcanos_fg.add_child(marker)
map.add_child(volcanos_fg)

pop_fg = folium.FeatureGroup(name="Country population")
worlds_file = open("world.json", encoding="utf-8-sig").read()
pop_fg.add_child(folium.GeoJson(data=worlds_file, style_function = lambda x : {
    "fillColor": get_country_color(x["properties"]["POP2005"]),
    "color": "white",
    "weight": 1
}))
map.add_child(pop_fg)

map.add_child(folium.LayerControl())
map.save("map.html")
