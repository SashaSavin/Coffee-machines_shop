import logging
import time

date = time.asctime()

def logg_this(mess_to_log):
    logging.basicConfig(filename="logs/logs - " + str(date) + ".log", level=logging.INFO, filemode='w')
    logging.info(mess_to_log)