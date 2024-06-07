const kafka = require('kafka-node');
const Consumer = kafka.Consumer;
const client = new kafka.KafkaClient({kafkaHost: 'kafka:9092'});
const consumer = new Consumer(
    client,
    [{ topic: 'my_topic', partition: 0 }],
    {
        autoCommit: true
    }
);

consumer.on('message', function (message) {
    console.log('Received message:', message.value);
});

consumer.on('error', function (err) {
    console.error('Error:', err);
});
