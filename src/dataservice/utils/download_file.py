import os
from dotenv import load_dotenv

import httpx
from loguru import logger

load_dotenv()

FILES_FOLDER_NAME:str = os.getenv("FILE_FOLDER_NAME")
FILE_NAME:str = os.getenv("FILE_NAME")
FILE_PATH:str = os.path.join(os.getcwd(), os.path.join(FILES_FOLDER_NAME, FILE_NAME))

def _create_folder(file_path:str)->None:
    """ This function creates a folder if it does not exist"""
    try:
        folder_path = os.path.dirname(file_path)
        
        if os.path.exists(folder_path):
            return
        
        os.makedirs(folder_path)

        logger.info("The created files folder")

        return
    
    except Exception as e:
        logger.error(f"Fuction _create_folder from data_service/utils has failed: \n{str(e)} ")
    

def download_file(url:str, file_path:str=FILE_PATH)->None:
    
    """ This function download file from the URL """

    try:
        if os.path.exists(file_path):
            logger.info("The csv file exists")
            return

        _create_folder(file_path)

        logger.info("Start download files")
        response = httpx.get(url=url, verify=False)
        
        if response.status_code != 200:
            raise Exception(f"Error to downloading file. \nStatus: {response.status_code}")
        
        with open(file_path, "wb") as file:
            file.write(response.content)
        
        logger.info("The file has been downloaded")

    except Exception as e:
        logger.error(f"Fuction download_file from data_service/utils has failed: \n{str(e)} ")
