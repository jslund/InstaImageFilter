import pika


class RabbitMQCPublisher:

    def __init__(self, rabbitmq_host: str, queue_name: str):
        self.rabbitmq_host = rabbitmq_host
        self.queue_name = queue_name

        self.__connection = pika.BlockingConnection(pika.ConnectionParameters(self.rabbitmq_host))
        self.channel = self.__connection.channel()

        self.channel.queue_declare(self.queue_name)

    def Publish(self, message: str):
        self.channel.basic_publish(exchange='',
                                   routing_key=self.queue_name,
                                   body=message)
