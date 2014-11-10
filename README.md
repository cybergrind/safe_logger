# safe_logger

## Description

This handler is designed to provide correct log files rotation when multiple processes writing to file.

Heavilly tested on production systems with up to 50 writers.

**Caveat**: this logger has been extracted from other system, so can have issues cause by copy-pasting

## Pitfalls

* Naive aproach fails because concurrent processes do independent rollovers and finally you will have zero-lenght log file: so we need locking
* Naive locking fails when you have some processes that not write often and them can rotate you file in case you archive old, or etc.: so we need check file that want to move by compare inodes
* Naive approach to start handler have issues, when you open file that in rollover - you can write data to rotated file: so we need locking on open file

## Usage

```python
import os
import logging
from safe_logger import TimedRotatingFileHandlerSafe

class NullHandler(logging.Handler):
    def emit(self, record):
        pass
    def write(self, *args, **kwargs):
        pass


LOG_FILE = '/tmp/debug.log'
ERR_FILE = '/tmp/error.log'

FORMAT = '[%(asctime)s] [%(levelname)s] [PID: '+str(os.getpid())+'] [%(name)s]:  %(message)s'
FORMATTER = logging.Formatter(FORMAT)


logging.basicConfig(level=logging.DEBUG, stream=NullHandler())
root = logging.root
log_handler = TimedRotatingFileHandlerSafe(LOG_FILE, when='MIDNIGHT')
log_handler.setLevel(logging.DEBUG)
log_handler.setFormatter(FORMATTER)
root.addHandler(log_handler)

err_handler = TimedRotatingFileHandlerSafe(ERR_FILE, when='MIDNIGHT')
err_handler.setLevel(logging.ERROR)
err_handler.setFormatter(FORMATTER)
root.addHandler(err_handler)
```