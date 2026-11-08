import logging
import sys
import os


class Logger:

    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)5s - %(message)s",
        encoding="UTF-8",
        handlers=[
            logging.FileHandler("logs/app.log", encoding="utf-8"),  # ذخیره در فایل
            logging.StreamHandler(sys.stdout)
        ]
    )

    @staticmethod
    def info(message):
        logging.info(message)

    @staticmethod
    def error(message):
        logging.error(message)

    @staticmethod
    def debug(message):
        logging.debug(message)