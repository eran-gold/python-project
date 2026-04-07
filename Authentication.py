import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# --- Configuration --- #
# Replace 'your-service-account-key.json' with the actual name of your JSON key file
SERVICE_ACCOUNT_KEY_FILE = 'miluim-491118-9c69bad198e4.json'
ORIGINAL_SHEET_URL = 'https://docs.google.com/spreadsheets/d/1Hre8FRvBU7A5g6KVOPEKjMHmEGntmURnURD1cy2Ac0E/edit?gid=0#gid=0'
NEW_SHEET_NAME = 'Copy of My Original Sheet'

# --- Authentication --- #
try:
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_KEY_FILE, scope)
    client = gspread.authorize(creds)
    print("Authentication successful!")
except Exception as e:
    print(f"Authentication failed: {e}")
    print("Please ensure your JSON key file is uploaded and named correctly, and the Google Sheets API is enabled.")