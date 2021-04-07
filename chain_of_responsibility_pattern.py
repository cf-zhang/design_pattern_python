class AbstractLogger:
    INFO = 1
    DEBUG = 2
    ERROR = 3

    def __init__(self):
        self.next_logger = None
        self.lever = 0

    def set_next_logger(self, next_logger: 'AbstractLogger'):
        self.next_logger = next_logger

    def log_message(self, level: 'int', message: 'str'):
        if self.lever <= level:
            self.write(message)
        if self.next_logger is not None:
            self.next_logger.log_message(level, message)

    def write(self, message: 'str'):
        pass


class ConsoleLogger(AbstractLogger):
    def __init__(self, level: 'int'):
        AbstractLogger.__init__(self)
        self.lever = level

    def write(self, message: 'str'):
        print("standard console::logger: " + message)


class ErrorLogger(AbstractLogger):
    def __init__(self, level: 'int'):
        AbstractLogger.__init__(self)
        self.lever = level

    def write(self, message: 'str'):
        print("error console::logger: " + message)


class FileLogger(AbstractLogger):
    def __init__(self, level: 'int'):
        AbstractLogger.__init__(self)
        self.lever = level

    def write(self, message: 'str'):
        print("file console::logger: " + message)


error_logger = ErrorLogger(AbstractLogger.ERROR)
file_logger = FileLogger(AbstractLogger.DEBUG)
console_logger = ConsoleLogger(AbstractLogger.INFO)
error_logger.set_next_logger(file_logger)
file_logger.set_next_logger(console_logger)

error_logger.log_message(AbstractLogger.INFO, "this is an information.")
error_logger.log_message(AbstractLogger.DEBUG, "this is an debug information.")
error_logger.log_message(AbstractLogger.ERROR, "this is an error information.")


