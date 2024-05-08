import os 
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name="brain_tumor_classification"


list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"

]

for path in list_of_files:
    file_path=Path(path)
    filedir,filename=os.path.split(file_path)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)

    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,"w") as f:
            pass

    else:
        logging.info(f"{filename} already exsist")