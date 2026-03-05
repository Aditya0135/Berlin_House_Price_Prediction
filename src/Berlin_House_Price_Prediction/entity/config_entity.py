import os
from dataclasses import dataclass
from pathlib import Path

# Defined our schema or the variable type for our data ingestion variables which we will later import
@dataclass(frozen=True)
class DataIngestionConfig:
    root_directory: Path
    source_url: str
    local_data_file: Path
    unzip_dir:  Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_directory: Path
    unzip_data_dir:  Path
    STATUS_FILE: str
    all_schema: dict

@dataclass(frozen=True)
class DataTransformationConfig:
    root_directory: Path
    data_path: Path
    test_size: float
    random_state: int
    features: list
    target: str
    numeric_features: list
    categorical_features: list

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_directory: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    n_estimators: int
    learning_rate:float
    random_state: int
    target_column: str