import strawberry

from ...dataservice import RowData, ListData

@strawberry.experimental.pydantic.type(model=RowData, all_fields=True)
class RowDataType:
    pass

@strawberry.experimental.pydantic.type(model=ListData, all_fields=True)
class ListDataType:
    pass