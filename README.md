# model_about_django

Este proyecto es una aplicación web desarrollada con Django.

## Requisitos

- Python 3.10+
- Django 5.2.6

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

## Uso

1. Clona el repositorio:
   ```bash
   git clone <URL-del-repositorio>
   cd model_about_django
   ```

2. Realiza las migraciones:
   ```bash
   python manage.py migrate
   ```

3. Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

4. Accede a la aplicación en [http://localhost:8000](http://localhost:8000)

## Estructura del proyecto

- `requirements.txt`: Dependencias del proyecto.
- `manage.py`: Script de administración de Django.
- `django_template/`: Configuración principal del proyecto.
- `tasks/`: Aplicación principal.
- `README.md`: Este archivo.

## Licencia

Este proyecto está bajo la licencia MIT.