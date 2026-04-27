python manage.py collectstatic --noinput
python manage.py collectstatic --noinput
gunicorn jango_deployment.wsgi:application --bind 0.0.0.0 :$PORT
