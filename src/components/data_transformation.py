import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

        
    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path, header=None)
            test_df=pd.read_csv(test_path, header=None)
        


            logging.info("Read train and test data completed")

            input_feature_train_df=train_df[0]
            target_feature_train_df=train_df[1]

            input_feature_test_df=test_df[0]
            target_feature_test_df=test_df[1]

            train_arr = np.c_[
                np.array(input_feature_train_df), np.array(target_feature_train_df)
            ]

            test_arr = np.c_[
                np.array(input_feature_test_df), np.array(target_feature_test_df)
                ]

            return (
                train_arr,
                test_arr,
            )
        except Exception as e:
            raise CustomException(e,sys)