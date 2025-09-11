Fetch real-time data from Binance:  wscat -c wss://stream.binance.com:9443/ws/btcusdt@trade
< {"e":"trade","E":1757522615939,"s":"BTCUSDT","t":5225367649,"p":"113747.89000000","q":"0.00060000","T":1757522615939,"m":true,"M":true}

< {"e":"kline","E":1757523280021,"s":"BTCUSDT","k":{"t":1757523000000,"T":1757523299999,"s":"BTCUSDT","i":"5m","f":5225377132,"L":5225383094,"o":"113647.98000000","c":"113670.12000000","h":"113708.45000000","l":"113627.74000000","v":"46.64096000","n":5963,"x":false,"q":"5302412.42715770","V":"14.72666000","Q":"1674287.91322410","B":"0"}}
< {"e":"kline","E":1757523282016,"s":"BTCUSDT","k":{"t":1757523000000,"T":1757523299999,"s":"BTCUSDT","i":"5m","f":5225377132,"L":5225383151,"o":"113647.98000000","c":"113670.12000000","h":"113708.45000000","l":"113627.74000000","v":"46.76163000","n":6020,"x":false,"q":"5316129.00053810","V":"14.73012000","Q":"1674681.21183930","B":"0"}}

services/
└── marketdata/
    └── crypto/
        ├── sources/                  # Pluggable source implementations
        │   ├── __init__.py
        │   ├── base.py              # Abstract base class for sources
        │   ├── binance.py           # Binance WebSocket source
        │   ├── coinbase.py          # Coinbase WebSocket source
        │   ├── simulator.py         # Simulator source
        │   └── replayer.py          # Replayer for backtests
        ├── publisher.py             # Kafka publisher logic
        ├── schema.py                # Unified schema definition
        ├── config.py                # Configuration (e.g., API keys, Kafka settings)
        ├── main.py                  # Entry point for running the pipeline
        └── tests/                   # Unit and integration tests
            ├── __init__.py
            ├── test_sources.py      # Test source implementations
            └── test_publisher.py    # Test Kafka publishing