# 🫁 Chest X-Ray Disease Classification

An end-to-end deep learning pipeline for detecting thoracic diseases from chest X-ray images using the NIH Chest X-ray Dataset.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.8+-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🏥 Project Overview

This project implements a comprehensive machine learning pipeline for multi-label chest X-ray classification. The system can detect multiple thoracic diseases including Pneumonia, Effusion, Infiltration, and others from chest radiographs.

### Key Features

- **Data Cleaning & Validation**: Robust preprocessing pipeline with audit logging
- **Multi-Label Classification**: Handles multiple concurrent pathologies
- **Bounding Box Validation**: Geometric correctness verification
- **Referential Integrity**: Ensures consistency between metadata and images
- **Audit Logging**: Full traceability of data sanitization steps

## 📊 Key Results

> **Note**: This project was developed in Google Colab. Results may vary based on dataset availability and training configuration.

- Data Cleaning: Successfully validated and cleaned corrupted dataset entries
- Multi-label processing: Implemented label binarization for concurrent disease detection
- Correlation Analysis: Analyzed co-occurrence patterns between different pathologies

## 🛠️ Tech Stack

**Core Technologies:**
- Python 3.8+
- TensorFlow/Keras
- Pandas & NumPy
- Matplotlib & Seaborn

**Data Processing:**
- `ImageDataGenerator` for data augmentation
- `MultiLabelBinarizer` for multi-label classification
- OpenCV for image processing

**Visualization:**
- Seaborn for statistical plots
- Matplotlib for custom visualizations

## 📂 Dataset

This project uses the **NIH Chest X-ray Dataset**, which contains thousands of chest X-ray images with labels for 15 different thoracic diseases.

> **Important**: The dataset is not included in this repository due to size constraints.

### To Run This Project:

1. Download the NIH Chest X-ray Dataset:
   - Download `images_001.zip` through `images_012.zip` from the [Official NIH Source](https://nihcc.app.box.com/v/ChestXray-NIHCC)
   - Download `Data_Entry.csv` and `BBox_List_2017.csv`

2. Extract the dataset:
   ```bash
   # Create data directory
   mkdir -p data
   
   # Extract all zip files to data directory
   unzip 'images_*.zip' -d data/
   
   # Move CSV files to data directory
   mv Data_Entry.csv BBox_List_2017.csv data/
   ```

## 🚀 Getting Started

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Chest-XRay-Classification.git
   cd Chest-XRay-Classification
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project

The complete project notebook is available in the `notebooks/` directory:

**`Untitled0 (2).ipynb`** - Complete end-to-end pipeline including:
- Data loading and validation
- Data cleaning and preprocessing
- Exploratory data analysis
- Label correlation analysis
- Multi-label binarization

This notebook contains the full workflow from the Google Colab environment. To run it:

```bash
# Start Jupyter Notebook
jupyter notebook

# Navigate to notebooks/ and open Untitled0 (2).ipynb
```

> **Note**: This notebook was originally developed in Google Colab. Some paths may reference Colab-specific directories (`/content/drive/MyDrive/`). Update these to local paths (e.g., `../data/`) before running locally.

#### Optional: Organize into Separate Notebooks

For better organization, you can split the main notebook into:
1. `01_Data_Cleaning_and_EDA.ipynb` - Data cleaning and exploration
2. `02_Model_Training.ipynb` - Model training (if applicable)
3. `03_Evaluation_and_Results.ipynb` - Results and metrics

## 📁 Project Structure

```
Chest-XRay-Classification/
│
├── data/                           # Dataset directory (not tracked)
│   └── .gitkeep
│
├── notebooks/                      # Jupyter notebooks
│   ├── Untitled0 (2).ipynb        # Complete workflow from Colab
│   └── README.md                   # Notebook organization guide
│
├── models/                         # Saved models (not tracked)
│   └── .gitkeep
│
├── results/                        # Output visualizations and metrics
│   ├── roc_curve.png
│   ├── confusion_matrix.png
│   └── classification_report.txt
│
├── src/                            # Source code modules
│   ├── data_loader.py
│   └── visualization.py
│
├── .gitignore                      # Git ignore file
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## 🔬 Methodology

### Data Cleaning Pipeline

1. **Schema Normalization**: Standardized column names and data types
2. **Missing Value Handling**: Identified and handled null values
3. **Referential Integrity**: Validated image-metadata relationships
4. **Bounding Box Validation**: Verified geometric correctness
5. **Audit Logging**: Comprehensive tracking of all data modifications

### Model Pipeline

1. **Data Preprocessing**: Image resizing, normalization
2. **Data Augmentation**: Rotation, flipping, zoom
3. **Model Architecture**: CNN-based architecture
4. **Training**: Multi-label classification
5. **Evaluation**: AUC, accuracy, precision, recall

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- NIH Clinical Center for providing the Chest X-ray dataset
- TensorFlow and Keras teams for excellent deep learning frameworks

## 📧 Contact

For questions or collaboration opportunities, please open an issue in this repository.

---

**Note**: This is an educational/portfolio project. For medical applications, please consult with healthcare professionals and ensure proper validation.
