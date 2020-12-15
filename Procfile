release: python manage.py migrate && python manage.py loaddata initial_data.json
web: gunicorn hunt_interiors.wsgi