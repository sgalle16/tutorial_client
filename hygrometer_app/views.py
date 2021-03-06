from django.shortcuts import render, HttpResponse
import requests

def hygrometer(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': 'hygrometer', 'value': value}
            response = requests.post('http://127.0.0.1:8000/hygrometer/', args)
            # Convierte la respuesta en JSON
            hygrometer_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/hygrometer/')
    # Convierte la respuesta en JSON
    hygrometer = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "hygrometer/hygrometer.html", {'hygrometer': hygrometer})
