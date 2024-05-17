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


        def config_check(self)->check_:
        
            config=self.config.prepare_callbacks

            create_directories([config.root_dir])
            create_directories([config.tensorboard_dir])
            create_directories([config.checkpoint])


            data_checkpoint=check_(
                root_dir=config.root_dir,
                tensorboard_dir=config.tensorboard_dir,
                checkpoint=config.checkpoint
            )

            return data_checkpoint
        
        def training_config(self)-> Training_Config:
            training=self.config.training
            params=self.params
            prepare_updated_model=self.config.base_model
            training_data=os.path.join("artifacts/data_ingestion/files/bain_tumor/Training")

            create_directories([training.root_dir])


            training_config=Training_Config(
                root_dir=Path(training.root_dir),
                trained_model_path=Path(training.trained_model_path),
                updated_model_weights=Path(prepare_updated_model.updated_model_weights),
                training_data=Path(training_data), 
                params_epochs=params.epochs, 
                params_image_size=params.Image_size
                )  

            return training_config
    



    except Exception as e:
        raise(Custom_Exception(e,sys))
    
