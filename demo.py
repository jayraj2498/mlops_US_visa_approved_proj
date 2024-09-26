from us_visa.logger import logging 
from us_visa.exception import USvisaException
import sys 
import os 

from us_visa.constants import  * 

from us_visa.pipline.training_pipeline import TrainPipeline 

obj = TrainPipeline() 

obj.run_pipeline()