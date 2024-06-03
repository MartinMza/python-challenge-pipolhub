import polars as pl
import os
from dotenv import load_dotenv

from typing import Optional, Union
from ..models.data import RowData, ListData, ListDataQuery
from ..utils.download_file import download_file

load_dotenv()

URL = os.getenv("URL_FILE")
FILES_FOLDER_NAME:str = os.getenv("FILE_FOLDER_NAME")
FILE_NAME:str = os.getenv("FILE_NAME")
FILE_PATH:str = f"./{FILES_FOLDER_NAME}/{FILE_NAME}"

class DataService:
    """
    Service for handling data operations.

    Attributes:
        path_file (Optional[str]): The path to the file.
        lazy_frame (Optional[pl.LazyFrame]): The lazy frame representing the data.
    """

    path_file : Optional[str]
    lazy_frame: Optional[pl.LazyFrame]

    def __init__(self, path:str=FILE_PATH):
        """
        Initialize the DataService.

        Args:
            path (str): The path to the file.
        """
        download_file(url=URL)
        self.path_file = path
        self._load_csv()
        
    def _load_csv(self, sep:str=",")->None:
        """
        Load the CSV file into a lazy frame.

        Args:
            sep (str): The separator used in the CSV file.
        """
        
        self.lazy_frame = pl.scan_csv(source=self.path_file, has_header=True, separator=sep,infer_schema_length=None)

  
    def get_line(self, where:Optional[str]="", order_by:Optional[str]="")->Union[RowData, None]:
        """
        Get a single row from the data.

        Args:
            where (Optional[str]): The condition to filter the data.
            order_by (Optional[str]): The order by which to sort the data.

        Returns:
            Union[RowData, None]: The retrieved row data, or None if not found.
        """
        if where != "": where=f"WHERE {where}"
        if order_by != "": order_by=f"ORDER BY {order_by}"

        result=self.lazy_frame.sql(f"SELECT * FROM self {where} {order_by}").limit(1).collect().to_dicts()

        if result: return RowData(**result[0])
        
        return None


    def get_multi_lines(self, where:Optional[str]="", order_by:Optional[str]="", limit:Union[str,int]=5, skip:Union[str,int]=0,)->ListData:
        """
        Get multiple rows from the data.

        Args:
            where (Optional[str]): The condition to filter the data.
            order_by (Optional[str]): The order by which to sort the data.
            limit (Union[str, int]): The maximum number of rows to retrieve.
            skip (Union[str, int]): The number of rows to skip.

        Returns:
            ListData: The list of retrieved row data.
        """        
        if where != "": where=f"WHERE {where}"
        if order_by != "": order_by=f"ORDER BY {order_by}"

        result=self.lazy_frame.sql(f"SELECT * FROM self {where} {order_by} OFFSET {skip}").limit(int(limit)).collect().to_dicts()

        data = [RowData(**line) for line in result]
        return ListData(list_data=data)
    
    def get_multi_lines_by_query(self,query:str):
        """
        Get multiple rows from the data using a custom query.

        Args:
            query (str): The SQL query to execute.

        Returns:
            ListDataQuery: The list of retrieved row data as dictionaries.
        """
        query = query.replace("\n"," ").replace(";","")
        result = self.lazy_frame.sql(query).collect().to_dicts()
        return ListDataQuery(list_data=result)

DS = DataService()