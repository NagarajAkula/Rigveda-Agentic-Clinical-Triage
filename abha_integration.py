# ABHA Integration for ABDM Compliance

# This script handles ABHA authentication and ensures compliance with the Ayushman Bharat Digital Mission (ABDM) standards for patient identification.

import requests
import json

class ABHAAuthentication:
    def __init__(self, abha_id: str, secret: str):
        self.abha_id = abha_id
        self.secret = secret
        self.token = None

    def authenticate(self):
        # API endpoint for ABHA authentication
        url = 'https://api.abdm.gov.in/authenticate'
        payload = {
            'abhaId': self.abha_id,
            'secret': self.secret
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            self.token = response.json().get('token')
            print("Authentication successful!")
        else:
            print(f"Authentication failed: {response.text}")
            raise Exception('Authentication failed')

    def get_patient_info(self, patient_abha_id: str):
        if not self.token:
            raise Exception('Authentication required')
        # API endpoint for fetching patient information
        url = f'https://api.abdm.gov.in/patient/{patient_abha_id}'
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch patient info: {response.text}")
            raise Exception('Failed to fetch patient info')

# Sample usage:

if __name__ == '__main__':
    # Replace with actual ABHA ID and secret
    abha_auth = ABHAAuthentication('your_abha_id', 'your_secret')
    try:
        abha_auth.authenticate()
        patient_info = abha_auth.get_patient_info('patient_abha_id')
        print(patient_info)
    except Exception as e:
        print(e)
