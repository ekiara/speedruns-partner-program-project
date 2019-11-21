# speedruns-partner-program-project
A speedrun of a simple CRUD application and REST API implemented with Django
Rest Framework


***
***
## Deploy Instructions

### Clone the project:
```
git clone <this_project>
```

### Virtual environment (pipenv):
The project uses `pipenv` so you can initialize the virtual environment by
running the command below, while your shell is in the directory that contains
the `Pipfile` and `Pipfile.lock` files:

```
$ ls
api  manage.py  my.cnf  partners  Pipfile  Pipfile.lock  programs  project_api
projects  users

$ pipenv shell
(project_api) $
```

### Initialize Database:

Ensure that a empty MySQL database exists, and that you have created a user as
per the `my.cnf` file:

mysql> DROP DATABASE project_api;
mysql> CREATE DATABASE project_api;

### Initialize the environment:

This project uses the `envdir` utility to manage environment variables.
Currently the only environment being managed is the Django `SECRET_KEY`.

You will need to keep environment variables in an env (or envdir) directory and
ensure they are loaded by invoking the project like this:
```
(venv) $ envdir ../env python ./manage.py runserver
```

Or,  for something closer to what you will be doing in a production environment:
```
(venv) $ envdir ../env gunicorn --bind 0.0.0.0:8000 project_api.wsgi
```

***
***
## How to access the API

Note:
replace `http://project_api_server` with the actual address that your test
server is listening on.

#### Partner LIST: View list of all Partners
http GET http://project_api_server/api/v1/partners/

#### Partner READ: Detail view of an individual Partner
http GET http://project_api_server/api/v1/partners/66/

#### Partner CREATE
http POST http://project_api_server/api/v1/partners/create/ name="Baptist Church Youth Entrepreneurship Initiative"

#### Partner UPDATE
http PUT http://project_api_server/api/v1/partners/5/update/ name="Baptist Church Youth Entrepreneurship Fund"

#### Partner DELETE/DESTROY
http DELETE http://project_api_server/api/v1/partners/5/delete/

***

#### Program LIST: View list of all Programs
http GET http://project_api_server/api/v1/programs/

#### Program READ: Detail view of an individual Program
http GET http://project_api_server/api/v1/programs/3/

#### Program CREATE
http POST http://project_api_server/api/v1/programs/create/ program_name="Self-Help Group Initiative" partner_id=32
http POST http://project_api_server/api/v1/programs/create/ program_name="Self-Help Urban Programme" program_code="SHUP" partner_id=6

#### Program UPDATE
http PUT http://project_api_server/api/v1/programs/4/update/ program_name="Self-Help Urban & Rural Programme" program_code="SHURP"

#### Program DELETE/DESTROY
http DELETE http://project_api_server/api/v1/programs/4/delete/

***

#### Projects LIST: View list of all Projects
http GET http://project_api_server/api/v1/projects/

#### Projects READ: Detail view of an individual Project
http GET http://project_api_server/api/v1/projects/8/

#### Project CREATE
http POST http://project_api_server/api/v1/projects/create/ program_id=4
project_name="Project Fuor"

#### Project UPDATE
http PUT http://project_api_server/api/v1/projects/8/update/ project_name="Project
Number Four"

#### Project Delete
http DELETE http://project_api_server/api/v1/projects/8/delete/
