from __future__ import print_function
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def make_event(summary, location, description, startDateTime, endDateTime, recurrence, attendees):
    """
    All the input is string, except attendees, which is a list of stings and
    recurrence, which is a dictionary of string(keys) and string(details).

    The keys for recurrence are: FREQ: "DAILY" / "WEEKLY" / "MONTHLY"
    COUNT: number in string
    interval: number in String
    Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    # Refer to the Python quickstart on how to setup the environment:
    # https://developers.google.com/google-apps/calendar/quickstart/python
    # Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
    # stored credentials.
    """ This is an example of the API use.
    event = {
      'summary': 'Google I/O 2015',
      'location': '800 Howard St., San Francisco, CA 94103',
      'description': 'A chance to hear more about Google\'s developer products.',
      'start': {
        'dateTime': '2016-09-28T09:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
      },
      'end': {
        'dateTime': '2016-09-28T17:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
      },
      'recurrence': [
        'RRULE:FREQ=DAILY;COUNT=2; INTERVAL=2' //repeated twice every alternate day.
      ],
      'attendees': [
        {'email': 'lpage@example.com'},
        {'email': 'sbrin@example.com'},
      ],
      'reminders': {
        'useDefault': False,
        'overrides': [
          {'method': 'email', 'minutes': 24 * 60},
          {'method': 'popup', 'minutes': 10},
        ],
      },
    }
    """
    invitations = []
    for i in attendees:
        invitations.append({'email' : i})

    repeat = "RRULE:"
    if "FREQ" in recurrence.keys():
        repeat += "FREQ=" +recurrence["FREQ"] + ';'
    if "COUNT" in recurrence.keys():
        repeat += "COUNT=" + '='+ recurrence["COUNT"] + ';'
    if "INTERVAL" in recurrence.keys():
        repeat += "INTERVAL=" + recurrence["INTERVAL"] + ';'
    event = {
      'summary': summary,
      'location': location,
      'description': description,
      'start': {
        'dateTime': startDateTime,
        'timeZone': 'America/Los_Angeles',
      },
      'end': {
        'dateTime': endDateTime,
        'timeZone': 'America/Los_Angeles',
      },

      'attendees': invitations,
      'reminders': {
        'useDefault': False,
        'overrides': [
          {'method': 'email', 'minutes': 24 * 60},
          {'method': 'popup', 'minutes': 10},
        ],
      },
    }
    if len(repeat) != 6:
        print("kavi")
        event.update({'recurrence':[
          repeat
        ]})
    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))

make_event("test", "test", "test", "2018-03-08T18:00:00-08:00", "2018-03-08T19:00:00-08:00", {"FREQ": "DAILY"}, ["kavid.vaidya@berkeley.edu"])
