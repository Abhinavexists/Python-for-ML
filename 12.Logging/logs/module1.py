import logging

def module_1_function():
    logger = logging.getLogger(__name__)
    logger.info('Module A function started')
    logger.debug('This is a debug message from Module A')
    logger.info('Module A function finished')