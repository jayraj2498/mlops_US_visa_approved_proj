from us_visa.logger import logging 
from us_visa.exception import USvisaException
import sys 

logging.info("inside demo.py code ")
try :
    a= 2/2
    print(a)  
except Exception as e : 
    raise USvisaException(e,sys)

logging.info(" outside demo.py  ")

             