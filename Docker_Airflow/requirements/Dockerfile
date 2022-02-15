# This image was tested with 1.10.1 / 1.10.2 / 1.10.3 but seems to be working only with 1.10.1 version. 
FROM puckel/docker-airflow:1.10.1

USER root
RUN pip install --upgrade pip

# prerequisits for Java installation
RUN pip install --user psycopg2-binary && \
    pip install --user psycopg2
RUN mkdir -p /usr/share/man/man1

# Java installation
RUN apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get install -y ant && \
    apt-get clean;
    
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

USER airflow

WORKDIR /usr/local/airflow/

COPY requirements.txt .

RUN pip install --user -r requirements.txt

# To assembly a new version of the image into a container, follow these steps:
#
# docker-compose down 
# cd path/to/the/folder/containing/Dockerfile
# docker build .
# docker-compose build --pull
# docker-compose up (or docker-compose up airflow for quick check)
