import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            model=load_object(file_path=model_path)
            preds=model.predict(features)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)

