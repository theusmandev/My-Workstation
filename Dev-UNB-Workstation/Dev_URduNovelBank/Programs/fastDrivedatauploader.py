import os
import time
import json
import pickle
import threading
import queue
import requests
import tkinter as tk
from tkinter import filedialog, messagebox
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from pathlib import Path
import urllib3.exceptions
from requests.exceptions import ConnectionError

# Configuration
UPLOAD_QUEUE_DIR = "upload_queue"
CREDENTIALS_FILE = r"E:\UNB\Programs\credentials.json.json"
TOKEN_FILE = "token.pickle"
CHUNK_SIZE = 256 * 1024 * 1024  # 256 MB
SCOPES = ["https://www.googleapis.com/auth/drive.file"]

class GoogleDriveUploader:
    def __init__(self):
        self.service = self.authenticate()
        self.upload_queue = queue.Queue()
        self.is_uploading = False
        self.root = tk.Tk()
        self.root.title("Google Drive Uploader")
        self.root.geometry("600x400")
        self.setup_gui()
        self.check_internet_thread = threading.Thread(target=self.monitor_internet, daemon=True)
        self.check_internet_thread.start()

    def authenticate(self):
        """Authenticate with Google Drive API using OAuth2."""
        creds = None
        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE, "rb") as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
                creds = flow.run_local_server(port=0)
            with open(TOKEN_FILE, "wb") as token:
                pickle.dump(creds, token)
        return build("drive", "v3", credentials=creds)

    def check_internet(self):
        """Check internet connectivity."""
        try:
            requests.get("https://www.google.com", timeout=5)
            return True
        except (ConnectionError, urllib3.exceptions.NewConnectionError):
            return False

    def monitor_internet(self):
        """Monitor internet connectivity and process upload queue when online."""
        while True:
            if self.check_internet() and not self.is_uploading:
                self.process_upload_queue()
            time.sleep(10)  # Check every 10 seconds

    def add_to_queue(self, file_path):
        """Add file to upload queue and save to local queue directory."""
        Path(UPLOAD_QUEUE_DIR).mkdir(exist_ok=True)
        queued_path = os.path.join(UPLOAD_QUEUE_DIR, os.path.basename(file_path))
        if not os.path.exists(queued_path):
            os.rename(file_path, queued_path)
        self.upload_queue.put(queued_path)
        self.log(f"Added {file_path} to upload queue")
        if self.check_internet() and not self.is_uploading:
            self.process_upload_queue()

    def upload_file(self, file_path):
        """Upload a file to Google Drive with resumable upload."""
        self.is_uploading = True
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        self.log(f"Starting upload of {file_name} ({file_size / (1024**3):.2f} GB)")

        media = MediaFileUpload(
            file_path,
            mimetype="application/octet-stream",
            chunksize=CHUNK_SIZE,
            resumable=True
        )
        file_metadata = {"name": file_name}
        request = self.service.files().create(
            body=file_metadata,
            media_body=media,
            fields="id"
        )

        response = None
        uploaded_bytes = 0
        while response is None:
            try:
                status, response = request.next_chunk()
                if status:
                    progress = (status.resumable_progress / file_size) * 100
                    self.log(f"Uploading {file_name}: {progress:.2f}%")
                    self.progress_label.config(text=f"Uploading {file_name}: {progress:.2f}%")
                    self.root.update()
                if response:
                    self.log(f"Upload of {file_name} completed. File ID: {response['id']}")
                    os.remove(file_path)  # Delete local file after successful upload
            except Exception as e:
                self.log(f"Error uploading {file_name}: {e}")
                self.is_uploading = False
                return False
        self.is_uploading = False
        return True

    def process_upload_queue(self):
        """Process files in the upload queue."""
        while not self.upload_queue.empty():
            file_path = self.upload_queue.get()
            if os.path.exists(file_path):
                if self.upload_file(file_path):
                    self.upload_queue.task_done()
                else:
                    self.upload_queue.put(file_path)  # Re-queue on failure
                    break
            else:
                self.log(f"File {file_path} not found, skipping")
                self.upload_queue.task_done()

    def setup_gui(self):
        """Set up the Tkinter GUI."""
        self.log_text = tk.Text(self.root, height=15, width=60)
        self.log_text.pack(pady=10)
        self.progress_label = tk.Label(self.root, text="No upload in progress")
        self.progress_label.pack(pady=5)
        select_button = tk.Button(self.root, text="Select Files to Upload", command=self.select_files)
        select_button.pack(pady=5)
        self.log("Google Drive Uploader started")

    def log(self, message):
        """Log messages to the GUI text area."""
        self.log_text.insert(tk.END, f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
        self.log_text.see(tk.END)

    def select_files(self):
        """Open file dialog to select files for upload."""
        files = filedialog.askopenfilenames()
        for file in files:
            self.add_to_queue(file)

    def run(self):
        """Start the Tkinter main loop."""
        self.root.mainloop()

if __name__ == "__main__":
    uploader = GoogleDriveUploader()
    uploader.run()