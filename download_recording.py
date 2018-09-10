"""
Simple module for downloading gecording from Twilio.
"""

import requests
import json
import os

from tqdm import tqdm

import api_credentials as acr

# Template of recording downloading url in wav format. You can also change to .mp3.
DOWNLOAD_URL_TEMP = "https://api.twilio.com/2010-04-01/Accounts/{}/Recordings/{}.wav"


CURRENT_PATH = os.path.abspath(os.curdir) + "/"
RECORDINGS_PATH = "recordings/"


def downloading_recording(recording_sid):
    """
    Downloading recording to your server.

    :param recording_sid: unique recording id from Twilio.
    :return: json with information about downloading status.
    """

    # You can find your ACCOUNT_SID in your Twilio account.
    downloading_url = DOWNLOAD_URL_TEMP.format(acr.ACCOUNT_SID, recording_sid)

    # local filename is recording sid.
    local_filename = downloading_url.split('/')[-1]
    r = requests.get(downloading_url, stream=True)

    # Creating wav file.
    with open(CURRENT_PATH + RECORDINGS_PATH + local_filename, 'wb') as f:
        for data in tqdm(r.iter_content()):
            f.write(data)

    # Preparing answer dict.
    answer_dict = {}
    answer_dict["task"] = "downloading_recording"
    answer_dict["status"] = "done"
    answer_dict["recording_path"] = CURRENT_PATH + RECORDINGS_PATH + local_filename

    return json.dumps(answer_dict)


