from kafka import KafkaProducer
import json
import time

# Kafka broker configuration
bootstrap_servers = ['gateway.hpcc.vn:29094']
# , 
                    # 'gateway.hpcc.vn:29095', 
                    # 'gateway.hpcc.vn:29096']

# Test topic name
topic_name = 'telegraf'

def create_producer():
    try:
        producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        return producer
    except Exception as e:
        print(f"Error creating producer: {e}")
        return None

def send_message():
    producer = create_producer()
    if not producer:
        return

    # Send test message
    test_message = {"message": "Hello Kafka!", "timestamp": time.time()}
    try:
        producer.send(topic_name, test_message)
        producer.flush()
        print("Message sent successfully")
    except Exception as e:
        print(f"Error sending message: {e}")
    finally:
        producer.close()

if __name__ == "__main__":
    send_message()