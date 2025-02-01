from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="meu_aplicativo")
location = geolocator.geocode("3, Floriano miranda, Sao Paulo")
if location:
    print(location.address)
    print(location.latitude, location.longitude)
else:
    print("Endereço não encontrado!")
