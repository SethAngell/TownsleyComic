python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
gunicorn townsley.wsgi:application --bind 0.0.0.0:8000
