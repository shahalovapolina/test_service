import lightgbm as lgb
import pickle
from services.SentenceNormalizeService import SentenceNormalizeService

# Service class for classifying text
class CategoryPredictorService:
    def __init__(self):
        self.vec = pickle.load(open("./models/tfidf.pickle", "rb"))
        self.model = lgb.Booster(model_file='./models/lgbm_model.txt')
        self.sentenceNormalizeService = SentenceNormalizeService()

    def categoryPrediction(self, message):
        normalizedMessage = self.sentenceNormalizeService.normalize(message)
        if normalizedMessage == '':
            return [0, 0, 0]
        vectorizedMessage = self.vec.transform([normalizedMessage])
        category = self.model.predict(vectorizedMessage.toarray()).tolist()
        return category
