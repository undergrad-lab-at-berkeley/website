# Based on Send_signal.py, changed to be more generic and to work with the website.
# Meant to be placed in the api directory of the website.
# Handle has a series of if statements for each task.
# Right now they all have placeholder code which just consists of emailing form information to designated recipients and the requester.
from api import gmailAPI as gmail

def handle(task_data):
    name = task_data["0"]
    group = task_data["1"]
    task = task_data["2"]
    priority = task_data["3"]
    time = task_data["4"]
    email = task_data["email"] # email of person submitting the form
    if task == "Contacting someone from outside of ULAB":
        contact = task_data["5"]
        info = task_data["6"]
        recipients = get_recipients(group)
        subject = "You have been assigned a task with {} priority".format(priority)
        message = "{} wants you to contact {} from outside of ULAB with {} priority.\nExtra Information: {}\n".format(name, contact, priority, info)
        subject2 = "You have requested a task with {} priority".format(name)
        message2 = "Task for '{}' has been assigned with {} priority.".format(task, priority)
        return send_message([recipients, subject, message, subject2, message2, email])
    if task == "Getting equipment":
        equip = task_data["5"]
        ref = task_data["6"]
        cost = task_data["7"]
        use = task_data["8"]
        recipients = get_recipients(group)
        subject = "{} wants {} with {} priority".format(name, equip, priority)
        message = "{} wants {}. Reference: {}, Est. Cost {}, Intended use {}".format(name, equip, ref, cost, use)
        subject2 = "You have requested a task with {} priority".format(priority)
        message2 = "Task for '{}' has been assigned with {} priority.".format(task, priority)
        return send_message([recipients, subject, message, subject2, message2, email])
    if task == "Getting information on a specific lab":
        contact = task_data["5"]
        info = task_data["6"]
        recipients = get_recipients(group)
        subject = "{} wants information from {} with {} priority".format(name, contact, priority)
        message = "{} wants information from {}.\n Note that {}".format(name, contact, info)
        subject2 = "You have requested a task with {} priority".format(priority)
        message2 = "Task for '{}' has been assigned with {} priority.".format(task, priority)
        return send_message([recipients, subject, message, subject2, message2, email])
    if task == "Recruiting":
        position = task_data["5"]
        desc = task_data["6"]
        reqs = task_data["7"]
        recipients = get_recipients(group)
        subject = "{} wants a new {} with {} priority".format(name, position, priority)
        message = "{} wants a new {}.\nWork will involve {} and its requirements are {}".format(name, desc, reqs)
        subject2 = "You have requested a task with {} priority".format(priority)
        message2 = "Task for '{}' has been assigned with {} priority.".format(task, priority)
        return send_message([recipients, subject, message, subject2, message2, email])
    if task == "Publicizing something":
        return
    if task == "Reimbursement":
        return
    if task == "Booking a room":
        return
    if task == "Training for lab equipment":
        return
    if task == "Attaining certification status":
        return
    if task == "Expert Consulting":
        return
    if task == "Activity Development":
        return
    if task == "Securing Lab tours":
        return

    if task == "Curricular Development":
        return
        "This is actually a work-in-progress on the Google Forms"

    if task == "Liaison Training":
        requesters = task_data["5"]
        liason_email = task_data["6"]
        recipients = get_recipients(group)
        subject = "{} requests Liaison Training with {} priority".format(name, priority)
        message = "{} from the {} request(s) training for {} with {} priority. Their email is {}.".format(name, group, requesters, priority, liason_email)
        subject2 = "You have requested a task with {} priority".format(priority)
        message2 = "Task for '{}' has been assigned with {} priority.".format(task, priority)
        return send_message([recipients, subject, message, subject2, message2, email])

    if task == "Make a change to the website":
        change = task_data["5"]
        desc = task_data["6"]
        reason = task_data["7"]
        sketch = task_data["8"]
        recipients = get_recipients(group)
        subject = "{} requests a change to the website with {} priority".format(name, priority)
        message = "{} from the {} requests (a/an) {} kind of change for the website. \nDescription of change: {} \nReasons for the change: {} \nOptional sketch for a design change: {}".format(name, group, change, desc, reason, sketch)
        subject2 = "You have requested a task with {} priority".format(priority)
        message2 = "Task for '{}' has been assigned with {} priority.".format(task, priority)
        return send_message([recipients, subject, message, subject2, message2, email])

    if task == "On Boarding":
        recruit = task_data["5"]
        recipients = get_recipients(group)
        subject = "{} needs {} to be On-Boarded with {} priority".format(name, recruit, priority)
        message = "{} from the {} needs {} to be On-Boarded with {} priority.".format(name, group, recruit, priority)
        subject2 = "You have requested a task with {} priority".format(priority)
        message2 = "Task for '{}' has been assigned with {} priority.".format(task, priority)
        return send_message([recipients, subject, message, subject2, message2, email])

    if task == "Graphic Design":
        request = task_data["5"]
        deadline = task_data["6"]
        theme = task_data["7"]
        colors = task_data["8"]
        sample = task_data["9"]
        comments = task_data["10"]
        recipients = get_recipients(group)
        subject = "{} has a Graphic Design request with {} priority".format(name, priority)
        message = "{} from the {} needs a {} with {} priority. \nThey need this by {}. Estimated time the project will take: {}. \nExtra Information: Theme: {}. Preferred Colors: {}. Inspirational Samples: {}. Additional Comments: {}.".format(name, group, request, priority, deadline, time, theme, colors, sample, comments)
        subject2 = "You have requested a task with {} priority".format(priority)
        message2 = "Task for '{}' has been assigned with {} priority.".format(task, priority)
        return send_message([recipients, subject, message, subject2, message2, email])

    #Other Case
    return

def send_message(message):
    for person in message[0]:
        #Email for the assigned
        gmail.send_email("eucbital@berkeley.edu", person, message[1], message[2])
    #Email for requester
    gmail.send_email("eucbital@berkeley.edu", message[5], message[3], message[4])

# Placeholder function for now
def get_recipients(group):
    return ["eucbital@berkeley.edu"]

# Contacting someone from outside of ULAB
# Getting equipment
# Getting information on a specific lab
# Recruiting
# Publicizing something
# Reimbursement
# Booking a room
# Training for lab equipment
# Attaining certification status
# Expert Consulting
# Activity Development
# Securing Lab tours
# Curricular Development
# Liaison Training
# Make a change to the website
# On Boarding
# Graphic Design
