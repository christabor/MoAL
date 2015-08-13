# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.systems_engineering.message_queues.rabbitmq import start
from random import randrange as rr
from random import choice
import pika
import time

DEBUG = True if __name__ == '__main__' else False


def emit(routing_key='info'):
    count = 0
    # Randomize to mimic "authenticity"
    time.sleep(float(rr(1, 10)) * 0.1)
    start.channel.basic_publish(
        exchange=start.EXCHANGE_NAME,
        routing_key=routing_key,
        body='MOAL Message! #{}'.format(count),
        properties=pika.BasicProperties(delivery_mode=2))
    count += 1


if DEBUG:
    with Section('Message Queues - RabbitMQ'):
        try:
            while True:
                emit(routing_key=choice(
                    ['info', 'warning', 'success', 'error']))
        except KeyboardInterrupt:
            print('Closing connection...')
            start.connection.close()
