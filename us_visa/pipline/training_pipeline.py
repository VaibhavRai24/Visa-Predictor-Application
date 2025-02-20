import sys
from us_visa.exception import MyException
from us_visa.logger import logging
from us_visa.components.data_ingestion import DataIngestion
from us_visa.components.data_validation import DataValidation
from us_visa.components.data_transformation import DataTransformation



from us_visa.entity.config_entity import DataIngestionConfig
from us_visa.entity.config_entity import DataValidationConfig
from us_visa.entity.config_entity import DataTransformationConfig


from us_visa.entity.artifact_entity import DataIngestionArtifact
from us_visa.entity.artifact_entity import DataValidationArtifact
from us_visa.entity.artifact_entity import DataTransformationArtifact



class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.data_transformation_config = DataTransformationConfig()
        
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
        
        
        
    def start_data_validation(self, data_ingestion_artifact:DataIngestionArtifact) -> DataValidationArtifact:
        """
        This method of TrainPipeline class is responsible for starting data validation component
        """
        logging.info("Entered the start_data_validation_method of traiing pipeline")
        try:
            data_validation = DataValidation(data_ingestion_artifact= data_ingestion_artifact,
                                             data_validation_config= self.data_validation_config)
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info("Performed the data validation operation")
            return data_validation_artifact
        except Exception as e:
            raise MyException(e, sys) from e
    
    
    def start_data_transformation(self, data_validation_artifact:DataValidationArtifact, data_ingestion_artifact:DataIngestionArtifact) ->DataTransformationArtifact:
        """
        This method of TrainPipeline class is responsible for starting data transformation component
        """
        try:
            data_transformation = DataTransformation(data_ingestion_artifact= data_ingestion_artifact,
                                                     data_transformation_config= self.data_transformation_config,
                                                     data_validation_artifact= data_validation_artifact)
            data_transformation_artifact = data_transformation.intiate_data_transformation()
            return data_transformation_artifact
        
        except Exception as e:
            raise MyException(e, sys)
        
        
              
    def run_pipline(self, ) -> None:
        """
        This method of TrainPipeline class is responsible for running complete pipeline
        """
        
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact= data_ingestion_artifact)
            data_transformation_artifact = self.start_data_transformation(data_ingestion_artifact= data_ingestion_artifact, data_validation_artifact= data_validation_artifact)
        except Exception as e:
            raise MyException(e , sys) from e