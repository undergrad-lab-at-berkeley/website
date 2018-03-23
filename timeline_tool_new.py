from GoogleCalendarCopy import quickstartCal
from GoogleSheetsCopy import employee_management

def get_groups(SID):
  	return employee_management.groups(SID)

def get_events(my_groups):
    events = quickstartCal.main()
    sortedevents = []
    if not events:
        print('No upcoming events found.')
    else:
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            try:
                attendees = event['attendees']
                for attendee in attendees:
                    try:
                        if attendee['displayName'] in my_groups: # we can look through attendees for group instead of description
                            # print(attendee['displayName'], my_groups)
                            if event not in sortedevents:
                                # print(event)
                                sortedevents.append(event)
                    except:
                        pass
            except:
                pass
    timeline = dict()
    print('------These are your events------')
    for i in range(len(sortedevents)):
        timeline['Event ' + str(i+1)] = dict()
        allday = False
        if sortedevents[i]['start'].get('dateTime') is None:
            allday = True

        timeline['Event ' + str(i+1)]['summary'] = sortedevents[i]["summary"]
        print(sortedevents[i]["summary"])

        try:
            if allday:
                start = sortedevents[i]['start'].get('date')
                end = sortedevents[i]['end'].get('date')
                timeline['Event ' + str(i+1)]['date_time'] = 'Date & Time:' + start[0:10] + '-' + end[0:9] + str(int(end[9]) - 1)
                print('Date & Time:', start[0:10], '-', end[0:9] + str(int(end[9]) - 1))
            else:
                start = sortedevents[i]['start'].get('dateTime', sortedevents[i]['start'].get('date'))
                end = sortedevents[i]['end'].get('dateTime', sortedevents[i]['end'].get('date)'))
                # if first two numbers > 12, subtract by 12
                # 24 = 12 AM

                if int(start[11:13]) >= 20 and int(start[11:13]) != 24:
                    start = start[0:11] + str(int(start[11:13])-12) + start[13:16] + ' PM'
                elif int(start[11:13]) > 12:
                    start = start[0:11] + str(int(start[11:13])-12) + start[13:16] + ' PM'
                elif int(start[11:13]) == 12:
                    start = start[0:16] + ' PM'
                elif int(start[11:13]) == 24:
                    start = start[0:11] + str(int(start[11:13])-12) + start[13:16] + ' AM'
                else:
                    start = start[0:16] + ' AM'

                if int(end[11:13]) >= 20 and int(end[11:13]) != 24:
                    end = end[0:11] + str(int(end[11:13])-12) + end[13:16] + ' PM'
                elif int(end[11:13]) > 12:
                    end = end[0:11] + str(int(end[11:13])-12) + end[13:16] + ' PM'
                elif int(end[11:13]) == 12:
                    end = end[0:16] + ' PM'
                elif int(end[11:13]) == 24:
                    end = end[0:11] + str(int(end[11:13])-12) + end[13:16] + ' AM'
                else:
                    end = end[0:16] + ' AM'

                if start[0:10] == end[0:10]: # if dates are the same
                    timeline['Event ' + str(i+1)]['date_time'] = 'Date & Time: ' + start[0:10] + ', ' + start[11:20] + ' - ' + end[11:20]
                else: # if dates are different
                    timeline['Event ' + str(i+1)]['date_time'] = 'Date & Time: ' + start[0:10] + ', ' + start[11:20] + ' - ' + end[0:10] + end[11:20]
                print('Date & Time:', start[0:10], start[11:20], '-', end[0:10], end[11:20])
        except KeyError:
            timeline['Event ' + str(i+1)]['date_time'] = 'Date & Time: ' + 'N/A'
            pass

        try:
            timeline['Event ' + str(i+1)]['location'] = 'Location: ' + sortedevents[i]['location']
            print('Location:', sortedevents[i]['location'])
        except KeyError:
            timeline['Event ' + str(i+1)]['location'] = 'Location: ' + 'N/A'
            pass

        try:
            timeline['Event ' + str(i+1)]['description'] = 'Description: ' + sortedevents[i]["description"]
            print('Description:', sortedevents[i]["description"])
        except KeyError:
            timeline['Event ' + str(i+1)]['description'] = 'Description: ' + 'N/A'
            pass

        try:
            timeline['Event ' + str(i+1)]['link'] = 'Hangout Link: ' + sortedevents[i]['hangoutLink']
            print('Hangout Link:', sortedevents[i]['hangoutLink'])
        except KeyError:
            timeline['Event ' + str(i+1)]['link'] = 'Hangout Link: ' + 'N/A'
            pass

        print()
    return timeline

        # start = event['start'].get('dateTime', event['start'].get('date'))
        # end = event['end'].get('dateTime', event['end'].get('date)'))
        # print(event["summary"])
        # print('Date & Time:', start[0:10], start[11:25], '-', end[0:10], end[11:25])
        # print('Description:', event["description"])
        # print()

# if __name__ == "__main__":
#     SID = int(sys.argv[1])

# groups = get_groups(SID)
