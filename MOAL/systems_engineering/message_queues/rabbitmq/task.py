# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.systems_engineering.message_queues.rabbitmq import start
import pika
import sys

DEBUG = True if __name__ == '__main__' else False


if DEBUG:
    with Section('Message Queues - RabbitMQ'):
        message = ' '.join(sys.argv[1:]) or '-- UNNAMED NEW TASK --'
        start.chan.basic_publish(
            exchange=start.EXCHANGE_NAME,
            routing_key=start.get_routing_key(sys.argv),
            body=message,
            properties=pika.BasicProperties(delivery_mode=2))
        print('Sent new task: {}'.format(message))
        start.connection.close()
