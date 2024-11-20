import logging
from datetime import datetime

logging.basicConfig(filename='leads.log', level=logging.INFO)

def log_new_leads():
    logging.info(f"Get new leads at {datetime.now()}")
def log_error_leads():
    logging.info(f"Erro to get new leads at {datetime.now()}")
