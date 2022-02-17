# ETL_project (under construction)
This README.md file provides details for kafka-to-spark pipeline instalment locally and remotely by using both Apache Airflow and Docker.
![alt_text](https://github.com/Gitnuts/kafka_spark_project/blob/main/schema.png)

# Local instalment

1) Launching zookeeper:

/usr/local/zookeeper/zookeeper-3.7.0/bin/zkServer.sh start

This command starts up zookeeper on port 2181.

2) Launching kafka server in daemon mode:

/usr/local/kafka/bin/kafka-server-start.sh -daemon /usr/local/kafka/config/server.properties

you may make sure that the kafka server was launched by typing 'jps' command. Next step is topic creation

/usr/local/kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:2181 --replication-factor 1 --partitions 1 --topic test

3) Producing messages with KafkaProduce

/usr/local/kafka/bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test --from-beginning

alternatively you can run python script 

4) Consuming messages with KafkaProduce

/usr/local/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning

same as production, you may define a python script that will consume all the messages.

5) Spark structured streaming through pyspark.sql

/usr/local/spark/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0  kafka_to_spark.py

Make sure that spark-sql-kafka package is included. Note that pyspark.streaming.kafka is deprecated in 2.3.0. Kafka 0.8 support is deprecated as of Spark 2.3.0. Thus, all operations must be conducted through pyspark.sql.SparkSession only.
