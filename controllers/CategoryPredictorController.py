from flask import jsonify
import json
from services.CategoryPredictorService import CategoryPredictorService

class CategoryPredictorController:
    def __init__(self):
        self.categoryPredictorService = CategoryPredictorService()

    def categoryPrediction(self, request):
        response = {
            'message': 'ok',
            'category': -1
        }

        try:
            request_data = request.get_data()
            request_data_json = json.loads(request_data)
            user_message = request_data_json['user_message']

            response['category'] = self.categoryPredictorService.categoryPrediction(user_message)

        except Exception as e:
            print(e)
            response['message'] = e

        return jsonify(response)
