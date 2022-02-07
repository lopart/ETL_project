from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.2.0,org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0 pyspark-shell'
from ast import literal_eval

if __name__ == '__main__':
	
	spark = SparkSession.builder.appName("Kafka2Spark").getOrCreate()

	schema1 = StructType([
		StructField("id", StringType(), True),
		StructField("sport_key", StringType(), True),
		StructField("sport_title", StringType(), True),
		StructField("commence_time", StringType(), True),
		StructField("home_team", StringType(), True),
		StructField("away_team", StringType(), True),
		StructField("bookmakers", ArrayType(StructType([
			StructField("title", StringType(), True),
			StructField("last_update", StringType(), True),
			StructField("markets", ArrayType(StructType([
				StructField("key", StringType(), True),
				StructField("outcomes", ArrayType(StructType([
					StructField("name", StringType(), True),
					StructField("price", StringType(), True)
					])))
				])))]
		)))])


	df = spark.readStream.format("kafka").option("kafka.bootstrap.servers",'localhost:9092').option("subscribe",'test').option("startingOffset", "earliest").load()
	df = df.selectExpr("CAST(value AS STRING)")
	df = df.select(from_json(df.value, schema1).alias("data")).withColumn("bookmaker", explode("data.bookmakers")).withColumn("market", explode("bookmaker.markets")).withColumn("outcome", explode("market.outcomes")).selectExpr("data.id", "bookmaker.title", "market.key", "outcome.*")

	final_df = df.writeStream.trigger(processingTime='20 seconds').option("checkpointLocation", "/private/tmp/kafka_output").option("path", "/private/tmp/kafka_output").format("csv").outputMode("append").start()

	# .option("truncate","false") 
	# .format("memory")
	# .queryName("sql_1")
	# .option("checkpointLocation", "/private/tmp/kafka_output")
	# .option("path", "/private/tmp/kafka_output")


	final_df.awaitTermination()
