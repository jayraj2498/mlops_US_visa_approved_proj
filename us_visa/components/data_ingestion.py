import os 
import sys 

from us_visa.exception import USvisaException 
from us_visa.logger import logging 

from pandas import DataFrame 
from sklearn.model_selection import train_test_split 

from us_visa.entity.config_entity import DataIngestionConfig            # it is going to written all the path 
from us_visa.entity.artifact_entity import DataIngestionArtifact        # it is going to writeen type for next component 
from us_visa.data_access.usvisa_data import USvisaData                  # it will give us dic to pd data  





class DataIngestion : 
    def __init__(self,data_ingestion_config :DataIngestionConfig=DataIngestionConfig()) :
        """
        :param data_ingestion_config : this is the configuration for data ingesiton 
        """ 
        
        try:
            self.data_ingestion_config = data_ingestion_config
            
        except Exception as e :
            raise USvisaException(e,sys) 
        
    
    """ we write the method to export the data into feature store """ 
    
    def export_data_into_feature_store(self)->DataFrame:
        """
        Method Name :   export_data_into_feature_store
        Description :   This method exports data from mongodb to csv file
        
        Output      :   data is returned as artifact of data ingestion components
        On Failure  :   Write an exception log and then raise an exception
        """ 
        
        try :
            logging.info(f"Exporting the data from mongoDB") 
            usvisa_data = USvisaData()           # <-- it will give you us visa data 
            dataframe=usvisa_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name) 
            
            logging.info(f"shape of dataframe is {dataframe.shape}") 
            
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            dir_path =os.path.dirname(feature_store_file_path) 
            os.makedirs(dir_path,exist_ok=True) 
            
            logging.info(f"Saving export data into features store file path :{feature_store_file_path}")  
            dataframe.to_csv(feature_store_file_path ,index=False , header=True)                    # here  we saving data as csv format in file path 
            return dataframe 
        
        except Exception as e :
            raise USvisaException(e,sys) 
        
        
    
    def split_data_as_train_test(self,dataframe:DataFrame) -> None : 
        """
        Method Name :   split_data_as_train_test
        Description :   This method splits the dataframe into train set and test set based on split ratio 
        
        Output      :   Folder is created 
        On Failure  :   Write an exception log and then raise an exception 
        
        """        
        logging.info(f"Entering split data and train_test_split on the dataframe") 
        
        try :
            train_set, test_set =train_test_split(dataframe , test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info(f"performed train test split opeation on dataframe ")
            logging.info(f"Exited split data_as train_test method of Data_Ingestion class") 
            
            dir_path=os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path , exist_ok=True)  
            
            logging.info("Exporting train and test file Path")  
            
            train_set.to_csv(self.data_ingestion_config.training_file_path , index=False , header=True)         # saving inside the path 
            test_set.to_csv(self.data_ingestion_config.test_file_path , index=False , header=True )
            
        except Exception as e :
            raise USvisaException(e,sys)
            
            
            
    ''' To exceute above 2 funtion we write final funtion below '''    
            
    def initiate_data_ingestion(self) -> DataIngestionArtifact : 
        """
        Method Name :   initiate_data_ingestion
        Description :   This method initiates the data ingestion components of training pipeline 
        
        Output      :   train set and test set are returned as the artifacts of data ingestion components
        On Failure  :   Write an exception log and then raise an exception
        
        """        
        logging.info(f"Entered into initiate_data_ingestion method of data_ingestion Class ") 
        
        try :
            dataframe = self.export_data_into_feature_store()            # calling 1st method 
            
            logging.info(f"get the data from mongodb") 
            
            self.split_data_as_train_test(dataframe)                      # calling 2nd method 
            
            logging.info(f"Exited initiate_data_ingestion method of Data_Ingestion class") 
            
            data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path , 
                                                            test_file_path=self.data_ingestion_config.test_file_path)   # as artifact we get our trainign & tesing directory for next component 
            
            logging.info(f" Data Ingestion Artifact done: {data_ingestion_artifact} ") 
            
            return data_ingestion_artifact
            
        except Exception as e :
            raise USvisaException(e,sys)  
        
        
        
        


# after that we move to our next module called pipeline 

