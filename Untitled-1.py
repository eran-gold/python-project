import gspread
from oauth2client.service_account import ServiceAccountCredentials
import traceback
import pandas as pd

# --- Configuration --- #
SERVICE_ACCOUNT_KEY_FILE = "miluim-491118-9c69bad198e4.json"

ORIGINAL_SHEET_URL = "https://docs.google.com/spreadsheets/d/1Hre8FRvBU7A5g6KVOPEKjMHmEGntmURnURD1cy2Ac0E"
NEW_SHEET_NAME = "Copy of My Original Sheet"

# --- Authentication --- #
try:
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        SERVICE_ACCOUNT_KEY_FILE, scope
    )

    client = gspread.authorize(creds)
    print("Authentication successful!")

except Exception as e:
    client = None
    print(f"Authentication failed: {e}")
    print("Make sure the JSON key file exists and the service account has access.")
    

# --- Copying the Spreadsheet --- #

if client:
    try:
        # Open the original spreadsheet using its URL
        original_spreadsheet = client.open_by_url(ORIGINAL_SHEET_URL)
        print(f"Opened original spreadsheet: {original_spreadsheet.title}")
        
        # Create a copy of the spreadsheet
        copied_spreadsheet = client.copy(
            original_spreadsheet.id, 
            title=NEW_SHEET_NAME,
            copy_permissions=True
        )

        print(f"\nSuccessfully copied the spreadsheet!")
        print(f"New sheet title: {copied_spreadsheet.title}")
        print(f"New sheet URL: https://docs.google.com/spreadsheets/d/{copied_spreadsheet['id']}\n")

        # Optional: Verify content
        # worksheet = copied_spreadsheet.sheet1
        # data = worksheet.get_all_values()
        # df = pd.DataFrame(data[1:], columns=data[0])
        # print(df.head())

    except gspread.exceptions.SpreadsheetNotFound as e:
        print(f"Error: Original spreadsheet not found or access denied. Details: {e}")
        print("Ensure the service account email has EDITOR access to the sheet.")

    except Exception as e:
        print(f"Unexpected error: {e}")
        traceback.print_exc()

else:
    print("Cannot proceed with copying the spreadsheet. Authentication was not successful.")