import torch
import time
import ollama
import geopy.geocoders
from geopy.geocoders import Nominatim  
from ollama import llama3
# Para obtener la ubicación
# Función para obtener la ubicación actual
def get_current_location():
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode("Mi ubicación actual")
    return location.latitude, location.longitude

# Función para consultar al modelo de Llama 3
def query_ollama(location):
    llama3_model = llama3()
    response = llama3_model.query(location)
    return response

# Bucle principal
while True:
    # Obtener la ubicación actual
    latitude, longitude = get_current_location()

    # Consultar al modelo de Llama 3
    response = query_llama3((latitude, longitude))

    # Procesar y mostrar la respuesta
    print("Edificio a tu derecha:", response['edificio_derecha'])
    time.sleep(1)