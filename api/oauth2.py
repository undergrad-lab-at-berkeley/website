import hashlib
import os

import flask
import google.oauth2.credentials
import google_auth_oauthlib.flow

# This variable specifies the name of a file that contains the OAuth 2.0
# information for this application, including its client_id and client_secret.
CLIENT_SECRETS_FILE = "/home/u/ul/ulab/myapp/src/api/client_secret.json"

service_dict = {
    "gmail": ['https://www.googleapis.com/auth/gmail.send']
}

def credentials_to_dict(credentials):
  return {'token': credentials.token,
          'refresh_token': credentials.refresh_token,
          'token_uri': credentials.token_uri,
          'client_id': credentials.client_id,
          'client_secret': credentials.client_secret,
          'scopes': credentials.scopes}

def begin_auth(service):
    SCOPES = service_dict[service]

    # Use the client_secret.json file to identify the application requesting
    # authorization. The client ID (from that file) and access scopes are required.
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES)
    # Indicate where the API server will redirect the user after the user completes
    # the authorization flow. The redirect URI is required.
    flow.redirect_uri = flask.url_for('auth_callback', service=service, _external=True, _scheme='https')

    # Generate URL for request to Google's OAuth 2.0 server.
    # Use kwargs to set optional request parameters.
    authorization_url, state = flow.authorization_url(
        # Enable offline access so that you can refresh an access token without
        # re-prompting the user for permission. Recommended for web server apps.
        access_type='offline',
        # State is used for verifying the authorization request
        state=hashlib.sha256(os.urandom(1024)).hexdigest(),
        # Enable incremental authorization. Recommended as a best practice.
        include_granted_scopes='true')

    flask.session['state'] = state

    return flask.redirect(authorization_url)

def finish_auth(service):
    SCOPES = service_dict[service]

    # Specify the state when creating the flow in the callback so that it can
    # verified in the authorization server response.
    state = flask.session['state']

    if flask.request.args.get('state', '') != flask.session['state']:
        flask.abort(401)
    else:
        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
        flow.redirect_uri = flask.url_for('auth_callback', service=service, _external=True, _scheme='https')

        # Use the authorization server's response to fetch the OAuth 2.0 tokens.
        authorization_response = flask.request.url
        # flask.request.url should use https://
        authorization_response = authorization_response.replace("http://", "https://")

        flow.fetch_token(authorization_response=authorization_response)

        # Store credentials in the session.
        # ACTION ITEM: In a production app, you likely want to save these
        #              credentials in a persistent database instead.
        credentials = flow.credentials
        flask.session['credentials'] = credentials_to_dict(credentials)

        return flask.redirect('https://ulab.berkeley.edu/')
