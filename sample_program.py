import json
import logging.config
import trace_log

with open('logging_config.json', 'r') as f:
    LOGGING_CONFIG = json.load(f)

logging.config.dictConfig(LOGGING_CONFIG)

logger = logging.getLogger("my_prog")

# Test the logger with some messages
logger.trace3('This is a trace3 message.')
logger.trace2('This is a trace2 message.')
logger.trace1('This is a trace1 message.')
logger.trace('This is a trace message.')
logger.debug('This is a debug message.')
logger.info('This is an info message.')
logger.warning('This is a warning message.')
logger.error('This is an error message.')
logger.critical('This is a critical message.')
