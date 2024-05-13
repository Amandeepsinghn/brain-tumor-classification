from pathlib import Path
from src.brain_tumor_classification.utils.common import *
from src.brain_tumor_classification.entity import *
from src.brain_tumor_classification.logger import logging 
from src.brain_tumor_classification.exception import Custom_Exception
import sys
from src.brain_tumor_classification.constants import *


class Configuration_manager:

    try:
        def __init__(self,config_path=CONFIG_PATH,param_path=PARAMS_PATH):
            config_path = Path(config_path)
            param_path = Path(param_path)
            self.config=read_yaml(config_path)
            self.params=read_yaml(param_path)

            create_directories([self.config.artifacts_root])

        def config_manager(self)->data_ingestion_config:
            config=self.config.Data_ingestion

            create_directories([config.root_dir])


            Data_ingestion=data_ingestion_config(root_dir=config.root_dir,
                                        uznip_files=config.uznip_files,
                                        download_file=config.download_file)
            
            return Data_ingestion
        
        def base_model_config(self)->Base_model:
            config=self.config.base_model

            base_model_config=Base_model(root_dir=config.root_dir,model_weights=config.model_weights,updated_model_weights=config.updated_model_weights,
                                    Image_size=self.params.Image_size, 
                                    Batch_size=self.params.Batch_size,
                                    weights=self.params.weights,
                                    epochs=self.params.epochs,
                                    classes=self.params.classes,
                                    include_top=self.params.include_top)
        

            return base_model_config
        

    except Exception as e:
        raise(Custom_Exception(e,sys))
    
