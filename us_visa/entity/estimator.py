import sys 
import os 
from us_visa.exception import USvisaException 
from us_visa.logger import logging  

from pandas import DataFrame 
from sklearn.pipeline import Pipeline 






class TargetValueMapping: 
    ''' This class is responsible for mapping the targert cat var into numerical '''
    
    def __init__(self) -> None:
        self.Certified:int = 0 
        self.Denied :int = 1 
        
    def _asdict(self):
        return self.__dict__ 
    
    def reverse_mapping(self):
        mapping_response = self._asdict() 
        return dict(zip(mapping_response.values() , mapping_response.keys() ))  
    
    
    
    
    
class USvisaModel : 
    pass 
        
    

     

