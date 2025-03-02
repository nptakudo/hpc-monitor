from kafka import KafkaConsumer
import json

# Kafka broker configuration
bootstrap_servers = ['gateway.hpcc.vn:29094', 
                    'gateway.hpcc.vn:29095', 
                    'gateway.hpcc.vn:29096']

# Test topic name
topic_name = 'telegraf'

def create_consumer():
    try:
        consumer = KafkaConsumer(
            topic_name,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            # group_id='test_group',
            # value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        return consumer
    except Exception as e:
        print(f"Error creating consumer: {e}")
        return None

def receive_messages():
    consumer = create_consumer()
    if not consumer:
        return

    print("Waiting for messages...")
    try:
        for message in consumer:
            print(f"Received message: {message.value}")
            # Remove the break if you want to keep receiving messages
            # break
    except Exception as e:
        print(f"Error consuming message: {e}")
    finally:
        consumer.close()

if __name__ == "__main__":
    receive_messages()