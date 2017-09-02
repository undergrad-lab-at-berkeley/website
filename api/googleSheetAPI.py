
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import os.path

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'ULAB website'


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
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
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

def retrieveSpreadsheetData(spreadsheetId, rangeName):
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        return values

def convertToDictionaryFormat(values):
    """
        Hardcoding the Google sheet format into a format necessary for Flask.

        It filters to only active members.
    """
    result_dict = dict()
    for sheetRow in values:
        if len(sheetRow) != 13:
            continue
        membershipStatus = sheetRow[12]
        if membershipStatus.lower() == 'active':
            firstName = sheetRow[2]
            lastName = sheetRow[3]
            # profileImage = sheetRow[5]
            profileImage = convertImageURL(firstName, lastName)
            print(profileImage)
            personalWebsiteLink = sheetRow[9]
            gitHubLink = sheetRow[7]
            linkedinProfileLink = sheetRow[8]
            biography = sheetRow[6]

            fullName = "{} {}".format(firstName, lastName)
            result_dict[fullName] = dict(img=profileImage,
                                        personal=personalWebsiteLink,
                                        github=gitHubLink,
                                        linkedin=linkedinProfileLink,
                                        bio=biography)
    return result_dict

def convertImageURL(firstName, lastName):
    imageFileAddr = "img/team/{} {}.jpg".format(firstName.lower(), lastName.lower())
    imageFileAddr = imageFileAddr.replace(" ", "_")
    return imageFileAddr

if __name__ == '__main__':
    values = retrieveSpreadsheetData("1GzJxD0LLVln3bZFbTJAgJZ-XkRHv-QRZ7AUUTk7_0Xg", 'A2:M')
    print(convertToDictionaryFormat(values))
    for row in values:
        print("{} \n".format(len(row)))
