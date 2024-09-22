from logger import logging

def add(a,b):
    logging.debug('The addition operation ins taking place')
    return a+b
logging.debug('addition function is called')
add(10,15)