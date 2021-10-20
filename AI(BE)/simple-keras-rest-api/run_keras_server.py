# USAGE
# Start the server:
# 	python -m ai.simple-keras-rest-api.run_keras_server
# Submit a request via cURL:
# 	curl -X POST -F wav=@ai/test.wav http://localhost:5000/score
# Submit a request via Python:
#	python -m ai.simple-keras-rest-api.simple_request ai/test.wav http://localhost:5000/score

# import the necessary packages
from ..Multimodal.Audio_Inference import score, AudioClassifier, BERTClassifier, MultimodalClassifier
import flask
import io
import os

# initialize our Flask application and the Keras model
app = flask.Flask(__name__)

@app.route("/score", methods=["POST"])
def predict():
	# initialize the data dictionary that will be returned from the
	# view
	data = {"success": False}

	# ensure a wav was properly uploaded to our endpoint
	if flask.request.method == "POST":
		if flask.request.files.get("wav"):
			# read the wav in librosa
			wav = flask.request.files["wav"].read()
			data_file = io.BytesIO(wav)

			# preprocess the wav and prepare it for classification
			# classify the input wav and then initialize the list
			# of predictions to return to the client
			result = score(data_file)
			data["predictions"] = []

			# loop over the results and add them to the list of
			# returned predictions
			for (label, prob) in result:
				r = {"label": label, "probability": float(prob)}
				data["predictions"].append(r)

			# indicate that the request was a success
			data["success"] = True

	# return the data dictionary as a JSON response
	return flask.jsonify(data)

# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
	print(("* Loading Keras model and Flask starting server..."
		"please wait until server has fully started"))
	os.chdir('ai/Multimodal')
	score(open('../test.wav','rb'))
	app.run()
