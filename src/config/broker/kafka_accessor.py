import json

from aiokafka import AIOKafkaConsumer

from src.config.database.accessor import Settings

settings = Settings()


def get_aiokafka_consumer() -> AIOKafkaConsumer:
    return AIOKafkaConsumer(
        settings.PROCESS_SWIPES_TOPIC,
        bootstrap_servers=(settings.KAFKA_SERVER,),
        value_deserializer=lambda message: json.loads(message.decode("utf-8")),
    )
