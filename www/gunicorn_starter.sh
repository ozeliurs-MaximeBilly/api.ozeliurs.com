gunicorn main:app -w 3 --threads 3 -b 0.0.0.0:8000