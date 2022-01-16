# kafka_spark_project
This README.md file provides details for kafka-to-spark pipeline installment locally and remotelly by using both Apache Airflow and Docker.

# Local installment

1) launching zookeeper:

/usr/local/zookeeper/zookeeper-3.7.0/bin/zkServer.sh start

this command starts up zookeeper on port 2181.

2) launching kafka server in daemon mode:

/usr/local/kafka/bin/kafka-server-start.sh -daemon /usr/local/kafka/config/server.properties

you may make sure that kafka server was launched by typing 'jps' command.
