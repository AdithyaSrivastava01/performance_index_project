import os
import sys
from src.exception import CustomException
from src.logger import logging
import math

import pandas as pd

from sklearn.model_selection import train_test_split

from dataclasses import dataclass


# decorator dataclass used to directly define class variables of DataIngestionConfig
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join("artifacts","train.csv")
    test_data_path: str=os.path.join("artifacts","test.csv")
    raw_data_path: str=os.path.join("artifacts","raw.csv")


# class DataIngestion:
#     def __init__(self):
#         self.ingestion = 