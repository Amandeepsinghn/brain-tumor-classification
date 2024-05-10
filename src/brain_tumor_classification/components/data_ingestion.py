from pathlib import Path
from src.brain_tumor_classification.utils.common import *
from src.brain_tumor_classification.entity import *
from src.brain_tumor_classification.logger import logging 
from src.brain_tumor_classification.exception import Custom_Exception
import sys
import shutil

class comp_data_ingestion:
    try:
        def __init__(self,config1:data_ingestion_config):
            self.config=config1

        def extract_data(self):
        
            shutil.copytree(self.config.download_file,os.path.join(self.config.uznip_files),dirs_exist_ok=True)

    except Exception as e:
        raise(Custom_Exception(e,sys))
