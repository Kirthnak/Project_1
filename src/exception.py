import sys
from src.logger import logging

def error_message_(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename #standard code taken from document but couldn't find need to check again
     # we are trying to only  capture the exc_tb info ( need to read more about this)
    error_message="Error has occured in python script name[{0}] in line number [{1}] and error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    
    return error_message

class custome_exp(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message