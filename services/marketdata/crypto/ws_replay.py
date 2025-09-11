import asyncio
import websockets
import json
from kafka import KafkaConsumer
from services.marketdata.crypto.config import Config

async def relay_data(websocket, path):
    consumer = KafkaConsumer(
        Config.MARKETDATA_TOPIC,
        bootstrap_servers=Config.KAFKA_BOOTSTRAP_SERVERS,
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    try:
        for message in consumer:
            data = message.value
            await websocket.send(json.dumps(data))
    except Exception as e:
        print(f"WebSocket relay error: {e}")
    finally:
        consumer.close()

async def main():
    server = await websockets.serve(relay_data, "localhost", 8765)
    print("WebSocket relay running on ws://localhost:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())