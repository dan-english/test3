# pull official base image
FROM python:3.8

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ=UTC


# install dependencies
RUN pip install --upgrade pip
# copy project
COPY . .
COPY .env.docker .env

RUN pip install -r requirements.txt

CMD [ "craft install" ]

# ports and volumes
EXPOSE 8000 3307
