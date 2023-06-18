import inspect
import logging


class Logs:
    def test_loggingDemo(self):
        logger_name = inspect.stack()[1][3]
        log = logging.getLogger(logger_name)

        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter(" %(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)
        log.addHandler(file_handler)

        log.setLevel(logging.DEBUG)
        return log
