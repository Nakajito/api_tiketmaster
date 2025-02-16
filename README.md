# Ticketmaster Events Web App (Django)

Este es un sitio web en Python con Django que permite consultar eventos en Ticketmaster utilizando su API oficial.

## Descripción
La aplicación permite a los usuarios buscar eventos por palabra clave y país, mostrando los resultados de manera interactiva y amigable.

## Características
- Búsqueda de eventos en Ticketmaster.
- Filtrado por palabra clave y código de país.
- Interfaz web simple y fácil de usar.

## Tecnologías Utilizadas
- Python 3
- Django
- Ticketmaster API
- TailwindCss

## Instalación
1. Clona este repositorio:
    ```bash
    git clone https://github.com/Nakajito/api_tiketmaster
    cd api_tiketmaster
    ```

2. Crea un entorno virtual e instala las dependencias:
    ```bash
    python -m venv env
    source env/bin/activate  # En Linux/Mac
    env\Scripts\activate    # En Windows
    pip install -r requirements.txt
    ```

3. Configura tu clave de la API de Ticketmaster:
    - Reemplaza `TU_API_KEY_DE_TICKETMASTER` en el código por tu clave de la API.

4. Ejecuta las migraciones y corre el servidor:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

5. Abre tu navegador en `http://localhost:8000`.

## Uso
- Ingresa una palabra clave para buscar eventos.
- Opcionalmente, ingresa el código de país (por defecto es 'US').
- Visualiza los eventos encontrados, incluyendo fechas, ubicaciones y más.

## Contribuciones
¡Las contribuciones son bienvenidas! Si tienes alguna mejora o sugerencia, no dudes en crear un pull request.

## Licencia
Este proyecto está bajo la licencia MIT.

---
✨ ¡Gracias por usar esta aplicación para descubrir eventos increíbles! ✨
