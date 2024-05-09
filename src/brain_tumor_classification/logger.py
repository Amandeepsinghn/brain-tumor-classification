import logging 
import os
from pathlib import Path
from datetime import datetime


os.makedirs("artifacts",exist_ok=True)   # to make a directory

file_name=f"{datetime.now().strftime('%Y-%M-%S-%H-%m-%s')}.log"


file_path=os.path.join(os.getcwd(),"artifacts",file_name)




logging.basicConfig(filename=file_path,
                    level=logging.INFO,
                    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s")





