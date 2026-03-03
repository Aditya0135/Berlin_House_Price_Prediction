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
