
FROM python:3.8


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install pipenv


RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin python-gdal python3-gdal libpq-dev postgis postgresql-11-postgis-scripts

RUN mkdir /src
WORKDIR /src

COPY Pipfile Pipfile.lock ./


RUN pipenv install --system --deploy


COPY /src .

# CMD ["python", "manage.py", "migrate", "--no-input"]