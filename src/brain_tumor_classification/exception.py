from src.brain_tumor_classification.logger import logging
import os 
from pathlib import Path
import sys 


def exception(error,error_details:sys):
    logging.info('we are making custom exception for our class')

    _,_,exc_tb=error_details.exc_info()

    file_name=exc_tb.tb_frame.f_code.co_filename

    return f"error found in script {file_name} in line {exc_tb.tb_lineno} and error is {str(error)}"



class Custom_Exception(Exception):

    def __init__(self,error_msg,error_detials:sys):
        super().__init__(error_msg)

        self.error=exception(error=error_msg,error_details=error_detials)


    def __str__(self):
        return self.error
    


