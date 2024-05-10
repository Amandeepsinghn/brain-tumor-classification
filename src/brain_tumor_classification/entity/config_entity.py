import os 
import sys 
from dataclasses import dataclass
from pathlib import Path


@dataclass
class data_ingestion_config:
    root_dir: Path
    uznip_files: Path 
    download_file: Path 


