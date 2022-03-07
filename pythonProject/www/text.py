
import logging
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def log(log_path,log_name):
    logger = logging.getLogger(log_name)
    logger.setLevel(level=logging.DEBUG)
    ch = logging.FileHandler(log_path, encoding='UTF-8')
    ch.setLevel(logging.INFO)
    ch1 = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
    ch.setFormatter(formatter)
    ch1.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(ch1)
    return logger

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
logger = log(log_path="config.ini", log_name="jjj")
logger.debug("debug message")
logger.info("info message")
logger.error("error message")
logger.warning("warning message")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

