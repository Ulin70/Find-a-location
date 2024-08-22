from geopy.geocoders import Nominatim

def lacak_lokasi(alamat):
    geolocator = Nominatim(user_agent="my_location_tracker")
    location = geolocator.geocode(alamat)
    
    if location:
        print(f"Alamat: {location.address}")
        print(f"Latitude: {location.latitude}")
        print(f"Longitude: {location.longitude}")
    else:
        print("Lokasi tidak ditemukan.")

# Contoh penggunaan
alamat = input("Masukkan alamat atau nama tempat: ")
lacak_lokasi(alamat)