# Data Service API

## Description
This project implements a data service API using FastAPI to provide access to data stored in a CSV file. The API allows performing SQL-like queries on the data and obtaining responses using natural language processing (NLP) models.

## Prerequisites
Make sure you have Docker and Docker Compose installed on your system before proceeding.

## Environment Configuration
Before running the application, make sure to properly configure the `.env` file with the following values:

```dotenv
# Data service
FILE_FOLDER_NAME="files"
FILE_NAME="datafile.csv"

URL_FILE="https://file.notion.so/f/f/8bdb40ef-cc0d-4853-862c-95ff2b4790ca/b82763a3-3ac0-4c8a-99bb-d763c0b00b54/Data_example_-_Python_Coding_Challenge_-_GraphQL.csv?id=76b87f9a-9e0f-4ca9-bd31-a2b4fd1b0a1d&table=block&spaceId=8bdb40ef-cc0d-4853-862c-95ff2b4790ca&expirationTimestamp=1717257600000&signature=sumM_Jp4r6FPSxCIpIcTPTPWUgjtayUUea2J0enEKbY&downloadName=Data+example+-+Python+Coding+Challenge+-+GraphQL.csv"

# Auth Variables
SECRET_KEY = "XXXXX"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

OPEN_AI = XXXXXXX

## How to Run
To run the application, follow these steps:

1. Clone this repository to your local machine.
2. Ensure that the `docker-compose.yml` file and the `Dockerfile` are in the root of the project.
3. Run the following command in your terminal to build and bring up the Docker containers:

```bash
docker-compose up --build -d
```

This will build the Docker image according to the specifications of the Dockerfile and run the API service in a Docker container.

# Accessing the API
Once the application is up and running, you can access the API at the following address:
*http://localhost:8000*

