# USAGE
# python simple_request.py

# import the necessary packages
import requests
import sys

# initialize the Keras REST API endpoint URL along with the input
# wav path
KERAS_REST_API_URL = sys.argv[2]
WAV_PATH = sys.argv[1]

# load the input wav and construct the payload for the request
wav = open(WAV_PATH, "rb").read()
payload = {"wav": wav}

# submit the request
r = requests.post(KERAS_REST_API_URL, files=payload).json()

# ensure the request was sucessful
if r["success"]:
	# loop over the predictions and display them
	for (i, result) in enumerate(r["predictions"]):
		print("{}. {}: {:.4f}".format(i + 1, result["label"],
			result["probability"]))
	print(r)

# otherwise, the request failed
else:
	print("Request failed")