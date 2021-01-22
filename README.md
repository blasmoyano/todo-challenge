# APP Control de tareas

La aplicación web permite a los usuarios crear y mantener una lista de tareas.
Para ver los requisitos del mismo leer el [enunciado](docs/ENUNCIADO.md)

## Instalación y Requerimientos

* [python 3.7](https://www.python.org/)
* [Django 3.1.5](https://www.djangoproject.com/)
* [django-filter 2.4.0](https://django-filter.readthedocs.io/en/stable/)
* [django-bootstrap-pagination 1.7.1](https://pypi.org/project/django-bootstrap-pagination/)
* [django-widget-tweaks 1.4.8](https://pypi.org/project/django-widget-tweaks/)
* [djangorestframework 3.12.2](https://www.django-rest-framework.org/)

```sh
$ cd todo-challenge
$ pip install -r requirements.txt
```

## Run
Para iniciar el proyecto se puede correr de dos maneras:
* desa
* prod

```sh
$ python manage.py makemigrations [task] --settings=app_control_lluvias.settings.[desa | prod]
$ python manage.py migrate --settings=app_control_lluvias.settings.[desa | prod]
$ python manage.py createsuperuser --settings=app_control_lluvias.settings.[desa | prod]
$ python manage.py runserver localhost:8080 --settings=app_control_lluvias.settings.[desa | prod]
```

# Test
```sh
python ./manage.py test tasks.tests  --settings=task_controller.settings.[desa | prod]
```

# urls
* /admin
* /login
* /logout
* /tasks/index
* /tasks/create
* /tasks/delete/<int>
* /tasks/edit/<int>
* /tasks/api/tareas
* /tasks/api/crear_tareas
* /tasks/api/borrar_tarea/<int>
* /tasks/api/update_tarea/<int>


# Me falta
 * docker ?
 * API DE BUSQEUDA
 * DOCS swagger
 * PEP