import logging.config
import module1
import module2

log_config = {
    'version':1,
    'formatter': {
        'default':{
            'format':'%(asctime)s-%(name)s-%(levelname)s-%(message)'
        }
    },

    'handlers': {
        'file' : {
            'class':'logging.FileHandler',
            'filename':'module_app.log',
            'format':'default',
            'level':'DEBUG'
        },
        'console': {
            'class':'logging.StreamHandler',
            'format':'default',
            'level':'DEBUG'
        }
    },

    'root': {
        'handlers':['file','console'],
        'level':'DEBUG'
    },
}

logging.config.dictconfig(log_config)

if __name__ == '__main__':
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Main module started')
    module_1_function()
    module_2_function()
    logger.info('Main module finished')

   
