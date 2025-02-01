from geopy.geocoders import GoogleV3

# Substitua pela sua chave válida da API do Google
API_KEY = 'AIzaSyCsmSi_pP0vnKWzsnTvHzKxKiKcjzLEbsw'

# Inicializa o geocoder
geolocator = GoogleV3(api_key=API_KEY)

# Endereço que será buscado
endereco = '3, Floriano Miranda, São Paulo, SP'

# Faz a busca
try:
    location = geolocator.geocode(endereco)
    if location:
        print(f"Endereço completo: {location.address}")
        print(f"Coordenadas: {location.latitude}, {location.longitude}")
    else:
        print("Endereço não encontrado.")
except Exception as e:
    print(f"Erro: {e}")
