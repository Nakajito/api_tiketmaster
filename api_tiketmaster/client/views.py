from django.shortcuts import render
import requests
from local_settings import ROOT_URL, API_KEY


# Create your views here.
def events(request):
    params = {
        'apikey' : API_KEY,
        'countryCode' : 'MX',
    }
    
    try:
        response = requests.get(f'{ROOT_URL}events.json?',params=params)
        response.raise_for_status()
        eventos = response.json().get('_embedded', {}).get('events', [])
    except requests.exceptions.RequestException as e:
        eventos = []
        print(f"Error al hacer la petición: {e}")
    
    
    return render(request,'layout/events.html', {
        'eventos': eventos,
        'ROOT_URL': ROOT_URL,
    })
