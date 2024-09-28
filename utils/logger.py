# utils/logger.py

import datetime

class Logger:
    def __init__(self, log_file='calculator.log'):
        self.log_file = log_file

    def log_operation(self, operation, a, b, result):
        timestamp = datetime.datetime.now()
        log_entry = f"{timestamp}: {operation} de {a} y {b} = {result}\n"
        with open(self.log_file, 'a') as f:
            f.write(log_entry)