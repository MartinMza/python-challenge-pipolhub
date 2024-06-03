import strawberry

from src.dataservice import RowData, ListData

@strawberry.experimental.pydantic.type(model=RowData, all_fields=True)
class RowDataType:
    """
    Pydantic type for RowData model.
    """
    pass

@strawberry.experimental.pydantic.type(model=ListData, all_fields=True)
class ListDataType:
    """
    Pydantic type for ListData model.
    """
    pass