import sys
import time


class Logger:
    def __init__(self):
        self.format = '%Y-%b-%d %H:%M:%S -->'
        
    def log(self, message):
        prefix = time.strftime(self.format, time.localtime())
        sys.stderr.write(f"{prefix} {message}\n")


class CustomerLogger(Logger):
    def __init__(self):
        super().__init__()
        self.format = '%Y-%b-%d ::'


logger = Logger()
logger.log('An error has happened!')

c_logger = CustomerLogger()
c_logger.log('Custom logged message!')