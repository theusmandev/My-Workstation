import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# AdSense Read-only permission
SCOPES = ['https://www.googleapis.com/auth/adsense.readonly']

def get_adsense_data():
    # 1. Authentication
    flow = InstalledAppFlow.from_client_secrets_file(r"E:\Private My-Worksataion\client_secret_73833788169-0918a7furunskkr6caiillra3mntcq1l.apps.googleusercontent.com.json", SCOPES)
    creds = flow.run_local_server(port=0)
    service = build('adsense', 'v2', credentials=creds)

    # 2. Get Account ID
    accounts = service.accounts().list().execute()
    account_id = accounts['accounts'][0]['name']

    # 3. Get Today's Earnings
    report = service.accounts().reports().generate(
        account=account_id,
        dateRange='TODAY',
        metrics=['ESTIMATED_EARNINGS', 'PAGE_VIEWS', 'IMPRESSIONS'],
    ).execute()

    print(f"Today's Estimated Earnings: {report['rows'][0]['cells'][0]['value']}")

if __name__ == '__main__':
    get_adsense_data()