import os
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/drive"]

creds = None

if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
              creds.refresh(Request())
    
        else:
              flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
              creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
              token.write(creds.to_json())


try:

    service = build("drive", "v3", credentials=creds)

    folder_target = service.files().list(
         q="name='rebelway_python_2025' and mimeType='application/vnd.google-apps.folder'",
         spaces="drive"
    ).execute()
    
    folder_id = folder_target["files"][0]["id"]
    folder_name = folder_target["files"][0]["name"]
    file =  "test.obj"

    print(folder_target)
    print(folder_id)

    file_metadata = {
        "name": "test",
        "parents": [folder_id]}
    
    media = MediaFileUpload(file)
    upload_file = service.files().create(body=file_metadata,
                                         media_body = media,
                                         fields = "id").execute()
    
    print(f"{file} uploaded to google drive folder {folder_name} succesfully!")

except HttpError as e:
    print("error: " + str(e))
