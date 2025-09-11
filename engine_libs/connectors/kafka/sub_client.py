from kafka import KafkaConsumer
import json
consumer = KafkaConsumer("streams.marketdata", bootstrap_servers="localhost:9092")
for msg in consumer:
    print(json.loads(msg.value))