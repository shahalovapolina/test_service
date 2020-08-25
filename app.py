from flask import Flask, request, jsonify
import requests
import os
import json
import traceback

from controllers.CategoryPredictorController import CategoryPredictorController

application = Flask(__name__)

@application.route("/")  
def root():
    return jsonify({'message': "Hello world"})

@application.route("/categoryPrediction")
def categoryPrediction():
    controller = CategoryPredictorController()
    return controller.categoryPrediction(request)

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    application.run(debug=True, port=port, host='0.0.0.0', threaded=True)
