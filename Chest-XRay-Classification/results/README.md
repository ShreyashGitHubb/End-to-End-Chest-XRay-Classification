# Results Directory

This directory contains visualizations and performance metrics from the model training and evaluation.

## Expected Files

Once you run the training and evaluation notebooks, the following files will be generated:

### Visualizations
- `roc_curve.png` - ROC curves for each disease class
- `confusion_matrix.png` - Multi-label confusion matrix
- `training_history.png` - Training/validation loss and accuracy curves
- `gradcam_examples/*.png` - Grad-CAM visualizations showing model attention

### Metrics
- `classification_report.txt` - Detailed classification metrics (precision, recall, F1)
- `model_performance.csv` - Performance metrics per class

## Adding Screenshots from Colab

If you trained your model in Google Colab, you can save plots by adding this code to your notebook:

```python
import matplotlib.pyplot as plt

# After creating your plot
plt.savefig('results/your_plot_name.png', dpi=300, bbox_inches='tight')
```

Then download the files from Colab and add them to this directory.

## Showcase in README

These visualizations will be referenced in the main README.md to showcase your results!
