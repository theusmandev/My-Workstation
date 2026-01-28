# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request  # Import added
# import csv
# import os
# import pickle

# # Google Drive API scopes
# SCOPES = ['https://www.googleapis.com/auth/drive']

# def authenticate():
#     """
#     Authenticate and return a Google Drive service object.
#     """
#     creds = None
#     # Check if token.pickle exists
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)
#     # If no valid credentials are available, log in
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())  # Use Request here
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 r"D:\\UNB\\New folder\\Urdu Novel Bank\\Programs\\credentials.json", SCOPES
#             )
#             creds = flow.run_local_server(port=8080)
#         # Save the credentials for the next run
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)
#     return build('drive', 'v3', credentials=creds)

# def list_pdfs_and_export_to_csv(service):
#     """
#     List all PDF files in Google Drive and export their titles and share links to a CSV file.
#     """
#     print("Fetching PDF files from Google Drive...")
#     results = service.files().list(
#         q="mimeType='application/pdf'",
#         pageSize=1000,  # Adjust page size as needed
#         fields="nextPageToken, files(id, name, webViewLink)"
#     ).execute()

#     items = results.get('files', [])

#     if not items:
#         print("No PDF files found.")
#         return

#     # Export details to a CSV file
#     output_file = 'pdf_files.csv'
#     with open(output_file, mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Title', 'Share Link'])  # Header row
#         for item in items:
#             writer.writerow([item['name'], f"https://drive.google.com/file/d/{item['id']}/view"])

#     print(f"PDF details exported to '{output_file}' successfully.")

# def main():
#     """
#     Main function to authenticate and fetch PDF details.
#     """
#     service = authenticate()
#     print("Service authenticated successfully.")
#     list_pdfs_and_export_to_csv(service)

# if __name__ == '__main__':
#     main()


from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import csv
import os
import pickle

# Google Drive API scopes
SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate():
    """
    Authenticate and return a Google Drive service object.
    """
    creds = None
    # Check if token.pickle exists
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If no valid credentials are available, log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())  # Use Request here
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                r"D:\\UNB\\New folder\\Urdu Novel Bank\\Programs\\credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=8080)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('drive', 'v3', credentials=creds)

def list_pdfs_and_export_to_csv(service):
    """
    List all PDF files in Google Drive and export their titles and share links to a CSV file.
    """
    print("Fetching PDF files from Google Drive...")
    results = service.files().list(
        q="mimeType='application/pdf'",
        pageSize=1000,  # Adjust page size as needed
        fields="nextPageToken, files(id, name, webViewLink)"
    ).execute()

    items = results.get('files', [])

    if not items:
        print("No PDF files found.")
        return

    # Specify the output file path (update this path as needed)
    output_file = r'C:\Users\Latitude\Downloads\pdf_files.csv'

    # Export details to a CSV file
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Share Link'])  # Header row
        for item in items:
            writer.writerow([item['name'], f"https://drive.google.com/file/d/{item['id']}/view"])

    print(f"PDF details exported to '{output_file}' successfully.")

def main():
    """
    Main function to authenticate and fetch PDF details.
    """
    service = authenticate()
    print("Service authenticated successfully.")
    list_pdfs_and_export_to_csv(service)

if __name__ == '__main__':
    main()
