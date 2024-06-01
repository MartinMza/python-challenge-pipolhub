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

@strawberry.type(description="Return info from csv")
class Query:
    """ Query class """

    @strawberry.field(
            description="This method return a only one row from csv"
            )
    def get_row(self, where:str="", order_by:str="")->RowDataType:
        row: RowDataType = RowDataType.from_pydantic(DS.get_line(where=where, order_by=order_by))
        return row

    @strawberry.field(
            description="This method return a multi rows from csv"
            )
    def get_multi_line(self, where:str="", order_by:str="", limit:int=5, skip:int=0)->ListDataType:
        list_data: ListDataType = ListDataType.from_pydantic(DS.get_multi_lines(where=where,order_by=order_by, limit=limit, skip=skip))
        return list_data   

schema = strawberry.Schema(Query, scalar_overrides={int:BigInt})

graphql_app = GraphQLRouter(schema=schema, graphiql=True,tags=["Graphql"], allow_queries_via_get=True)