import os
from dotenv import load_dotenv

load_dotenv()

MONGO_CONFIG = {
    "port": os.getenv("MONGO_PORT"),
    "host": os.getenv("MONGO_HOST"),
    "user": os.getenv("MONGO_USER"),
    "pass": os.getenv("MONGO_PASS"),
    "authSource": os.getenv("MONGO_AUTH"),
}

DEPTH_TRADE_BINANCE_CONFIG = {
    "raw_database": "raw_depth_trade_binance_db",
    "raw_collection": "depth_trade_binance_raw",
    "clean_database": "clean_depth_trade_binance_and_cmc_db",
    "clean_trade_collection": "trade",
    "clean_depth_collection": "depth",
    "clean_cmc_collection": "cmc",
}

COINMARKETCAP_CONFIG = {
    "clean_database": "clean_depth_trade_binance_and_cmc_db",
    "clean_cmc_collection": "cmc",
    "cmc_api": os.getenv("CMC_API"),
    "cmc_interval_send_request": 260,
    "cmc_url": f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=100&convert=USD",
}


TELE_CONFIG = {
    "tele_bot_token": os.getenv("TELE_BOT_TOKEN"),
    "tele_chat_id": os.getenv("TELE_CHAT_ID"),
    "tele_message_parse": "HTML",
    "tele_check_interval_second": 30,
}
