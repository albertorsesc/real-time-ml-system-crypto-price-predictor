from typing import List, Dict

class KrakenWebsocketTradeAPI:
  def __init__(self):
    pass

  def get_trades(self) -> List[Dict]:
    mock_trades = [
      {
        'product_id': 'BTC-USD',
        'price': 60000,
        'volume': 0.01,
        'timestamp': 1630000000
      },
      {
        'product_id': 'BTC-USD',
        'price': 59000,
        'volume': 0.01,
        'timestamp': 1640000000
      },
    ]

    return mock_trades