from geopy.geocoders import Nominatim

nom = Nominatim(scheme="http")

loc = nom.geocode("3995 23rd St, San Francisco, CA 94114")
print(loc.latitude)
