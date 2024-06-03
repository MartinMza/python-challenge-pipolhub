from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


def custom_openapi(app:FastAPI):
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Python Challenge Pipol Hub",
        version="0.1.0",
        summary="This documentation outlines the requirements for the challenge",
        description="""## Overview \nThe Data Service API provides access to data stored in a CSV file. It allows performing SQL-like queries on the data and obtaining responses using natural language processing (NLP) models.\n 
### Endpoints
- **POST /question**: Endpoint for processing questions using NLP.
- **GET /health**: Health check endpoint.
- **GET /get-row**: Retrieves a single row from the CSV file.
- **GET /get-rows**: Retrieves multiple rows from the CSV file.
- **GET /get-rows-query**: Retrieves multiple rows from the CSV file using a custom SQL query.
- **POST /new**: Endpoint to create a new user.
- **POST /token**: Endpoint to obtain an access token for authentication.
- **GET /users/me**: Retrieves information about the current user.\n
### Authentication

The API uses JWT (JSON Web Tokens) for authentication. Access tokens are obtained by sending a username and password to the `/token` endpoint.

### Error Handling

The API returns appropriate HTTP status codes and error messages for different scenarios. For example, a `404 Not Found` status code is returned when a resource is not found, and a `400 Bad Request` status code is returned for invalid requests.\n

### Dependencies

The API relies on the following dependencies:
- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python.
- Pydantic: Data validation and settings management using Python type annotations.
- Polars: A blazingly fast DataFrames library implemented in Rust and built to integrate with the PyData ecosystem.
- Uvicorn: ASGI server that runs FastAPI applications.
- Strawberry: GraphQL library for Python.
- Langchain: A library for natural language processing tasks, providing tools for text generation and understanding.
- OpenAI: A powerful API for natural language processing tasks, offering state-of-the-art models for text generation and understanding.
""",

        routes=app.routes,
    )
    openapi_schema["paths"]["/api/graphql"]["post"] = {
        "tags": ["Graphql"],
        "summary":"GraphQL POST", 
        "description": "This endpoint do it something and more...",
        "parameters": [
          {
            "name": "token",
            "in": "header",
            "required": "true",
            "schema": {
              "type": "string",
              "title": "Token"
            }
          }
        ],
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
    