# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.datamaker import random_person
from kafka import SimpleProducer, KafkaClient, KafkaConsumer


DEBUG = True if __name__ == '__main__' else False

KAFKA_URL = 'localhost:9092'
kafka = KafkaClient(KAFKA_URL)
# bin/kafka-console-consumer.sh --zookeeper localhost:2181 \
#   --topic main-topic --from-beginning
# bin/kafka-console-producer.sh --broker-list localhost:9092 --topic main-topic
producer = SimpleProducer(kafka)
# topics = ['foo', 'bar', 'quux', 'foo.bar', 'foo.bar.*']
topics = ['main-topic']
consumer = KafkaConsumer('main-topic',
                         group_id='my_group',
                         bootstrap_servers=['localhost:9092'])

if DEBUG:
    # http://kafka-python.readthedocs.org/en/latest/usage.html to use kafka
    # See .sh scripts at:
    # http://kafka.apache.org/08/documentation.html#quickstart
    # instance and send/receive messages.
    with Section('Kafka - via kafka-py'):
        # PRODUCER - typically living somewhere else beside the consumer,
        # running in parallel.
        for topic in topics:
            for i in range(10):
                producer.send_messages(topic, '{}'.format(random_person()))
        # Also works with command line message sending:
        # Typing into the console after running the below command will cause the
        # arguments to be sent to the queue, and processed.
        # They will also be visible here when read by the consumer in python.
        # bin/kafka-console-producer.sh --broker-list \
        #   localhost:9092 --topic main-topic

        # CONSUMER
        for message in consumer:
            print("{}:{}:{}: key={} value={}".format(
                message.topic, message.partition,
                message.offset, message.key,
                message.value))
