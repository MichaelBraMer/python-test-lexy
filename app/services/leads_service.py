from app.utils.request_helper import make_request
import os

def fetch_data():
    CRM_API_KEY = os.getenv("CRM_API_KEY")
    CRM_API_URL = os.getenv("CRM_API_URL")
    headers = {
        'Content-Type': 'application/json'
    }
    response = make_request(f'{CRM_API_URL}&apiKey={CRM_API_KEY}', headers)
    return response
