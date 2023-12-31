import json
import os
 
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
 
 
API_KEY = 'AIzaSyByS5JL2bTmI9UtpnXLoLRDARDAfah7Zrg'
 
APP_TOKEN_FILE = "/Users/ajzanylsabdanbekova/Desktop/python/api/youtube/client_secrets.json"
USER_TOKEN_FILE = "user_token.json"
 
# https://developers.google.com/identity/protocols/oauth2/scopes#youtube
SCOPES = [
    'https://www.googleapis.com/auth/youtube.force-ssl',
    'https://www.googleapis.com/auth/userinfo.profile',
    'https://www.googleapis.com/auth/youtube.upload',
    'https://www.googleapis.com/auth/userinfo.email'
]
 

def get_creds_cons():
    flow = InstalledAppFlow.from_client_secrets_file(APP_TOKEN_FILE, SCOPES)
    return flow.run_console()
 

def get_creds_saved():
    # https://developers.google.com/docs/api/quickstart/python
    creds = None
 
    if os.path.exists(APP_TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(APP_TOKEN_FILE, SCOPES)
 
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
 
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(APP_TOKEN_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
 
        with open(USER_TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
 
    return creds
 
 
'''
Get YouTube API service w API Key only
'''
def get_service():
    #creds = get_creds_cons()
    creds = get_creds_saved()
    service = build('oauth2', 'v2', credentials=creds)
    return service
 
 
'''
Get User Info 
'''
def get_user_info(channel_id = 'UCf6kozNejHoQuFhBDB8cfxA'):
    r = get_service().userinfo().get().execute()
    print(json.dumps(r))
 
if __name__ == '__main__':
    print("** Hola Hey, Azzrael_YT subs!!!\n")
    get_user_info()