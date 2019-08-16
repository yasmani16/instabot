import logging
import os
from datetime import date


def logs():
  currenttime = date.today()
  LOG_FORMAT ="%(levelname)s %(asctime)s - %(message)s"
  logname = "{}.log".format(currenttime)
  subdir = "logging"
  logfile = os.path.join(subdir, logname)
  logging.basicConfig(
      filename= logfile, 
      level = logging.DEBUG,
      format = LOG_FORMAT
    )
  logger=logging.getLogger()
  return logger