import json
from config.logger_config import LoggerConfig
from config.variable_config import DEPTH_TRADE_BINANCE_CONFIG


class DepthTradeBinanceExtract:
    def __init__(self):
        try:
            self.logger = LoggerConfig(
                "Extract depth - trade from top 100 coin in Binance"
            )
            with open(
                "/home/duc/symbol_flow_big_data/data/processed/top100_symbol.json", "r"
            ) as f:

                self.symbol_list = json.load(f)
            self.depth_trade_binance_url = DEPTH_TRADE_BINANCE_CONFIG[
                "depth_trade_binance_url"
            ]
            for symbol in self.symbol_list[:20]:
                self.top_20symbol = self.depth_trade_binance_url + f"{symbol}@trade"

        except Exception as e:
            pass
