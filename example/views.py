import os
import requests
import subprocess
import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

def custom_404(request, exception):
    return render(request, '404.html',{})

# Login para verificar el acceso a panel
@csrf_exempt
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Almacenar el correo en la sesión (para usuarios autenticados)
            request.session['user_email'] = user.email
            login(request, user)
            return render(request, 'home.html', {'user_email': user.email})
        elif 'correo' in request.POST and 'firma' in request.POST and 'certificado' in request.POST:
            correo = request.POST.get('correo')
            firma = request.POST.get('firma')
            certificado = request.POST.get('certificado')
            data = {'user_email': correo, 
                    'firma': firma, 
                    'certificado': certificado
                    }
            # Almacenar el correo en la sesión (para otros usuarios)
            request.session['user_email'] = correo
            
            # Aquí deberías implementar la lógica de validación para estas variables
            user = authenticate(request, username='jose', password='Capstonejose')
            if user is not None:
                login(request, user)
                return render(request, 'home.html', data)
            else:
                return render(request, 'login.html', {'error_message': 'Credenciales incorrectas'})
        else:
            return render(request, 'login.html', {'error_message': 'Credenciales incorrectas o falta información'})
    
    return render(request, 'login.html')
# Cerrar sesion
def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):
    # Obtener el correo de la sesión
    user_email = request.session.get('user_email', 'Correo no disponible')
    
    # Aquí puedes usar 'user_email' como lo desees, por ejemplo, mostrarlo en el template
    return render(request, 'home.html', {'user_email': user_email})


def run_script(request):
    """Ejecuta el script main.py y devuelve la salida."""
    try:
        # Ejecuta el script main.py
        result = subprocess.run(
            ['python', 'modulos\main.py'],
            capture_output=True,
            text=True,
            check=True  # Esto lanzará una excepción si el script falla
        )
        # Retorna el resultado en formato JSON
        return JsonResponse({'output': result.stdout})
    except subprocess.CalledProcessError as e:
        # Captura errores de ejecución del script
        return JsonResponse({'error': f'Error al ejecutar el script: {e.stderr}'})
    except Exception as e:
        # Captura cualquier otro tipo de error
        return JsonResponse({'error': f'Error inesperado: {str(e)}'})
    
@login_required(login_url='/login/')
def panel(request):
    try:
        return render(request, 'panel.html')
    except Exception as e:
        return render(request, 'error.html', {'error_message': str(e)})

# Leer archivo de logs de ejecuciones en scraping
def get_logs(request):
    """Lee el archivo logs_scraping.txt y devuelve su contenido como JSON."""
    try:
        log_file_path = "logs_scraping.txt"
        with open(log_file_path, "r") as log_file:
            logs = log_file.readlines()
        return JsonResponse({'logs': logs})
    except Exception as e:
        return JsonResponse({'error': f'Error al leer el archivo: {str(e)}'})
    
# datos de 'logs_scraping.txt' enviados a API mockapi

def enviar_logs_a_api():
    url = "https://671d555c09103098807cd937.mockapi.io/api/odorwatch/logs_scraping"
    
    # Leer el contenido completo del archivo de logs
    with open('logs_scraping.txt', 'r') as file:
        logs = file.read()
    
    # Crear el payload con el contenido de logs
    data = {
        "logs": logs
    }
    
    try:
        # Enviar el contenido a la API mediante una solicitud POST
        response = requests.post(url, json=data)
        
        # Verificar si la solicitud fue exitosa
        if response.status_code == 201:
            print("Logs enviados con éxito a la API.")
        else:
            print(f"Error al enviar los logs. Código de respuesta: {response.status_code}")
            print("Respuesta:", response.text)
            
    except Exception as e:
        print(f"Ocurrió un error al intentar enviar los logs: {e}")

# Llamada a la función para enviar los logs
enviar_logs_a_api()


def snifa(request):
    return render(request, 'snifa.html')