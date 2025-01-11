import json
from typing import List, Dict
from websocket import create_connection
from loguru import logger

class KrakenWebsocketTradeAPI:
  URL = 'wss://ws.kraken.com/v2'

  def __init__(self, product_id: str):
    self.product_id = product_id

    self._ws = create_connection(self.URL)
    logger.info("Connection Established")

    # Subscribe to the trades for the given `product_id`
    self._subscribe(product_id)

  def _subscribe(self, product_id: str):
      """
      Establish connection to the Kraken websocket API and subscribe to the trades for the given `product_id`
      """

      logger.info(f"Subscribing to trades for {product_id}")
      # Subscribe to the trades for the given `product_id`
      message = {
        "method": "subscribe",
        "params": {
          "channel": "trade",
          "symbol": [
            product_id,
          ],
          "snapshot": False
        }
      }

      self._ws.send(json.dumps(message))

      logger.info("Subscription worked!")

      # Discarding the first 2 messages we got from the websocket, because
      # they contain no trade data, only confirmation from Kraken that the subscription was successful.
      _ = self._ws.recv()
      _ = self._ws.recv()

  def get_trades(self) -> List[Dict]:
    # mock_trades = [
    #   {
    #     'product_id': 'BTC-USD',
    #     'price': 60000,
    #     'volume': 0.01,
    #     'timestamp': 1630000000
    #   },
    #   {
    #     'product_id': 'BTC-USD',
    #     'price': 59000,
    #     'volume': 0.01,
    #     'timestamp': 1640000000
    #   },
    # ]

    message = self._ws.recv()

    if 'heartbeat' in message:
      # when we get a heartbeat, i return empty list.
      return []

    # parse message string as a dictionary
    message = json.loads(message)
    logger.info('Message received: ', message)

    trades = []
    for trade in message['data']:
      trades.append({
        'product_id': self.product_id,
        'price': trade['price'],
        'volume': trade['qty'],
        'timestamp': trade['timestamp'],
      })

    return trades