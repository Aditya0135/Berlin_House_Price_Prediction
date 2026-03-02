import zipfile
import os
from pathlib import Path
from Berlin_House_Price_Prediction.config.configuration import DataIngestionConfig
import urllib.request as request
from Berlin_House_Price_Prediction import logger
from Berlin_House_Price_Prediction.utils.common import get_size

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config=config



    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
                )
            logger.info(f"{filename} downloaded successfully with info {headers}")
        else:
            logger.info(f"file already exist of size: {get_size(Path(self.config.local_data_file))}")

    

    def extract_zipfile(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)