from kafka import KafkaProducer
import json
from .config import Config

class MarketDataPublisher:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=Config.KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        self.topic = Config.MARKETDATA_TOPIC

    def publish(self, data_list):
        for item in data_list:
            self.producer.send(self.topic, item)
        self.producer.flush()