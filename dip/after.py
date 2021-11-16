import sys
import time


class TerminalPrinter:
    def write(self, msg):
        sys.stderr.write(f"{msg}\n")


class FilePrinter:
    def write(self, msg):
        with open('log.txt', 'a+', encoding='UTF8') as f:
            f.write(f"{msg}\n")


class Logger:
    def __init__(self):
        self.format = '%Y-%b-%d %H:%M:%S'


    def log(self, message, notifier):
        prefix = time.strftime(self.format, time.localtime())
        notifier().write(f"{prefix} {message}")


logger = Logger()
logger.log("Starting the program...", TerminalPrinter)
logger.log("An error!", FilePrinter)