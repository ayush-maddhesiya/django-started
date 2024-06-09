# Using UV for Python Virtual Environment 

<p> after installtion we have to active uv as virtual env , so that we dont pollute our whole system. </p>

```source .venv/Scripts/activate```

```uv pip install django```

## Creating a project/app

```django-admin startproject chaiaurdjango```
### this command is run *once a project*, not multiple time.


## Running a project
```python manage.py runserver```
<p> this commmand is just like npm run dev </p>

## Specify Port
```python manage.py runserver 8001```
<p>You can specify the port directly in the terminal to run the server on a different port.</p>