import sys 

from us_visa.exception import USvisaException 
from us_visa.logger import logging 

from us_visa.components.data_ingestion import DataIngestion 
from us_visa.components.data_validation import DataValidation 


from us_visa.entity.config_entity import (DataIngestionConfig ,DataValidationConfig)

from us_visa.entity.artifact_entity import (DataIngestionArtifact , DataValidationArtifact)





class TrainPipeline : 
    def __init__(self):
        self.data_ingestion_config  = DataIngestionConfig()  
        self.data_validaion_config = DataValidationConfig()
        
        
        
    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        This method of TrainPipeline class is responsible for starting data ingestion component steps
        """ 
        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from mongodb") 
            
            data_ingestion= DataIngestion(data_ingestion_config = self.data_ingestion_config) 
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            
            logging.info("Got the train_set and test_set from mongodb")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            
            return data_ingestion_artifact 
            
        except Exception as e :
            raise USvisaException(e,sys)  
        
        
        
        
    def start_data_validation(self , data_ingestion_artifact :DataIngestionArtifact)-> DataValidationArtifact :
        '''
        This method is the training pipeline class which is responsible to starting Data validation component 
        '''        
        logging.info(f"Enter the Data Valiadtion method inside the TrainingPipeline Class  ") 
        
        try : 
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact , 
                                             data_validation_config=self.data_validaion_config ) 
            
            
            data_validation_artifact = data_validation.initiate_data_validation() 
            logging.info(f"performed the data validation operation") 
            
            logging.info(f"Exited the Data validation method from Trainpipeline Class") 
            
            return data_validation_artifact 
        
        except Exception as e :
            raise USvisaException(e,sys)
             
            
        
        
    
    
    def run_pipeline(self, ) ->None : 
        """
        This method of TrainPipeline class is responsible for running complete pipeline of all component class 
        
        """ 
        try :
            data_ingestion_artifact = self.start_data_ingestion()
            
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            
        except Exception as e :
            raise USvisaException(e,sys)