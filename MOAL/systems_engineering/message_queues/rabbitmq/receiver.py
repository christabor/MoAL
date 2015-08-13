# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_success
from MOAL.helpers.display import print_error
from MOAL.helpers.display import print_info
from MOAL.helpers.display import print_warning
from MOAL.systems_engineering.message_queues.rabbitmq import start

DEBUG = True if __name__ == '__main__' else False


def on_open(ch, method, properties, body):
    key = method.routing_key
    message = '* Received! {}'.format(body)
    if key == 'info':
        print_info(message)
    if key == 'warning':
        print_warning(message)
    if key == 'error':
        print_error(message)
    if key == 'success':
        print_success(message)

    if not start.USE_EXCHANGE:
        # Specify ACK to prevent failures from disappearing.
        ch.basic_ack(delivery_tag=method.delivery_tag)


if DEBUG:
    with Section('Message Queues - RabbitMQ'):
        queue_name = start.result.method.queue
        for severity in start.SEVERITIES:
            start.channel.queue_bind(
                exchange=start.EXCHANGE_NAME,
                queue=queue_name,
                routing_key=severity)

        start.channel.basic_qos(prefetch_count=1)
        # Setup exchange to mediate messages between consumer/producer.
        start.channel.basic_consume(on_open, queue=queue_name, no_ack=True)
        start.channel.start_consuming()
