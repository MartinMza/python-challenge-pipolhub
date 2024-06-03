from pydantic import BaseModel
from typing import Optional, List, Dict

class RowData(BaseModel):
    """
    This is the model for one row in the CSV file.

    Attributes:
        id_tie_fecha_valor (int): The ID for the date value.
        id_cli_cliente (int): The ID for the client.
        id_ga_vista (int): The ID for the view.
        id_ga_tipo_dispositivo (int): The ID for the device type.
        id_ga_fuente_medio (int): The ID for the source/medium.
        desc_ga_sku_producto (str): The SKU description of the product.
        desc_ga_categoria_producto (Optional[str]): The category description of the product.
        fc_agregado_carrito_cant (int): The count of items added to the cart.
        fc_ingreso_producto_monto (float): The amount for product entry.
        fc_retirado_carrito_cant (Optional[str]): The count of items removed from the cart.
        fc_detalle_producto_cant (int): The count of product details.
        fc_producto_cant (int): The count of products.
        desc_ga_nombre_producto (Optional[str]): The name description of the product.
        fc_visualizaciones_pag_cant (Optional[str]): The count of page views.
        flag_pipol (int): The pipol flag.
        SASASA (str): The SASASA field.
        id_ga_producto (int): The ID for the product.
        desc_ga_nombre_producto_1 (str): The first name description of the product.
        desc_ga_sku_producto_1 (str): The first SKU description of the product.
        desc_ga_marca_producto (str): The brand description of the product.
        desc_ga_cod_producto (Optional[int]): The code description of the product.
        desc_categoria_producto (Optional[str]): The category description of the product.
    """
    id_tie_fecha_valor: int
    id_cli_cliente: int
    id_ga_vista: int
    id_ga_tipo_dispositivo: int
    id_ga_fuente_medio: int
    desc_ga_sku_producto: str
    desc_ga_categoria_producto: Optional[str]
    fc_agregado_carrito_cant: int
    fc_ingreso_producto_monto: float	
    fc_retirado_carrito_cant: Optional[str]	
    fc_detalle_producto_cant: int	
    fc_producto_cant: int	
    desc_ga_nombre_producto: Optional[str]	
    fc_visualizaciones_pag_cant: Optional[str]	
    flag_pipol: int	
    SASASA: str	
    id_ga_producto: int	
    desc_ga_nombre_producto_1: str	
    desc_ga_sku_producto_1: str	
    desc_ga_marca_producto: str	
    desc_ga_cod_producto: Optional[int]	
    desc_categoria_producto: Optional[str]

class ListData(BaseModel):
    """
    This is the model for listing multiple rows of data in the CSV file.

    Attributes:
        list_data (List[RowData]): A list of RowData instances representing the rows in the CSV file.
    """
    list_data: List[RowData]

class ListDataQuery(BaseModel):
    """
    This is the model for querying multiple rows of data as dictionaries.

    Attributes:
        list_data (List[Dict]): A list of dictionaries representing the rows in the CSV file.
    """
    list_data: List[Dict]