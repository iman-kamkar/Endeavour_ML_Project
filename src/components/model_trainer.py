import os
import sys
from dataclasses import dataclass
from src.simple_linear_regr import SimpleLinearRegression
from src.simple_linear_regr_utils import evaluate
from src.utils import save_object


from src.exception import CustomException
from src.logger import logging

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()


    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            model = SimpleLinearRegression()

            model.fit(X_train, y_train)
            
            y_hat = model.predict(X_test)
            
            evaluate(model, X_test, y_test, y_hat)

            logging.info(f"Model is fit on the training data")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=model
            )
            
        except Exception as e:
            raise CustomException(e,sys)