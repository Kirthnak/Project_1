import os
import sys
from src.exception import custome_exp
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
   train_data_path: str=os.path.join('artifact',"train.csv")
   test_data_path: str=os.path.join('artifact',"test.csv")
   raw_data_path: str=os.path.join('artifact',"raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Starting data ingestion")
        try:
            df=pd.read_csv("notebook\data\stud.csv")
            logging.info("Reading the data")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True) # created raw file in the data ingestion folder

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=100)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)# created train file in the data ingestion folder

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)# created test file in the data ingestion folder

            logging.info("Data ingestion completed")

            return(self.ingestion_config.train_data_path,
                   self.ingestion_config.test_data_path)


        except Exception as e:
            raise custome_exp(e,sys)

if __name__ == "__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transforamtion(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))

    