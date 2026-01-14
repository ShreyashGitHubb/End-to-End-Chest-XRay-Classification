# Getting Started

## Quick Setup Guide

### 1. Initial Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/Chest-XRay-Classification.git
cd Chest-XRay-Classification

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Download Dataset

1. Go to [NIH Chest X-ray Dataset](https://nihcc.app.box.com/v/ChestXray-NIHCC)
2. Download the following files:
   - `images_001.zip` through `images_012.zip` (or at minimum download `images_001.zip` to get started)
   - `Data_Entry_2017.csv`
   - `BBox_List_2017.csv`

3. Extract files:
```bash
# Windows (PowerShell)
Expand-Archive images_001.zip -DestinationPath data\
# Or use Extract option in File Explorer

# Linux/Mac
unzip images_001.zip -d data/
```

4. Place CSV files in `data/` directory

### 3. Verify Setup

Run this quick verification script:

```python
import os
import pandas as pd

# Check if data directory exists
assert os.path.exists('data/'), "Data directory not found!"

# Check if CSV files exist
assert os.path.exists('data/Data_Entry_2017.csv'), "Data_Entry CSV not found!"

# Load and check data
df = pd.read_csv('data/Data_Entry_2017.csv')
print(f"✓ Found {len(df)} entries in dataset")
print(f"✓ Number of unique images: {df['Image Index'].nunique()}")
print("Setup verification complete!")
```

### 4. Run Notebooks

Start Jupyter and run notebooks in order:

```bash
jupyter notebook
```

Navigate to `notebooks/` and run:
1. `01_Data_Cleaning_and_EDA.ipynb`
2. `02_Model_Training.ipynb`
3. `03_Evaluation_and_Results.ipynb`

---

## Troubleshooting

**Issue**: "Module not found" errors
- **Solution**: Make sure you activated the virtual environment and installed all requirements

**Issue**: "data/ directory not found"
- **Solution**: Create the data directory: `mkdir data`

**Issue**: Out of memory during training
- **Solution**: Reduce batch size in training notebook or use Google Colab for training

**Issue**: Slow training on CPU
- **Solution**: If you have a GPU, ensure TensorFlow-GPU is installed, or use Google Colab

---

For more details, see the main [README.md](README.md)
