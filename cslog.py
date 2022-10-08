#%%
import sys
import logging
try:
    from colorlog import ColoredFormatter
except:
    try:
        import pip
        pip.main(["install", 'colorlog', "-q"])
        from colorlog import ColoredFormatter
    except:
        print('Error install colorlog')

SUCCESS = 90
logging.addLevelName(SUCCESS, "SUCCESS")
def success(self, message, *args, **kws):
    # Yes, logger takes its '*args' as 'args'.
    self._log(SUCCESS, message, args, **kws) 
logging.Logger.success = success

class CustomLogger():
    def __init__(self):
        LOG_LEVEL = logging.DEBUG
        LOGFORMAT = "%(log_color)s%(message)s%(reset)s"
        logging.root.setLevel(LOG_LEVEL)
        formatter = ColoredFormatter(LOGFORMAT, log_colors={
            'DEBUG':    'white',
            'INFO':     'cyan',
            'SUCCESS':     'green',
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'red',
        })
        stream = logging.StreamHandler()
        stream.setLevel(LOG_LEVEL)
        stream.setFormatter(formatter)
        logger = logging.getLogger('pythonConfig')
        logger.setLevel(LOG_LEVEL)
        if (logger.hasHandlers()):
            logger.handlers.clear()
        logger.addHandler(stream)
        self.logger = logger
        self.s = logger.success
        self.i = logger.info
        self.w = logger.warning
        self.e = logger.error
        self.d = logger.debug
        self.success = logger.success
        self.info = logger.info
        self.warning = logger.warning
        self.error = logger.error
        self.debug = logger.debug

        
logger = CustomLogger()

# Usage
# from csmodules.cslog import logger
# logger.s("A quirky message only developers care about")

# Example
# logger.d("A quirky message only developers care about")
# logger.debug("A quirky message only developers care about")
# logger.s("A quirky message only developers care about")
# logger.success("A quirky message only developers care about")
# logger.i("Curious users might want to know this")
# logger.info("Curious users might want to know this")
# logger.w("Something is wrong and any user should be informed")
# logger.warning("Something is wrong and any user should be informed")
# logger.e("Serious stuff, this is red for a reason")
# logger.error("Serious stuff, this is red for a reason")

