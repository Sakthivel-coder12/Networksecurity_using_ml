from network_security.components.data_ingestion import DataIngestion
import sys
from network_security.components.data_transformation import DataTransformation
from network_security.components.data_validation import DataValidation
from network_security.entity.config_entity import DataIngestionConfig,DatavalidationConfig,DataTransformationConfig
from network_security.components.data_validation import DataValidation
from network_security.logging.logger import logging
from network_security.exception.exception import NetworkSecurityException
from network_security.entity.config_entity import TrainingPipelineConfig

if __name__ == "__main__":
    try:
        trainingpipelieconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelieconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
    
        logging.info("Inititate the data ingestion")

        datainstestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation completed")
        data_validation_config = DatavalidationConfig(trainingpipelieconfig)
        data_validation = DataValidation(datainstestionartifact,data_validation_config=data_validation_config)

        logging.info("Initiate the data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("data validation completed")


        logging.info("Initiate the data Transformation")
        data_transformation_config = DataTransformationConfig(trainingpipelieconfig)
        data_transformation = DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("data Transformation completed")

        print(vars(dataingestionconfig))
        print(vars(data_validation_artifact))
        print(vars(data_transformation_artifact))
    except Exception as e:
        raise NetworkSecurityException(e,sys)