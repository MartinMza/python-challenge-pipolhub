from fastapi import APIRouter,HTTPException,Query
from ..models.data import RowData, ListData, ListDataQuery
from src.dataservice import DS
from typing import Optional,Union


data = APIRouter(prefix="/data_service", tags=["Data service"])

@data.get(path="/get-row", response_model=RowData, status_code=200)
async def get_row(where:Optional[str]=Query(default=""), order_by:Optional[str]=Query(default="")):
    """ Endpoint get one row """
    try:
        result = DS.get_line(where=where, order_by=order_by)
        if result:
            return result
    
        raise HTTPException(status_code=404, detail="Not Found")
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Bad Requests: {str(e)}")

@data.get(path="/get-rows", response_model=ListData, status_code=200)
async def get_multi_rows(where:Optional[str]=Query(default=""), order_by:Optional[str]=Query(default=""),limit:Union[str,int]=Query(default=5), skip:Union[str,int]=Query(default=0)):
    """ Endpoint get multi row """
    try:
        result = DS.get_multi_lines(where=where, order_by=order_by,limit=limit,skip=skip)
        if result:
            return result
    
        raise HTTPException(status_code=404, detail="Not Found")
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Bad Requests: {str(e)}")

@data.get(path="/get-rows-query", response_model=ListDataQuery, status_code=200)
async def get_multi_rows(query:str=Query(default="")):
    """ Endpoint get multi row """
    try:
        result = DS.get_multi_lines_by_query(query=query)
        if result:
            return result
    
        raise HTTPException(status_code=404, detail="Not Found")
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Bad Requests: {str(e)}")
