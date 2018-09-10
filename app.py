"""
Flask app to receive requests from Twilio.
"""

import time

from flask import Flask, request

import download_recording as dr

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def download():
    """
    This function parse get request from Twilio and download recording by recording_sid(from get request).
    I set my Twilio account to send get requests to my server after all calls.

    :return: status of app.
    """

    downloading_url = request.args.get("RecordingUrl")
    recording_sid = downloading_url.split('/')[-1]

    # Need to wait 5 seconds otherwise Twilo will not give a correct audio.
    time.sleep(5)
    dr.downloading_recording(recording_sid=recording_sid)

    return "Twilio integration app is running"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
