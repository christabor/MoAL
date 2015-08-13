import pika

USE_EXCHANGE = True
QUEUE_NAME = 'moal_tasks'
EXCHANGE_NAME = 'moal'
EXCHANGE_TYPE = 'direct'
SEVERITIES = ['error', 'warning', 'info', 'success', ]
DEFAULT_SEVERITY = 'info'

tier = 'development'
host = 'localhost' if tier == 'development' else 'SOME_IP'
connection = pika.BlockingConnection(pika.ConnectionParameters(host))
channel = connection.channel()

channel.exchange_declare(exchange=EXCHANGE_NAME, type=EXCHANGE_TYPE)

if USE_EXCHANGE:
    result = channel.queue_declare(queue=QUEUE_NAME, durable=True)
else:
    result = channel.queue_declare(exclusive=True)


def get_routing_key(args):
    return args if len(args) > 1 else DEFAULT_SEVERITY
