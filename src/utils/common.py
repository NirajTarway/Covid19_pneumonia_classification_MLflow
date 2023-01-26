import os
import yaml
import logging
import  pandas as pd
import time
import json
from zipfile import ZipFile

def read_yaml(path_to_yaml:str)->dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    logging.info(f"YAML file: {path_to_yaml} loaded successfully")
    return content

def create_directories(path_to_directories:list)->None:
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logging.info(f"Directory created at {path}")

def save_json(path:str, data: dict):
    with open(path,'w')as f:
        json.dump(data,f,indent=4)

    logging.info(f"json file saved at: {path}")

def unzip_file(source:str, destination:str)->None:
    logging.info("unzipping started...")

    with ZipFile(source, 'r')as f:
        f.extractall(destination)

    logging.info(f"zip extracted from {source} to {destination}")
    
    
        
    

    