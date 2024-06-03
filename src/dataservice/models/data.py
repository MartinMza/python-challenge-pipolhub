from pydantic import BaseModel
from typing import Optional, List, Dict, Union

class RowData(BaseModel):
    """ This is the model from one row in the CSV file """
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
    """ This is the model to listing the multiple rows of data in the CSV file """
    list_data: List[RowData]

class ListDataQuery(BaseModel):
    list_data: List[Dict]