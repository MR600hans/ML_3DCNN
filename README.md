# Hybrid 3D CNN and FeatureNet for Alzheimer's Disease Prediction

## Project Overview

This project aims to develop a model for predicting the progression of Alzheimer's Disease (AD) by combining 3D Convolutional Neural Networks (3D CNN) with Support Vector Machine (SVM) and leveraging critical features identified through Predictive Power Score (PPS). The model enhances prediction accuracy by incorporating temporal features in addition to spatial MRI data analysis.

## Main Notebook

### `Subject_based_Splitting_3DCNN_SVM.ipynb`

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
- The first stage involves training the model solely with `structured_data_mac.csv` to determine the accuracy in AD detection.
- Among the models employed in this stage is the **DualCore 3D NeuroNet**, a sophisticated model designed for high precision in identifying AD-related patterns in MRI data.

### Stage Two: Incorporation of `dataB_change.csv` and SVM Classifier
- The second stage adds `dataB_change.csv` and an SVM classifier to the training process, enhancing the model's capability to integrate and analyze both spatial and temporal features.

## Methodology

1. **Hybrid 3DCNN FeatureNet**: Combines 3D CNN for spatial feature extraction from MRI data with a network for temporal feature analysis.
   ![3D CNN Architecture](/image/model2.png)
2. **3DCNN + SVM**: This effective approach uses 3D CNN to process MRI images, with SVM for classification based on extracted features and additional temporal data.
   ![3D CNN Architecture](/image/model.png)

### Feature Selection
- Predictive Power Score (PPS) was used to identify highly correlated features within the `dataB_change.csv` dataset.
- These features were integrated to enhance the prediction model's accuracy.
  ![pps](/image/pps.png)

## Results

- **CNN-only Model**: Achieved an accuracy of 0.45, using only spatial features from MRI data.
- **Feature-based Model (SVM)**: Achieved an accuracy of 0.8, using selected temporal features without MRI data.
- **Combined CNN + Features Model**: The hybrid model reached an accuracy of 0.81, indicating the effectiveness of combining spatial MRI data with temporal features.
  ![Result](/image/result.png)

## Conclusion

The project shows that integrating critical temporal features with spatial data from MRI images significantly improves AD progression prediction. This holistic approach addresses AD's multifaceted nature, offering a more robust tool for early diagnosis and monitoring.

## Additional Models in Stage One
- **DualCore 3D NeuroNet**: A state-of-the-art model tailored for extracting intricate spatial patterns from MRI data, crucial for early-stage AD detection.
- Other models in this stage were also evaluated for their efficacy in AD pattern recognition and accuracy.

