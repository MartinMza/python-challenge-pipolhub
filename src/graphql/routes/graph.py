import polars as pl
from typing import Optional, Union
import strawberry
from strawberry.fastapi import GraphQLRouter
from ..models.data_model import RowDataType, ListDataType
from src.dataservice import DS

BigInt = strawberry.scalar(
    Union[int, str],  # type: ignore
    serialize=lambda v: int(v),
    parse_value=lambda v: str(v),
    description="BigInt field",
)

@strawberry.type(description="Queries to retrieve data from the CSV file.")
class Query:
    """ Query class for retrieving data from CSV. """

    @strawberry.field(
            description="Retrieve a single row from the CSV file."
            )
    def get_row(self, where:str="", order_by:str="")->RowDataType:
        """
        Get a single row from the CSV file.

        Args:
            where (str): The condition to filter the data.
            order_by (str): The order by which to sort the data.

        Returns:
            RowDataType: The retrieved row.
        """
        
        row: RowDataType = RowDataType.from_pydantic(DS.get_line(where=where, order_by=order_by))
        return row

    @strawberry.field(
            description="Retrieve multiple rows from the CSV file"
            )
    def get_multi_line(self, where:str="", order_by:str="", limit:int=5, skip:int=0)->ListDataType:
        """
        Get multiple rows from the CSV file.

        Args:
            where (str): The condition to filter the data.
            order_by (str): The order by which to sort the data.
            limit (int): The maximum number of rows to retrieve.
            skip (int): The number of rows to skip.

        Returns:
            ListDataType: The list of retrieved rows.
        """

        list_data: ListDataType = ListDataType.from_pydantic(DS.get_multi_lines(where=where,order_by=order_by, limit=limit, skip=skip))
        return list_data   

schema = strawberry.Schema(Query, scalar_overrides={int:BigInt})

graphql_app = GraphQLRouter(schema=schema, graphiql=False,tags=["Graphql"], allow_queries_via_get=False)