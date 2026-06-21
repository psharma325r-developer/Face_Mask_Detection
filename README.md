# 😷 Face Mask Detection using CNN

This project is a Deep Learning based Face Mask Detection system developed using TensorFlow/Keras and Convolutional Neural Networks (CNN). The model classifies whether a person is wearing a mask or not from images.

---

## 📌 Project Overview

The project performs:

- Image preprocessing
- Image resizing
- Data augmentation
- CNN model training
- Validation and testing
- Prediction on custom images

The dataset contains two classes:

- With Mask → Label 1
- Without Mask → Label 0

---

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- OpenCV
- NumPy
- Matplotlib
- PIL
- Scikit-learn
- Google Colab

---

## 📂 Dataset

Dataset used from Kaggle:

https://www.kaggle.com/datasets/omkargurav/face-mask-dataset

Dataset folders:

```bash
with_mask/
without_mask/
```

---

## 🔄 Data Preprocessing

The images are:

- Converted into NumPy arrays
- Resized to `(128,128)`
- Converted into RGB format

---

## 🔄 Data Augmentation

Image augmentation is performed using `ImageDataGenerator`.

Techniques used:

- Rotation
- Zoom
- Width Shift
- Height Shift
- Shear Transformation
- Horizontal Flip

---

## 🧠 CNN Architecture

The CNN model contains:

- Conv2D Layers
- Batch Normalization
- MaxPooling Layers
- Flatten Layer
- Dense Layers
- Dropout Layers
- Sigmoid Output Layer

---

## ⚙️ Model Training

### Optimizer
- Adam

### Loss Function
- Binary Crossentropy

### Metric
- Accuracy

### Callbacks Used
- EarlyStopping
- ReduceLROnPlateau

---

## 📊 Model Evaluation

The model is evaluated on test data using:

- Accuracy
- Loss

Graphs plotted:

- Training Loss vs Validation Loss
- Training Accuracy vs Validation Accuracy

---

## 🔍 Prediction System

The user can provide a custom image path for prediction.

Example:

```python
input_image_path = "/content/image.jpg"
```

### Output

```bash
Mask
```

or

```bash
No Mask
```

---

## 💾 Model Saving

The trained model is saved as:

```bash
Face_mask.keras
```
