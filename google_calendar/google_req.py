import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class PostToGoogleCalendar:
    def __init__(self):
        self.creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                self.creds = flow.run_local_server()
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

        self.service = build('calendar', 'v3', credentials=self.creds)

    def get_events(self):
        now = datetime.utcnow().isoformat() + 'Z'
        events_result = self.service.events().list(calendarId='primary', timeMin=now,
                                                maxResults=500, singleEvents=True,
                                                orderBy='startTime').execute()
        return events_result.get('items', [])

    def create_event(self, new_event):
        if not self.already_exists(new_event):
            event = self.service.events().insert(calendarId='primary', body=new_event).execute()
            return event.get('htmlLink')
        else:
            return 'Event Already Exists'

    def already_exists(self, new_event):
        events = self.get_date_events(new_event['start']['dateTime'], self.get_events())
        event_list = [new_event['summary'] for new_event in events]
        if new_event['summary'] not in event_list:
            return False
        else:
            return True

    def get_date_events(self, date, events):
        lst = []
        date = date
        for event in events:
            if event.get('start').get('dateTime'):
                d1 = event['start']['dateTime']
                if d1 == date:
                    lst.append(event)
        return lst
