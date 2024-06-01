import polars as pl
import os
from dotenv import load_dotenv

from typing import Optional, Union
from .model.data import RowData, ListData
from .utils.download_file import download_file

load_dotenv()

URL = os.getenv("URL_FILE")
FILES_FOLDER_NAME:str = os.getenv("FILE_FOLDER_NAME")
FILE_NAME:str = os.getenv("FILE_NAME")
FILE_PATH:str = f"./{FILES_FOLDER_NAME}/{FILE_NAME}"

class DataService:
    path_file : Optional[str]
    lazy_frame: Optional[pl.LazyFrame]

    def __init__(self, path:str=FILE_PATH):
        download_file(url=URL)
        self.path_file = path
        self._load_csv()
        
    def _load_csv(self, sep:str=",")->None:
        """ Load data from CSV file """
        self.lazy_frame = pl.scan_csv(source=self.path_file, has_header=True, separator=sep,infer_schema_length=None)

  
    def get_line(self, where:Optional[str]="", order_by:Optional[str]="", query:Optional[str]=None)->Union[RowData, None]:
        """ This method return only one row from CSV file """
        if query:
            result=self.lazy_frame.sql(query).limit(1).collect().to_dicts()
            if result: return RowData(**result[0])
            
            return None

        if where != "": where=f"WHERE {where}"
        if order_by != "": order_by=f"ORDER BY {order_by}"

        result=self.lazy_frame.sql(f"SELECT * FROM self {where} {order_by}").limit(1).collect().to_dicts()
        if result: return RowData(**result[0])
        
        return None


    def get_multi_lines(self, where:Optional[str]="", order_by:Optional[str]="", limit:Union[str,int]=5, skip:Union[str,int]=0,query:Optional[str]=None)->ListData:
        """ This method return multi rows from CSV file """
        if query:
            result = self.lazy_frame.sql(query).collect().to_dicts()
            data = [RowData(**line) for line in result]
            return ListData(list_data=data)

        if where != "": where=f"WHERE {where}"
        if order_by != "": order_by=f"ORDER BY {order_by}"

        result=self.lazy_frame.sql(f"SELECT * FROM self {where} {order_by} OFFSET {skip}").limit(int(limit)).collect().to_dicts()

        data = [RowData(**line) for line in result]
        return ListData(list_data=data)
