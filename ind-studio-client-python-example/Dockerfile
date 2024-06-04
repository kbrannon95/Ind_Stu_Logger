FROM python:2.7-slim

# Install dockerize
ENV DOCKERIZE_VERSION v0.6.1
RUN apt-get update && apt-get install -y wget iputils-ping \
    && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

WORKDIR /app
COPY . .
COPY ./requirements.txt .
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 5672

ENTRYPOINT [ "python", "./run.py" ]