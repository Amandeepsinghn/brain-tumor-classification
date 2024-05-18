import os 
import sys 
from dataclasses import dataclass
from pathlib import Path    


@dataclass
class data_ingestion_config:
    root_dir: Path
    uznip_files: Path 
    download_file: Path 


@dataclass
class Base_model:
    root_dir: Path
    model_weights: Path
    updated_model_weights:Path
    Image_size: list
    Batch_size: int
    weights: str
    epochs: int
    classes: int
    include_top:bool

@dataclass
class check_:
    root_dir: Path
    tensorboard_dir: Path
    checkpoint: Path


@dataclass(frozen=True)
class Training_Config:
    root_dir:Path
    trained_model_path:Path
    updated_model_weights:Path
    training_data: Path 
    params_epochs: int 
    params_image_size: list  


@dataclass
class evaluation:
    training_data: Path
    model_path: Path
    image_size: list