from app.utils.request_helper import make_request
from app.utils.log_leads import log_new_leads, log_error_leads

import os

def fetch_data():
    CRM_API_KEY = os.getenv("CRM_API_KEY")
    CRM_API_URL = os.getenv("CRM_API_URL")
    headers = {
        'Content-Type': 'application/json'
    }
    response = make_request(f'{CRM_API_URL}&apiKey={CRM_API_KEY}', headers)
    if response.get("status") == "ok":
        log_new_leads()
    else:
        log_error_leads()
    return response
