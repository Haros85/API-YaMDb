FROM python:3.8.5

WORKDIR /code

COPY requirements.txt /code
COPY fixtures.json /code

RUN pip install -r /code/requirements.txt

COPY . /code

RUN python manage.py collectstatic --noinput

CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:5000