import requests
import sys
import time
import os
import json

BASE_URL = "http://localhost:8000/api"

def upload_file(file_path):
    print(f"Uploading {file_path}...")
    url = f"{BASE_URL}/validationrequest/"
    
    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            # We might need to send 'channel': 'API' if required, but it defaults or is optional
            data = {'channel': 'API', 'file_name': os.path.basename(file_path)} 
            response = requests.post(url, files=files, data=data, auth=('admin', 'admin'))
            
        if response.status_code == 201 or response.status_code == 200:
            return response.json()
        else:
            print(f"Error uploading file: {response.status_code}")
            print(response.text)
            sys.exit(1)
    except Exception as e:
        print(f"Exception: {e}")
        sys.exit(1)

def check_status(request_id):
    url = f"{BASE_URL}/validationrequest/{request_id}/"
    response = requests.get(url, auth=('admin', 'admin'))
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error checking status: {response.status_code}")
        return None

def get_outcomes(request_id):
    url = f"{BASE_URL}/validationoutcome/?request_public_id={request_id}"
    response = requests.get(url, auth=('admin', 'admin'))
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error getting outcomes: {response.status_code}")
        return []

def main():
    if len(sys.argv) < 2:
        print("Usage: python custom_client.py <path_to_ifc_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)

    # 1. Upload
    req_data = upload_file(file_path)
    request_id = req_data.get('public_id')
    print(f"Validation Request ID: {request_id}")
    print(f"Initial Status: {req_data.get('status')}")

    # 2. Poll for completion
    while True:
        status_data = check_status(request_id)
        status = status_data.get('status')
        print(f"Current Status: {status}")
        
        if status in ['COMPLETED', 'FAILED']:
            break
        
        time.sleep(2)

    # 3. Get Results
    print("\nValidation Completed!")
    print("Fetching results...")
    outcomes = get_outcomes(request_id)
    
    print(f"\nFound {len(outcomes)} outcomes:")
    for outcome in outcomes:
        code = outcome.get('outcome_code')
        severity = outcome.get('severity')
        feature = outcome.get('feature')
        print(f" - [{code}] Severity: {severity} (Feature: {feature})")

    if not outcomes:
        print("No issues found (or no outcomes recorded).")

if __name__ == "__main__":
    main()
