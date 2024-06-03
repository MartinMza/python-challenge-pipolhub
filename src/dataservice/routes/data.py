from fastapi import APIRouter,HTTPException,Query
from ..models.data import RowData, ListData, ListDataQuery
from src.dataservice import DS
from typing import Optional,Union


data = APIRouter(prefix="/data_service", tags=["Data service"])

@data.get(path="/get-row", response_model=RowData, status_code=200)
async def get_row(
    where: Optional[str] = Query(default="", example="id_cli_cliente=8"), 
    order_by: Optional[str] = Query(default="", example="id_tie_fecha_valor ASC")
):
    """
    Retrieve a single row from the data source.

    Args:
        where (Optional[str]): The condition to filter the data.
        order_by (Optional[str]): The order by which to sort the data.

    Returns:
        RowData: The retrieved row data.

    Raises:
        HTTPException: If no data is found or if there's a bad request.
    """
    try:
        result = DS.get_line(where=where, order_by=order_by)
        if result:
            return result
    
        raise HTTPException(status_code=404, detail="Not Found")
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Bad Request: {str(e)}")

@data.get(path="/get-rows", response_model=ListData, status_code=200)
async def get_multi_rows(
    where: Optional[str] = Query(default="", example="id_tie_fecha_valor=20240131 AND id_cli_cliente=8"), 
    order_by: Optional[str] = Query(default="", example="desc_ga_sku_producto ASC"),
    limit: Union[str, int] = Query(default=5), 
    skip: Union[str, int] = Query(default=0)
):
    """
    Retrieve multiple rows from the data source.

    Args:
        where (Optional[str]): The condition to filter the data.
        order_by (Optional[str]): The order by which to sort the data.
        limit (Union[str, int]): The maximum number of rows to retrieve.
        skip (Union[str, int]): The number of rows to skip.

    Returns:
        ListData: The list of retrieved row data.

    Raises:
        HTTPException: If no data is found or if there's a bad request.
    """
    try:
        result = DS.get_multi_lines(where=where, order_by=order_by, limit=limit, skip=skip)
        if result:
            return result
    
        raise HTTPException(status_code=404, detail="Not Found")
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Bad Request: {str(e)}")

@data.get(path="/get-rows-query", response_model=ListDataQuery, status_code=200)
async def get_multi_rows_by_query(
    query: str = Query(default="", example="SELECT id_ga_vista, id_cli_cliente, desc_ga_sku_producto FROM self WHERE id_cli_cliente = 8 LIMIT 5")
):
    """
    Retrieve multiple rows from the data source using a query.

    Args:
        query (str): The query string to execute.

    Returns:
        ListDataQuery: The list of retrieved row data as dictionaries.

    Raises:
        HTTPException: If no data is found or if there's a bad request.
    """
    try:
        result = DS.get_multi_lines_by_query(query=query)
        if result:
            return result
    
        raise HTTPException(status_code=404, detail="Not Found")
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Bad Request: {str(e)}")