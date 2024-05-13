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

