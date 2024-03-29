# Hybrid 3D CNN and FeatureNet for Alzheimer's Disease Prediction

## Project Overview

This project develops a model to predict the progression of Alzheimer's Disease (AD) by combining 3D Convolutional Neural Networks (3D CNN) with Support Vector Machine (SVM) and leveraging critical features identified through Predictive Power Score (PPS). The model enhances prediction accuracy by incorporating temporal features in addition to spatial MRI data analysis.

## Main Notebook

### `Subject_based_Splitting_3DCNN_SVM.ipynb`

### Environment Setup
To run the models and scripts in this repository, you need a Python environment with certain libraries installed. The primary dependencies are listed below:

- Python 3.10
- Pandas: For data manipulation and analysis.
- NumPy: For numerical operations on arrays and matrices.
- NiBabel: For reading and writing Neuroimaging data files.
- Scikit-learn: For machine learning models and data processing.
- PyTorch: A deep learning framework.
- Matplotlib: For plotting graphs and visualizations.
- tqdm: For displaying progress bars during iterations.

You can install these dependencies via pip:
```
pip install pandas numpy nibabel scikit-learn torch matplotlib tqdm
```

## Data Sources

### `structured_data_mac.csv`
#### Pros
- Better quality images.
- Images resized to fit the model.
- Sufficient data quantity for model training.
#### Cons
- Lack of alignment with diagnosis conversion information.

### `dataB_change.csv`
#### Pros
- Suitable for training stage conversion features.
#### Cons
- Smaller dataset size.
- Varied types of descriptions.

## Two-Stage Training Process

### Stage One: Using `structured_data_mac.csv`
- Focused on training models like the **DualCore 3D NeuroNet**, **ResNet50**, **EnhancedFeatureNet**, and **AlexNet** with `structured_data_mac.csv` to determine accuracy in AD detection.
![3D CNN](/image/Dual.png)
![3D CNN](/image/model3.png)

### Stage Two: Incorporation of `dataB_change.csv` and SVM Classifier
- Added `dataB_change.csv` and an SVM classifier, integrating both spatial and temporal features.

## Methodology

1. **Hybrid 3DCNN FeatureNet**: Combines 3D CNN with a temporal feature analysis network.
   ![3D CNN Architecture](/image/model2.png)
2. **3DCNN + SVM**: Uses 3D CNN for MRI image processing, and SVM for classification based on combined spatial and temporal data.
   ![3D CNN Architecture](/image/model.png)

### Feature Selection
- Used Predictive Power Score (PPS) to identify highly correlated features within `dataB_change.csv`.
  ![pps](/image/pps.png)

## Integrated Models and Characteristics

- **ResNet50**: Known for its deep architecture and residual learning framework, providing a robust foundation for feature extraction.
- **EnhancedFeatureNet**: Tailored to extract and enhance nuanced features, crucial for detecting subtle changes related to AD.
- **AlexNet**: Pioneering in deep learning for image recognition, contributed to the model's ability to effectively analyze MRI data.

These models' unique strengths were synthesized into our final **3DCNN NET**, creating a powerful tool for AD progression prediction.

## Results

- **CNN-only Model**: Achieved 0.45 accuracy with MRI spatial features.
- **Feature-based Model (SVM)**: Reached 0.8 accuracy using temporal features.
- **Combined CNN + Features Model**: Highest accuracy of 0.81, blending spatial and temporal data.
  ![Result](/image/result.png)

## Conclusion

This project demonstrates that a combination of spatial MRI data with critical temporal features significantly improves AD progression prediction. The integration of advanced models like ResNet50, EnhancedFeatureNet, and AlexNet into our 3DCNN NET has been pivotal in achieving this level of accuracy and robustness.

