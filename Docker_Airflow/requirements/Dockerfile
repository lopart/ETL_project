# This image was tested with 1.10.1 / 1.10.2 / 1.10.3 but seems to be working only with 1.10.1 version. 
FROM puckel/docker-airflow:1.10.1

USER root
RUN pip install --upgrade pip

# prerequisits for Java installation
RUN pip install --user psycopg2-binary && \
    pip install --user psycopg2
RUN mkdir -p /usr/share/man/man1

# Java installation (openjdk-8-jdk is depreciated)
RUN apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get install -y ant && \
    apt-get clean;
    
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

ARG SPARK_VERSION="3.2.1"
ARG HADOOP_VERSION="3.2"
ENV SPARK_HOME /usr/local/spark

# Installing Spark
RUN cd "/tmp" && \
        wget --no-verbose "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" && \
        tar -xvzf "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" && \
        mkdir -p "${SPARK_HOME}/bin" && \
        mkdir -p "${SPARK_HOME}/assembly/target/scala-2.12/jars" && \
        cp -a "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}/bin/." "${SPARK_HOME}/bin/" && \
        cp -a "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}/jars/." "${SPARK_HOME}/assembly/target/scala-2.12/jars/" && \
        rm "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz"

RUN export SPARK_HOME
ENV PATH $PATH:/usr/local/spark/bin

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
