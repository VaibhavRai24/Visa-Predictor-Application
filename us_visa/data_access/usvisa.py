from us_visa.configuration.mongo_db_connection import MongoDBClient
from us_visa.constants import DATABASE_NAME
from us_visa.exception import MyException
import pandas as pd
import sys
import numpy as np
from typing import Optional


class USVisaData:
    """
    This class help to export entire mongo db record as pandas dataframe
    
    """
    
    def __init__(self):
        """
        Exports an entire MongoDB collection as a pandas DataFrame.

        Parameters:
        ----------
        collection_name : str
            The name of the MongoDB collection to export.
        database_name : Optional[str]
            Name of the database (optional). Defaults to DATABASE_NAME.

        Returns:
        -------
        pd.DataFrame
            DataFrame containing the collection data, with '_id' column removed and 'na' values replaced with NaN.
        """
        
        try:
            self.mongo_client = MongoDBClient(database_name= DATABASE_NAME)
        except Exception as e:
            raise MyException (e, sys)
        
        
    def export_collection_as_dataframe(self, collection_name:str, database_name:Optional[str] = None) ->pd.DataFrame:
        """
        export entire collectin as dataframe:
        return pd.DataFrame of collection
        
        """
        try:
            
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            
            df = pd.DataFrame(list(collection.find())) 
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis= 1)
                
            df.replace({"na":np.nan}, inplace= True)
            return df
        except Exception as e:
            raise MyException(e, sys)