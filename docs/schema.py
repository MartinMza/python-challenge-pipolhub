from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


def custom_openapi(app:FastAPI):
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Python Challenge PipolHub",
        version="0.1.0",
        summary="This is the documentation about the requirements for the challenge",
        description="Here's a longer description of the custom **OpenAPI** schema",
        routes=app.routes,
    )
    openapi_schema["paths"]["/api/graphql"]["post"] = {
        "tags": ["Graphql"],
        "summary":"GraphQL POST", 
        "description": "This endpoint do it something and more...",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "string",
                "example":{"query": "{ getRow { idTieFechaValor idGaVista idGaTipoDispositivo idGaProducto idGaFuenteMedio idCliCliente flagPipol fcVisualizacionesPagCant fcRetiradoCarritoCant fcProductoCant fcIngresoProductoMonto fcDetalleProductoCant fcAgregadoCarritoCant descGaSkuProducto1 descGaSkuProducto descGaNombreProducto descGaMarcaProducto descGaNombreProducto1 descGaCodProducto descGaCategoriaProducto descCategoriaProducto SASASA } getMultiLine { listData { idTieFechaValor idGaTipoDispositivo flagPipol fcProductoCant } }}"},
                "title": "Data"
              }
            }
          },
          "required": "true"
        }, 
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {

                }
              }
            }
          }
        }}
    app.openapi_schema = openapi_schema
    return openapi_schema
    