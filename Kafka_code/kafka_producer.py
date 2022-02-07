from kafka import KafkaProducer
import json
import time

def json_serializer(kafka_d):
	return json.dumps(kafka_d).encode("utf-8")

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
						 value_serializer=json_serializer,
						 api_version=(0,10,1))


with open("input_file.json") as f:
	data_object = json.load(f)	
	for odd in data_object['odds']:
		producer.send("test",odd)
		
	producer.close()
		

f.close()
