import sys
import os

from Helpers.RabbitMQConsumer import RabbitMQConsumer

def main():
    rabbitmq_host = 'host.docker.internal'
    consumer_queue_name = 'instagram_pictures'

    rabbitmq_consumer = RabbitMQConsumer(rabbitmq_host, queue_name=consumer_queue_name)
    rabbitmq_consumer.Consume()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)