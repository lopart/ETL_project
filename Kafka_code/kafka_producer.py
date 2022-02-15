from kafka import KafkaProducer
import json
import time

def json_serializer(kafka_data):
	return json.dumps(kafka_data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
			value_serializer=json_serializer,
			api_version=(1,4,6))

with open("/usr/local/airflow/data/input_file.json") as f:
	data_object = json.load(f)	
	for odd in data_object['odds']:
		producer.send("test",odd)
		
	producer.close()
		

f.close()
