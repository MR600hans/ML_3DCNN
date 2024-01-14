# 3D CNN Classification for MRI Data

## Summary

This project develops a 3D Convolutional Neural Network (CNN) for classifying medical MRI images into categories: CN (Cognitively Normal), MCI (Mild Cognitive Impairment), and AD (Alzheimer's Disease). Leveraging PyTorch and CUDA GPU acceleration, this model aims to provide efficient and accurate diagnostic classifications.

## Introduction

The motivation for this project is rooted in the need for automated, reliable diagnostic tools in the medical field, particularly for neurological conditions like Alzheimer's Disease. The 3D CNN model is designed to process three-dimensional MRI data, capturing essential spatial relationships within the brain for accurate diagnosis.

## Methods

### Data Preprocessing
1. Data loading from structured CSV files, followed by cleansing to ensure the presence of expected labels.
2. Unique identification of subjects and splitting of data into training and validation sets based on these IDs.

### Model Architecture
1. The model comprises convolutional layers, pooling layers, batch normalization, global average pooling, fully connected layers, and a softmax output layer.
2. Training involves forward and backward passes, loss computation, and optimizer steps.

### Training and Validation
1. Iterative training and validation of the model across 20 epochs.
2. Computation of performance metrics like accuracy and F1 score for both training and validation phases.

### Additional Testing
- Further testing of the model with a separate dataset (dataB) to predict groups for new MRI images.

## Results

The model shows moderate accuracy in classifying MRI images into respective categories. The best model is saved based on validation loss and accuracy. Detailed results, including confusion matrices and accuracy scores, are provided.

## Discussion / Conclusion

This project highlights the potential of 3D CNNs in medical image analysis, especially in neuroimaging. While achieving satisfactory results, further tuning and a broader dataset could enhance performance. The project emphasizes the significance of deep learning in medical diagnostics and opens avenues for more advanced applications in the field.

## Data and Code Availability

- Datasets in CSV format, including MRI image paths and corresponding labels.
- MRI data processing into a uniform 3D size for model input.
- All code for data preprocessing, model definition, training routines, and evaluation scripts is available in the GitHub repository.

## Repository Structure


