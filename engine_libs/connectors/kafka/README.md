Run the Kafka broker:
docker run -p 9092:9092 confluentinc/cp-kafka

Create a topic:
kafka-topics --create --topic streams.marketdata --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1