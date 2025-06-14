# Breast Cancer Detection using Deep Learning and Django

This project is a web-based application developed using **Django** and **TensorFlow/Keras**, which enables automated classification of breast ultrasound images into three categories: **Benign**, **Malignant**, and **Normal**. It aims to assist in the early detection of breast cancer by providing a user-friendly platform to upload and analyze ultrasound images using a pre-trained Convolutional Neural Network (CNN) model.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack Used](#tech-stack-used)
- [Project Structure](#project-structure)
- [Machine Learning Model](#machine-learning-model)
- [How to Use](#how-to-use)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [Contributors](#contributors)
- [License](#license)

## Project Overview

This web application allows users to upload breast ultrasound images and uses a deep learning model to classify them. It is primarily built for educational and research purposes and demonstrates the integration of a trained CNN model into a full-stack web framework.

## Features

- Upload ultrasound images through a web interface.
- Classify images into one of three categories: **Benign**, **Malignant**, or **Normal**.
- Model trained using **transfer learning** (VGG16 architecture).
- Basic frontend pages: `Home`, `Analysis`, and `About`.
- Backend API for image processing and prediction.
- Clear, modular Django structure for easy understanding and maintenance.

## Tech Stack Used

### Backend
- Python 3
- Django 4.x
- TensorFlow / Keras
- NumPy, Pillow

### Frontend
- HTML5, CSS3
- Bootstrap (optional)
- JavaScript (for basic interaction)

## Project Structure

```
rbcd/
├── smartheat/               # Main Django app
│   ├── migrations/
│   ├── templates/           # HTML templates and static assets
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py            # Optional (not used for DB in this version)
│   ├── urls.py              # App-specific routing
│   ├── views.py             # Core logic for upload and prediction
├── rbcd/                    # Project settings and global config
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
├── savedfiles/              # Contains pre-trained Keras model (breast_detect.h5)
├── manage.py
├── db.sqlite3
```

## Machine Learning Model

- **Model Architecture:** Transfer Learning using **VGG16** (pre-trained on ImageNet).
- **Custom Layers:** Additional convolution and dense layers added for fine-tuning.
- **Input Shape:** 224x224 RGB images.
- **Classes:** 
  - Benign (non-cancerous)
  - Malignant (cancerous)
  - Normal

- **Dataset:** Breast Ultrasound Images Dataset (publicly available on Kaggle).
- **Accuracy Achieved:** ~90% on validation data.

## How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/rbcd.git
cd rbcd
```

### 2. Setup Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> Create a `requirements.txt` using `pip freeze > requirements.txt` if not already present.

### 4. Ensure the Model File Exists

Ensure that the model file `breast_detect.h5` is placed inside:

```
rbcd/savedfiles/breast_detect.h5
```

If missing, add it manually or generate it using the ML training code.

### 5. Run the Django Server

```bash
python manage.py runserver
```

Then open the browser and navigate to:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

### 6. Upload an Image

- On the home page, click **Upload Image**
- Select an ultrasound `.png` file
- The model will predict and display the result on the screen

## Screenshots

*(You can add screenshots here by uploading images to the repo and linking them like below)*

```
![Home Page](screenshots/home.png)
![Prediction](screenshots/result.png)
```

## Future Enhancements

- Store prediction history in a database
- Add user authentication and login
- Improve frontend UI using modern JS frameworks
- Support batch image uploads
- Display prediction confidence and visualization (like heatmaps)

## Contributors

- **Karthikeya S** — Developer, ML Model, Django Integration

## License

This project is open-source and available under the MIT License.
