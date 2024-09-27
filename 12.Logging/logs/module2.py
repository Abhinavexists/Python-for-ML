import logging

def module_2_function():
    logger = logging.getLogger(__name__)
    logger.info('Module B function started')
    logger.debug('This is a debug message from Module B')
    logger.info('Module B function finished')