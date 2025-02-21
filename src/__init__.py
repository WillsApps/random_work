import logging
from logging import INFO
from sys import stdout

logger = logging.getLogger(__name__)
logger.setLevel(INFO)

# output message format
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# add a stream handler to print logs to console
stream_handler = logging.StreamHandler(stdout)
stream_handler.setFormatter(formatter)

# add the stream handler to logger
logger.addHandler(stream_handler)
