## Real-Time ML System that predicts short-term crypto prices

### Getting Started with the Crypto Trading Project
#### Prerequisites

- Docker and Docker Compose installed
- Poetry (Python package manager)
- Git (for version control)

#### Setup Instructions

1. Start Redpanda (Message Broker)

```bash
# Navigate to docker-compose directory
cd docker-compose

# Start Redpanda containers
docker compose -f redpanda.yaml up -d
```

This will start:

- Redpanda broker (accessible at localhost:19092)
- Redpanda Console (accessible at http://localhost:8080)

2. Start the Trade Producer Service

```bash
# Navigate to the Trade Producer service directory
cd ../services/trade_producer

# Build and run the service
make build
make run
```

#### What to Expect

The Trade Producer service will:

- Connect to Kraken's WebSocket API
- Subscribe to BTC/USD trade data
- Stream real-time trade data to the Redpanda topic named "trade"

You can verify the data flow by:

- Opening Redpanda Console at http://localhost:8080
- Navigating to Topics → trade
- Viewing the incoming messages

#### Project Structure

```
.
├── docker-compose/
│   ├── redpanda.yaml    # Redpanda configuration
│   └── Makefile         # Commands for Redpanda management
│
└── services/
    └── trade_producer/  # Service that produces trade data
        ├── src/
        │   ├── main.py      # Entry point
        │   └── kraken_api.py # Kraken WebSocket client
        ├── Dockerfile    # Container configuration
        ├── pyproject.toml # Python dependencies
        └── Makefile      # Build and run commands
```

#### Troubleshooting

If you encounter the "ModuleNotFoundError: No module named 'src'" error:

- Make sure you have the poetry.lock file in the trade_producer directory
- Verify that both src/__init__.py and tests/__init__.py exist
- Try rebuilding the Docker image with make build before running

#### Next Steps

After setup, you should see log messages indicating:

Successful connection to Kraken WebSocket
Subscription to BTC/USD trade channel
"Message Sent!" logs as trades are published to Redpanda