# Copyright (c) 2023 Dylan Reinhold
# MIT License

import logging
import logging.config

TRACE_LEVEL_NUM = 5
TRACE1_LEVEL_NUM = 4
TRACE2_LEVEL_NUM = 3
TRACE3_LEVEL_NUM = 2

logging.addLevelName(TRACE_LEVEL_NUM, "TRACE")
logging.addLevelName(TRACE1_LEVEL_NUM, "TRACE1")
logging.addLevelName(TRACE2_LEVEL_NUM, "TRACE2")
logging.addLevelName(TRACE3_LEVEL_NUM, "TRACE3")

def trace(self, message, *args, **kws):
    if self.getEffectiveLevel() <= TRACE_LEVEL_NUM:
        self._log(TRACE_LEVEL_NUM, message, args, **kws)

def trace1(self, message, *args, **kws):
    if self.getEffectiveLevel() <= TRACE1_LEVEL_NUM:
        self._log(TRACE1_LEVEL_NUM, message, args, **kws)

def trace2(self, message, *args, **kws):
    if self.getEffectiveLevel() <= TRACE2_LEVEL_NUM:
        self._log(TRACE2_LEVEL_NUM, message, args, **kws)

def trace3(self, message, *args, **kws):
    if self.getEffectiveLevel() <= TRACE3_LEVEL_NUM:
        self._log(TRACE3_LEVEL_NUM, message, args, **kws)


logging.Logger.trace = trace
logging.Logger.trace1 = trace1
logging.Logger.trace2 = trace2
logging.Logger.trace3 = trace3

