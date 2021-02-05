import pika


class RabbitMQConsumer:

    def callback(self, ch, method, properties, body):
        print("Consumed " + str(body))
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def __init__(self, rabbitmq_host: str, queue_name: str):
        self.rabbitmq_host = rabbitmq_host
        self.queue_name = queue_name

        self.__connection = pika.BlockingConnection(pika.ConnectionParameters(self.rabbitmq_host))
        self.__channel = self.__connection.channel()

        self.__channel.queue_declare(self.queue_name)
        self.__prefetch_count = 1

    def Consume(self):
        self.__channel.basic_consume(queue=self.queue_name,
                                     on_message_callback=self.callback)
        self.__channel.basic_qos(prefetch_count=self.__prefetch_count)

        self.__channel.start_consuming()
