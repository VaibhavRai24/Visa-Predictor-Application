import sys
from us_visa.exception import MyException
from us_visa.logger import logging
from us_visa.components.data_ingestion import DataIngestion



from us_visa.entity.config_entity import DataIngestionConfig



from us_visa.entity.artifact_entity import DataIngestionArtifact


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        
        
    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        This method of TrainPipeline class is responsible for starting data ingestion component
        """
        try:
            logging.info("Entered the start data ingestion method of TrainPipline")
            logging.info("Getting the data from MONGODB----------->")
            data_ingestion = DataIngestion(data_ingestion_config= self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Data ingestion is completed")
            return data_ingestion_artifact
        except Exception as e:
            raise MyException(e, sys) from e
        
        
        
        
    def run_pipline(self, ) -> None:
        """
        This method of TrainPipeline class is responsible for running complete pipeline
        """
        
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            
            
        except Exception as e:
            raise MyException(e , sys) from e 