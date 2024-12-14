import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
import torch.optim as optim
import numpy as np
import polars as pl
import os
import argparse

class MEData(Dataset):
    def __init__(self, data_path)