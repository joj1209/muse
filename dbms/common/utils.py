import logging

def getLogger(logger_name):
    logger = logging.getLogger(logger_name)
    print('---1.logger start')

    if len(logger.handlers) > 0:
        return logger

    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(levelname)s|%(name)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')

    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    logger.addHandler(streamHandler)
    print('---2.logger start')
    file_handler = logging.FileHandler('output.log')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger