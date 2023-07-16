import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from simple_linear_regr_utils import generate_data


from dataclasses import dataclass


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
            logging.info('read and split data into train and test')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            pd.concat([pd.DataFrame(X_train), pd.DataFrame(y_train)], axis=1).to_csv(
            self.ingestion_config.train_data_path, index=False, header=True)

            pd.concat([pd.DataFrame(X_test), pd.DataFrame(y_test)], axis=1).to_csv(
            self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()