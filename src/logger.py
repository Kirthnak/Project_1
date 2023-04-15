import logging
import os
from datetime import datetime
import os

 # logging function

LOG_file= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_file)
os.makedirs(logs_path,exist_ok=True)

Log_file_path=os.path.join(logs_path,LOG_file)

logging.basicConfig(filename=Log_file_path,level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if __name__=='__main__':
    logging.info("Starting logging")