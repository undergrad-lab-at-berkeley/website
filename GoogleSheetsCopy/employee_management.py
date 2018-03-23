from __future__ import print_function
import httplib2
import os
#from Drive import drive

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

# try:
#     import argparse
#     flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
# except ImportError:
#     flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'
ROSTER = 'ULAB_ROSTER'
ROOT_GROUP = 'ulab'

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

def main():
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
    return service

def get_sheets(service):
    sheet_metadata = service.spreadsheets().get(spreadsheetId=spreadsheet_Id).execute()
    sheets = sheet_metadata.get('sheets', '')
    return sheets

spreadsheet_Id = '1k5OgXFL_o99gbgqD_MJt6LuggL4KRGBI27SIW45-FgQ'
service = main()
sheets = get_sheets(service)

def groups(SID):
    sortedgroups = []
    mainroster = sheets[0].get("properties", {}).get("title", "mainroster") # Assumes mainroster is 1st sheet
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_Id, range=mainroster).execute()
    values = result.get('values', [])
    try:
        SIDindex = values[0].index("SID")
        num_rows = len(values)
        for row_index in range(1, num_rows):
            if str(SID) == values[row_index][SIDindex]:
                SIDrow = row_index
                break
        # Later revision: iterate through top row until first instance starting with 'ulab' and use that index for group start instead
        groupIndexStart =  group_start_index()
        for group_index in range(groupIndexStart, len(values[SIDrow])):
            cell = values[SIDrow][group_index]
            if cell == 'y':
                sortedgroups.append(values[0][group_index])
    except:
        pass
    return sortedgroups

def person_from_group(group):
    persons = []
    mainroster = sheets[0].get("properties", {}).get("title", "mainroster") # Assumes mainroster is 1st sheet
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_Id, range=mainroster).execute()
    values = result.get('values', [])
    try:
        SIDindex = values[0].index("SID")
        group_index = values[0].index(group)
        num_rows = len(values)
        num_cols = len(values[0])
        for row_index in range(1, num_rows):
            if values[row_index][group_index] == 'y':
                persons.append(values[row_index][SIDindex])
    except:
        pass
    return persons

# Input n should not be zero-indexed.
def num_to_letter(n):
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string

def create_group(title, parent='ulab'):
    requests = []
    values = [
    ["SID", "Role", "Subgroups", "Parent"], # Additional rows
    ]
    requests.append({
        "addSheet": {
            "properties": {
              "title": title,
            }
            }
        }
    )
    values1= [
    ["SID", "Role", "Subgroups", "Parent"]# Additional rows
    ]
    if parent and type(parent) == str:
        values2 = [["", "", "", parent]]
    data = [
    {
        'range': title + "!A1:D1",
        'values': values1
    },
    {
        'range': title + "!A2:D2",
        'values': values2
    }
    # Additional ranges to update ...
    ]
    body2 = {
    'valueInputOption': "USER_ENTERED",
    'data': data
    }
    if requests:
        body = {'requests': requests}
        response = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_Id, body=body).execute()
        sheetId = response.get('replies')[0].get('addSheet').get('properties').get('sheetId')
        column = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_Id, body=body2).execute()

    #add group to parent's subgroup
    if parent and type(parent) == str:
        parent_sheet = service.spreadsheets().values().get(spreadsheetId=spreadsheet_Id, range=parent).execute()
        parent_values = parent_sheet.get('values', [])
        parent_subgroup_column = []
        count = 2
        for i in range(1, len(parent_values)):
            row = parent_values[i]
            if len(row) > 2:
                subgroup = row[2]
                parent_subgroup_column.append(subgroup)
                count += 1
        parent_subgroup_column.append(title)
        body3 = {
                'valueInputOption': "USER_ENTERED",
                "data": [
                    {
                        "range": parent + "!C2:C" + str(count + 1),
                        "majorDimension": "COLUMNS",
                        "values": [
                            parent_subgroup_column
                        ]
                    }
                ]
        }
        addSubgroup = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_Id, body=body3).execute()
    #add group to mainroster column
    mainrosterid = get_sheetid('mainroster')
    mainroster = service.spreadsheets().values().get(spreadsheetId=spreadsheet_Id, range='mainroster').execute()
    values = mainroster.get('values', [])
    num_rows = len(values)
    num_cols = len(values[0])
    default_values = []
    default_values.append(title)
    letter = num_to_letter(num_cols + 1)
    for i in range(num_rows - 1):
        default_values.append('n')
    rangeName = '!' + letter + '1:' + letter + str(num_rows)
    body4 = {
            'valueInputOption': "USER_ENTERED",
            "data": [
                {
                    "range": 'mainroster' + rangeName,
                    "majorDimension": "COLUMNS",
                    "values": [
                        default_values
                    ]
                }
            ]
    }
    addMainColumn = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_Id, body=body4).execute()

def total_num_groups() :
    return len(get_all_groups())

def get_all_groups() :
    groups = []
    mainroster = sheets[0].get("properties", {}).get("title", "Sheet1") # Assumes mainroster is 1st sheet
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_Id, range=mainroster).execute()
    values = result.get('values', [])
    try :
        groupIndexStart = group_start_index()
        for group_index in range(groupIndexStart, len(values[0])) :
            groups.append(values[0][group_index])
    except:
        pass # Ignores sheets
    return groups

def group_start_index() :
    mainroster = sheets[0].get("properties", {}).get("title", "Sheet1") # Assumes mainroster is 1st sheet
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_Id, range=mainroster).execute()
    values = result.get('values', [])
    try :
        for group_index in range(0, len(values[0])) :
            if values[0][group_index].find("ulab") != -1 :
                break
    except :
        pass # Ignores Sheets

    return group_index
def remove_group(title):
    if title == 'ulab' or title == 'mainroster':
        return # Revise in future renditions (i.e. do not pass 'ulab' into fxn)
    sheetId = get_sheetid(title)
    if sheetId != -1:
        result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_Id, range=title).execute()
        values = result.get('values', [])
        subgroup_index = values[0].index("Subgroups")
        for row_index in range(1,len(values)) :
            subgroup_title = values[row_index][subgroup_index]
            if subgroup_title :
                remove_group(subgroup_title)
        parent_index = values[0].index("Parent")
        parent_title = values[1][parent_index]
        if parent_title != 'mainroster':
            parent_sheet = service.spreadsheets().values().get(spreadsheetId=spreadsheet_Id, range=parent_title).execute()
            parent_values = parent_sheet.get('values', [])
            # List comprehension to get the values in the subgroup column of the parent if there is a subgroup value in that row.
            parent_subgroup_column = []
            removed = False
            count = 2
            for i in range(1, len(parent_values)):
                row = parent_values[i]
                if len(row) > 2:
                    subgroup = row[2]
                    if subgroup != title:
                        parent_subgroup_column.append(subgroup)
                        removed = True
                    count += 1
            if removed :
                parent_subgroup_column.append('')
            body = {
                    'valueInputOption': "USER_ENTERED",
                    "data": [
                        {
                            "range": parent_title + "!C2:C" + str(count),
                            "majorDimension": "COLUMNS",
                            "values": [
                                parent_subgroup_column
                            ]
                        }
                    ]
            }
            deleteSubgroups = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_Id, body=body).execute()

        delsheetrequest = [{
            "deleteSheet": {
                "sheetId": sheetId,
                }
            }
        ]
        mainrosterid = get_sheetid('mainroster')
        mainroster = service.spreadsheets().values().get(spreadsheetId=spreadsheet_Id, range='mainroster').execute()
        title_rows = mainroster.get('values', [])[0]
        column_index = title_rows.index(title)
        delmaincolumnreq = [{
            "deleteDimension": {
                "range": {
                  "sheetId": mainrosterid,
                  "dimension": "COLUMNS",
                  "startIndex": column_index,
                  "endIndex":   column_index + 1
                }
            }
            }
        ]
        body2 = {"requests": delsheetrequest}
        body3 = {"requests": delmaincolumnreq}

        deleteCurgroup = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_Id, body=body2).execute()
        deleteMainColumn = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_Id, body=body3).execute()

# Returns the sheet id for the given sheet title. Returns -1 if no sheet title matches.
def get_sheetid(sheet_title):
    for sheet in sheets:
        title = sheet.get("properties", {}).get("title", "Sheet1")
        if title == sheet_title:
            sheetId = sheet.get("properties", {}).get("sheetId")
            return sheetId
    return -1

def add_person_to_mainroster(firstname, lastname, calnet, SID, email, phonenumber, supervisor):
    mainroster = service.spreadsheets().values().get(spreadsheetId=spreadsheet_Id, range='mainroster').execute()
    values = mainroster.get('values', [])
    num_rows = len(values)
    num_cols = len(values[0])
    default_values = [firstname, lastname, calnet, SID, email, phonenumber, supervisor, 'y'] # 'Yes' for membership in ulab
    letter = num_to_letter(num_cols)
    for i in range(num_cols - group_start_index() - 1): # change number depending on column before groups
        default_values.append('n')
    rangeName = '!A' + str(num_rows + 1) + ':' + letter + str(num_rows + 1)
    body = {
            'valueInputOption': "USER_ENTERED",
            "data": [
                {
                    "range": 'mainroster' + rangeName,
                    "majorDimension": "ROWS",
                    "values": [
                        default_values
                    ]
                }
            ]
    }
    addMainrow = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_Id, body=body).execute()

def add_person_to_group(SID, role, group):
    # Failure Cases
    # 1. SID isn't in ulab
    mainroster = service.spreadsheets().values().get(spreadsheetId=spreadsheet_Id, range='mainroster').execute()
    main_values = mainroster.get('values', [])
    main_SID_index = main_values[0].index('SID')
    SID_list_main = []
    for row_index in range(1, len(main_values)) :
        SID_list_main.append(main_values[row_index][main_SID_index])
    if str(SID) not in SID_list_main :
        print('Person does not exist in ulab. Add them to ulab using the add_person_to_mainroster method.')
        return
    # 2. Person already exists in the group (SID and role are same)
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_Id, range=group).execute()
    group_values = result.get('values', [])
    group_SID_index = group_values[0].index('SID')
    group_roles_index = group_values[0].index('Role')
    for row_index in range (1, len(group_values)) :
        if group_values[row_index][group_SID_index] == str(SID) and group_values[row_index][group_roles_index] == str(role) :
            print('Person already exists in this group with the requested SID and role.')
            return
    SID_column = []
    count = 2

    if group_values[1][group_SID_index] != '':
        for row_index in range(1, len(group_values)):
            SIDvalue = group_values[row_index][group_SID_index]
            SID_column.append(SIDvalue)
            count += 1

    SID_column.append(SID)
    body = {
        'valueInputOption': "USER_ENTERED",
        "data": [
            {
                "range": group + "!A2:A" + str(count),
                "majorDimension": "COLUMNS",
                "values": [SID_column]
            }
        ]
    }
    #### Replacing Role Column
    role_column = []
    count = 2

    if group_values[1][group_roles_index] != '':
        for row_index in range(1, len(group_values)) :
            roles = group_values[row_index][group_roles_index]
            role_column.append(roles)
            count += 1

    role_column.append(role)
    body2 = {
        'valueInputOption': "USER_ENTERED",
        "data": [
            {
                "range": group + "!B2:B" + str(count),
                "majorDimension": "COLUMNS",
                "values": [role_column]
            }
        ]
    }

    # replace 'n' w/ 'y'
    main_group_index = main_values[0].index(group)
    num_cols = len(main_values[0])
    letter = num_to_letter(num_cols)
    for row_index in range(1, len(main_values)):
        if str(SID) == main_values[row_index][main_SID_index]:
            row = row_index
            main_values[row_index][main_group_index] = 'y'
            rangeName = '!A' + str(row_index) + ':' + letter + str(row_index)
            break

    body3 = {
        'valueInputOption': "USER_ENTERED",
        "data": [
            {
                "range": 'mainroster',
                "majorDimension": "ROWS",
                "values": main_values
            }
        ]
    }

    replaceSIDs = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_Id, body=body).execute()
    replaceRoles = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_Id, body=body2).execute()
    replaceMain = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_Id, body=body3).execute()

def del_person_from_group(SID, group):
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_Id, range=group).execute()
    values = result.get('values', [])
    SID_index = values[0].index('SID')
    role_index = values[0].index('Role')
    subgroup_index = values[0].index("Subgroups")
    #### Recursive Call
    for row_index in range(1,len(values)) :
        if values[1][subgroup_index] != '' : # Checks if there is a subgroup
            subgroup_title = values[row_index][subgroup_index]
            print(subgroup_title)
            del_person_from_group(SID, subgroup_title)
    #### Replacing SID column
    SID_column = []
    count = 1
    for row_index in range(1, len(values)):
        SIDvalue = values[row_index][SID_index]
        SID_column.append(SIDvalue)
        count += 1

    if str(SID) in SID_column:
        SID_column.remove(str(SID))
        SID_column.append('')
    else :
        print('A person of this SID does not exist in the group.')
    body = {
        'valueInputOption': "USER_ENTERED",
        "data": [
            {
                "range": group + "!A2:A" + str(count),
                "majorDimension": "COLUMNS",
                "values": [SID_column]
            }
        ]
    }
    #### Replacing Role Column
    role_column = []
    count = 1
    if values[1][role_index] != '':
        for row_index in range(1, len(values)) :
            roles = values[row_index][role_index]
            role_column.append(roles)
            SIDvalue = values[row_index][SID_index]
            if SIDvalue == str(SID) :
                role = values[row_index][role_index]
                role_column.remove(role)
                role_column.append('')
            count += 1

    body2 = {
        'valueInputOption': "USER_ENTERED",
        "data": [
            {
                "range": group + "!B2:B" + str(count),
                "majorDimension": "COLUMNS",
                "values": [role_column]
            }
        ]
    }

    # replace 'y' w/ 'n'
    mainroster = service.spreadsheets().values().get(spreadsheetId=spreadsheet_Id, range='mainroster').execute()
    main_values = mainroster.get('values', [])
    main_SID_index = main_values[0].index('SID')
    main_group_index = main_values[0].index(group)
    num_cols = len(main_values[0])
    letter = num_to_letter(num_cols)
    for row_index in range(1, len(main_values)):
        if str(SID) == main_values[row_index][main_SID_index]:
            row = row_index
            main_values[row_index][main_group_index] = 'n'
            rangeName = '!A' + str(row_index) + ':' + letter + str(row_index)
            break

    body3 = {
        'valueInputOption': "USER_ENTERED",
        "data": [
            {
                "range": 'mainroster',
                "majorDimension": "ROWS",
                "values": main_values
            }
        ]
    }

    replaceSIDs = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_Id, body=body).execute()
    replaceRoles = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_Id, body=body2).execute()
    replaceMain = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_Id, body=body3).execute()

def del_person_from_ulab(SID):
    del_person_from_group(SID, 'ulab')
    mainrosterid = get_sheetid('mainroster')
    mainroster = service.spreadsheets().values().get(spreadsheetId=spreadsheet_Id, range='mainroster').execute()
    values = mainroster.get('values', [])
    roworder = 0
    requests = []
    try:
        SIDindex = values[0].index("SID")
        for row in values:
            if str(SID) == row[SIDindex]:
                requests.append({
                    'deleteDimension': {
                        'range': {
                            'sheetId': mainrosterid,
                            'dimension': 'ROWS',
                            'startIndex': roworder,
                            'endIndex': roworder + 1,
                        }
                    }
                }
            )
            roworder += 1
    except:
        pass # Ignores sheets that do not have SID as a column
    if requests:
        body = {'requests': requests}
        response = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_Id, body=body).execute()

# Returns the Group object corresponding to the given group name. If there
# is no group of this name, returns None. This function is used in the Group class as well.
# Needs to create a Group instance according to the constructor defined in the Group class and return that instance.
# The parent field of Group is another Group and the subgroups field is a list of subgroup names.
# So, to get the Group <group_name> you would also need to get the parent group.
# (Just call get_group on the parent group name for this.)
def get_group(group_name):
    group_sheet = service.spreadsheets().values().get(spreadsheetId=spreadsheet_Id, range=group_name).execute()
    values = group_sheet.get('values', [])
    if not values:
        return None
    SID_index = values[0].index('SID')
    role_index = values[0].index('Role')
    subgroup_index = values[0].index("Subgroups")
    parent_index = values[0].index("Parent")
    parent_name = values[1][parent_index]
    persons = {}
    subgroups = set()
    for row in range(1, len(values)):
        sid = int(values[row][SID_index])
        role = values[row][role_index]
        subgroup = str(values[row][subgroup_index])
        if subgroup:
            subgroups.add(subgroup)
        if sid:
            persons[sid] = role
    if group_name == ROOT_GROUP:
        group = Group(group_name, persons, subgroups, True)
    else:
        group = Group(group_name, persons, subgroups, True, get_group(parent_name))
    return group


# Returns the Person object corresponding to the given SID. If there is no person with this SID, returns None.
# Needs access to the spreadsheets. Needs to create a Person instance according to the constructor defined in the Person class.
# For now just create the Person instance with basic field information (name, sid, email, etc.). We can add other fields later.
def get_person(SID):
    mainroster = service.spreadsheets().values().get(spreadsheetId=spreadsheet_Id, range=ROSTER).execute()
    values = mainroster.get('values', [])
    if not values:
        return None
    field_indices = {}
    group_index = group_start_index()
    # Get the index of each field in the sheet, such as SID, First Name, etc.
    for i in range(group_index):
        field_indices[values[0][i]] = i

    person_fields = {}
    for row_index in range(1, len(values)):
        if str(SID) == values[row_index][field_indices[Person.SID]]:
            # To accommodate all the necessary fields, make a list of fields instead in the Person class.
            person_fields[Person.SID] = values[row_index][field_indices[Person.SID]]
            person_fields[Person.USERNAME] = values[row_index][field_indices[Person.USERNAME]]
            person_fields[Person.LAST_NAME] = values[row_index][field_indices[Person.LAST_NAME]]
            person_fields[Person.FIRST_NAME] = values[row_index][field_indices[Person.FIRST_NAME]]
            person_fields[Person.SUPERVISOR] = values[row_index][field_indices[Person.SUPERVISOR]]
            person_fields[Person.EMAIL] = values[row_index][field_indices[Person.EMAIL]]
            person_fields[Person.PHONE_NUMBER] = values[row_index][field_indices[Person.PHONE_NUMBER]]
            groups = set()
            groupIndexStart =  group_start_index()
            for group_index in range(groupIndexStart, len(values[SIDrow])):
                cell = values[row_index][group_index]
                if cell == 'y':
                    groups.add(values[0][group_index])
            return Person(person_fields, True, groups)
    return None


"""
During tree traversals of the group structure, Group objects will not be
created until needed. The subgroups field of Groups will store string names
of subgroups and when the actual Group object is needed, we call get_group on
that string name.

After making modifications to a group, use the save() function to commit the changes
to the spreadsheet.
"""

class Group:

    def __init__(self, name='', subgroups=set(), exists=False, parent=None):
        self.name = name
        self.subgroups = subgroups
        # Stored as a dictionary of SIDs to roles, as Person objects here
        # will take up a considerable amount of space. This dictionary
        # should only be populated at leaf node groups.
        self.people = {}
        self.exists = exists
        self.parent = parent
        self.googlegroup = 'example@googlegroups.com'
    def __init__(self, name='', people = {}, subgroups=set(), exists=False, parent=None):
        self.name = name
        self.subgroups = subgroups
        # Stored as a dictionary of SIDs to roles, as Person objects here
        # will take up a considerable amount of space. This dictionary
        # should only be populated at leaf node groups.
        self.people = people
        self.exists = exists
        self.parent = parent
        self.googlegroup = 'example@googlegroups.com'

    # Returns whether this group is a leaf or not. The group is a leaf only if there are no subgroups.
    def isLeaf(self):
        return not bool(subgroups)

    # Takes in a string name of the subgroup we are adding as a child of this group.
    def add_subgroup(self, subgroup):
        if type(subgroup) == str:
            self.subgroups.add(subgroup)

    # Adds a person to the group if they are not already in it. People can only be added to groups
    # that are leaves in the ULAB organization. Traverse the path back to the root and add the person
    # to each ancestor group's respective column on mainroster. Returns true if the person is added successfully.
    def add_person_to_group(self, person, role):
        if not person or not isinstance(person, Person):
            print("Please provide a proper person.")
            return False
        if not self.isLeaf():
            print("Please specify a more specific subgroup to add this person to.")
            return False

        if person.SID in self.people:
            print("This person already exists in the group.")
            return True
        else :
            self.people[person.SID] = role
            group = self
            while group.parent != None:
                if group.name not in person.groups:
                    person.groups.add(group.name)
                group = group.parent
            return True

    # Removes a person from this group if they are in the group. If this group is a leaf, the person is only removed from this leaf group.
    # If this group is an internal node, we remove the person from all the subgroups as well. Returns true if the remove is successful and
    # returns false otherwise.
    def remove_person_from_group(self, person):
        if not person or not isinstance(person, Person):
            print("Please provide a proper person.")
            return False

        if self.isLeaf():
            if person.SID not in self.people:
                print("This person does not exist in the group.")
                return True
            else:
                del self.people[person.SID]
        else:
            # Remove this group from the set of group names for the person.
            person.groups.remove(self.name)
            # Recursively remove the person from subgroups.
            for subgroup_name in self.subgroups:
                subgroup = Group.get_group(subgroup_name)
                if subgroup and isinstance(subgroup, Group):
                    subgroup.remove_person_from_group(person)

    def remove_group(self):
        pass
    def save_group(self):
        pass

"""
After making modifications to a person, use the save() function to commit the changes
to the spreadsheet.
"""

class Person:


    # Define fields for the Person type here.
    SID  = 'SID'
    FIRST_NAME = 'First Name'
    MIDDLE_NAME = 'middle_name'
    LAST_NAME = 'Last Name'
    USERNAME = 'CalNet'
    SUPERVISOR = 'supervisor'
    EMAIL = 'Email'
    PHONE_NUMBER = 'Phone Number'
    MAJORS = 'majors'
    BACK_ID = 'back_id'
    DIETARY_PREFERENCES = 'dietary_preferences'
    EXPECTED_GRADUATION = 'expected_graduation'
    CLASSES = 'classes'
    GOALS = 'goals'
    ACCOUNTS = 'accounts'
    ACCESSES = 'accesses'

    def __init__(self, person_fields={}, exists=False, groups=set()):
        self.SID = person_fields[Person.SID]
        self.first_name = person_fields[Person.FIRST_NAME]
        self.middle_name = person_fields[Person.MIDDLE_NAME]
        self.last_name = person_fields[Person.LAST_NAME]
        self.username = person_fields[Person.USERNAME]
        self.supervisor = person_fields[Person.SUPERVISOR]
        self.email = person_fields[Person.EMAIL]
        self.phone = person_fields[Person.PHONE_NUMBER]
        self.majors = person_fields[Person.MAJORS]
        self.back_id = person_fields[Person.BACK_ID]
        self.dietary_preferences = person_fields[Person.DIETARY_PREFERENCES]
        self.expected_graduation = person_fields[Person.EXPECTED_GRADUATION]
        self.classes = person_fields[Person.CLASSES]
        self.goals = person_fields[Person.GOALS]
        self.accounts = person_fields[Person.ACCOUNTS]
        self.accesses = person_fields[Person.ACCESSES]
        # Stores the string names of the groups that this person is a part of. Using the get_group() in employee-management.py
        # to retrieve the Group object for this group. Since order does not matter, we will use a set.
        self.groups = groups

    # Adds the string name of a group to this person.
    def add_group(self, group) :
        self.groups.append(group)

    def addRole(Role) :
        self.Roles.append(Role)

    def deleteRole(Role) :
        self.Roles.remove(Role)

    def adjustFirstName(Name) :
        self.FirstName = Name

    def adjustLastName(Name) :
        self.LastName = Name

    def adjustMiddleName(Name) :
        self.MiddleName = Name

    def adjustSID(newSID) :
        self.SID = newSID

    def adjustEmail(newEmail):
        self.Email = newEmail

    def adjustPhoneNumber(newPhoneNumber):
        self.PhoneNumber = newPhoneNumber

    def dietaryPreferences(DietaryPreferences):
        self.DietaryPreferences = DietaryPreferences

    def linkSchedule(schedule):
        self.schedule = schedule

    def remove_person(self):
        pass
    def save_person(self):
        pass



if __name__ == '__main__':
    main()
