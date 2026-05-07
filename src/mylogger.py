import logging
from logging.handlers import TimedRotatingFileHandler as handler

def get_logger(name, log_directory='', log_to_stream=True):
    logger = logging.getLogger(name=name)
    formatter = logging.Formatter("%(asctime)s [%(levelname)8s] %(message)s")
    logger.setLevel(logging.DEBUG)

    if log_directory:
        file_handler = handler(filename='{}/{}.log'.format(log_directory, name),
                               when='midnight', interval=1, encoding='utf-8')
        file_handler.setFormatter(formatter)
        file_handler.suffix = "%Y%m%d%H%M"
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)

    if log_to_stream:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(logging.DEBUG)
        logger.addHandler(stream_handler)

    return logger
