import httplib2
import googleapiclient.discovery
import flask

# Modules needed for emailing
import base64
from email.mime.text import MIMEText
from apiclient import errors


def create_message(sender, to, subject, message_text):
    """Create a message for an email.

    Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

    Returns:
    An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text)
    message['to'] = to
    # message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}


def send_message(service, user_id, message):
    """Send an email message.

    Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

    Returns:
    Sent Message.
    """
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                    .execute())
        print('Message Id: {}'.format(message['id']))

        flask.session['credentials'] = credentials_to_dict(credentials)

        return message
    except errors.HttpError as error:
        print('An error occurred: {}'.format(error))


def send_email(sender, to, subject, msg_text):
    """Uses Gmail API to create and then send an email.
    """
     # Load credentials from the session.
    credentials = google.oauth2.credentials.Credentials(**flask.session['credentials'])

    http = credentials.authorize(httplib2.Http())
    service = googleapiclient.discovery.build('gmail', 'v1', http=http)

    msg = create_message(sender, to, subject, msg_text)
    return send_message(service, sender, msg) #send_message(service, "me", msg)

# send_email("eucbital@berkeley.edu", "eucbital@berkeley.edu", "The Body of the Damned", "Let this be a message")
