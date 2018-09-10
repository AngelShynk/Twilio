# Twilio
Small project to download Twilio recrdings right after the call.

=======PROJECT STRUCTURE=======

DIRS:

1. recordings - keep all recordings from Twilio in wav format.

FILES:

1. downloading_recording.py - module for downloading recording to server by recording_sid(recording id in Twilio).
2. api_credentials.py  - all api credentials to twilio account.
3. app.py - Flask app to receive requests from Twilio.
