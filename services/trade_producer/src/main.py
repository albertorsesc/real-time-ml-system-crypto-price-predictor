from typing import Dict, List

from loguru import logger
from quixstreams import Application

from kraken_api import KrakenWebsocketTradeAPI

from src import config

def produce_trades(
    kafka_broker_address: str,
    kafka_topic_name: str,
    product_id: str,
) -> None:
    """
    Reads trades from the Kraken websocket API and saves them into a Kafka Topic.

    Args:
      kafka_broker_address (str): The address of the Kafka broker.
      kafka_topic_name (str): The name of the Kafka Topic.
      product_id (str): The product ID to subscribe to.
    Returns:
      None
    """

    app = Application(broker_address=kafka_broker_address)

    # The Topic where we will save the Trades.
    topic = app.topic(name=kafka_topic_name, value_serializer='json')

    # Create instance of the Kraken API
    kraken_api = KrakenWebsocketTradeAPI(product_id=product_id)

    # Create a Producer instance
    with app.get_producer() as producer:
        while True:
            # Get the trades from the Kraken API
            trades: List[Dict] = kraken_api.get_trades()

            for trade in trades:
                # Serialize a trade using the defined Topic
                message = topic.serialize(key=trade['product_id'], value=trade)

                # Produce a message into the Kafka topic
                producer.produce(topic=topic.name, value=message.value, key=message.key)

                logger.info('Message Sent!')

            from time import sleep

            sleep(1)


if __name__ == '__main__':
    produce_trades(
        kafka_broker_address=config.kafka_broker_address,
        kafka_topic_name=config.kafka_topic_name,
        product_id=config.product_id
    )
