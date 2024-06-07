from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json
import os

app = Flask(__name__)

KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'kafka:9092')
producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

@app.route('/produce', methods=['POST'])
def produce():
    data = request.json
    producer.send('my_topic', value=data)
    producer.flush()
    return jsonify({'status': 'Message sent to Kafka'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
