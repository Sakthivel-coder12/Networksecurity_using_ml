from dataclasses import dataclass
## dataclasses used the class that contains only the varibale name noo function in it 
## to maintain these kind of class we are using the dataclass 

@dataclass # like constructor
class DataIngestionArtifact:
    trained_file_path : str
    test_file_path : str


@dataclass
class DataValidationArtifact:
    validation_status : bool
    valid_train_file_path: str
    valid_test_file_path : str
    invalid_train_file_path : str
    invalid_test_file_path : str
    drift_report_file_path : str


