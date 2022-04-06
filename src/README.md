# Notes backend.
This directory contains backend Django app REST API.


### Running.
To start development server:
```commandLIne
python manage.py runserver
```

### Deploying production.
Work in progress...
For production you may use gunicorn.
```commandLine
gunicorn --bind 0.0.0.0:8000 notes_web.wsgi
```

### Config.
Config values should be changed under `../../docker-compose.yml` file!