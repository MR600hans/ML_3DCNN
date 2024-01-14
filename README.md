# Hybrid 3D CNN and FeatureNet for Alzheimer's Disease Prediction

## Project Overview

This project focuses on developing a model to predict the progression of Alzheimer's Disease (AD) by combining 3D Convolutional Neural Networks (3D CNN) with Support Vector Machine (SVM) and leveraging critical features identified through Predictive Power Score (PPS). The model aims to enhance prediction accuracy by incorporating temporal features in addition to spatial MRI data analysis.

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

## Methodology

To address the challenge of predicting AD progression, we experimented with two approaches:
1. **Hybrid 3DCNN FeatureNet**: A combination of 3D CNN for spatial feature extraction from MRI data and a separate network for temporal feature analysis.
2. **3DCNN + SVM**: Ultimately, this approach was chosen for its effectiveness. The 3D CNN model processes MRI images, and SVM is used for classification based on extracted features and additional temporal data.
![3D CNN Architecture](/image/model.png)

### Feature Selection
- Utilized Predictive Power Score (PPS) to identify highly correlated features within the `dataB_change.csv` dataset.
- These features were integrated to enhance the prediction model's accuracy.

## Results

- **CNN-only Model**: Achieved an accuracy of 0.45, using only spatial features from MRI data.
- **Feature-based Model (SVM)**: Achieved an accuracy of 0.8, using selected temporal features without MRI data.
- **Combined CNN + Features Model**: The hybrid model achieved the highest accuracy of 0.81, indicating the effectiveness of combining spatial MRI data with temporal features.

## Conclusion

The project demonstrates that integrating critical temporal features alongside spatial data from MRI images significantly improves the prediction of AD progression. This holistic approach addresses the multifaceted nature of AD, offering a more robust tool for early diagnosis and monitoring of the disease.

