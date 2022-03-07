import logging


class Log():
    def __init__(self):
        self.logger = logging.getLogger("mylog")
        self.logger.setLevel(logging.DEBUG)

        hand = logging.FileHandler("log1.txt",encoding="utf-8")
        format = logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")
        hand.setFormatter(format)
        self.logger.addHandler(hand)

    def debug(self, deg_msg):
        self.logger.debug(deg_msg)

    def info(self, info_msg):
        self.logger.info(info_msg)

    def warn(self, warn_msg):
        self.logger.info(warn_msg)

    def error(self, error_msg):
        self.logger.info(error_msg)

