# Proyecto Eficiencia (Django)

Pequeña app Django con patrón MVT que registra y lista mediciones energéticas.

## Requisitos
- Python 3.13 
- pip

## Instalación rápida
```bash
python -m venv .venv
. .venv/Scripts/activate   # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
