"""
Helper module for loading and preprocessing chest X-ray images
"""
import os
import pandas as pd
import numpy as np
from PIL import Image


def load_image(image_path, target_size=(224, 224)):
    """
    Load and preprocess a single chest X-ray image
    
    Args:
        image_path: Path to the image file
        target_size: Tuple of (height, width) for resizing
        
    Returns:
        Preprocessed image as numpy array
    """
    img = Image.open(image_path).convert('RGB')
    img = img.resize(target_size)
    img_array = np.array(img) / 255.0  # Normalize to [0,1]
    return img_array


def load_metadata(data_dir='../data'):
    """
    Load metadata CSVs
    
    Args:
        data_dir: Path to data directory containing CSV files
        
    Returns:
        Tuple of (data_entry_df, bbox_df)
    """
    data_entry = pd.read_csv(os.path.join(data_dir, 'Data_Entry_2017.csv'))
    bbox = pd.read_csv(os.path.join(data_dir, 'BBox_List_2017.csv'))
    
    return data_entry, bbox


def clean_data(data_df, bbox_df):
    """
    Clean and validate the dataset
    
    Args:
        data_df: Data entry dataframe
        bbox_df: Bounding box dataframe
        
    Returns:
        Tuple of (clean_data_df, clean_bbox_df)
    """
    # Remove empty columns
    data_df = data_df.dropna(axis=1, how='all')
    
    # Standardize column names
    bbox_df = bbox_df.rename(columns={'Finding Label': 'finding_label'})
    data_df.columns = data_df.columns.str.strip()
    bbox_df.columns = bbox_df.columns.str.strip()
    
    # Remove invalid bounding boxes
    bbox_df = bbox_df[
        (bbox_df['width'] > 0) & 
        (bbox_df['height'] > 0) &
        (bbox_df['bbox_x'] >= 0) &
        (bbox_df['bbox_y'] >= 0)
    ]
    
    return data_df, bbox_df
