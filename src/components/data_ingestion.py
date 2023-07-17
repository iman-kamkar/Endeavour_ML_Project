import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from src.simple_linear_regr_utils import generate_data


from dataclasses import dataclass

from src.components.data_transformation import DataTransformation


from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer



@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            X_train, y_train, X_test, y_test = generate_data()

            logging.info("Ingestion of the data is completed")

            return(
                X_train,
                y_train,
                X_test,
                y_test

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj = DataIngestion()
    X_train, y_train, X_test, y_test = obj.initiate_data_ingestion()

    modeltrainer=ModelTrainer()
    modeltrainer.initiate_model_trainer(X_train, y_train, X_test, y_test)
