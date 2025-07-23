# Flame-Watch

## Project Overview

Flame-Watch is an interactive web application for wildfire prediction, powered by a custom-trained machine learning model. The application is built using Django and provides an easy-to-use interface for users to predict wildfire risks based on provided data. The ML models and training scripts are included in the `Model/` directory, allowing users to explore, retrain, or understand the prediction logic.

### Key Features
- Wildfire risk prediction using a custom ML model
- Interactive web interface built with Django
- Reference datasets and model training scripts included
- Easy local setup and deployment


## Directory Structure

### Application/
```
Application/
    db.sqlite3
    manage.py
    requirements.txt
    App/
        __init__.py
        admin.py
        apps.py
        best_model_tuned.pkl
        best_model.pkl
        forms.py
        Ml.py
        models.py
        tests.py
        urls.py
        views.py
        migrations/
        templates/
    Flamewatch/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    public/
    static/
    tmp/
```

### Model/
```
Model/
    best_model_tuned.pkl
    best_model.pkl
    merging.py
    nasa_data_nonf.py
    nasa_data.py
    testing_m.py
    testing_usingdat.py
    training.py
    Training Dataset/
        nasa_merged_wildfire_data_1.csv
        nasa_non_fire_data_tst.csv
        ...
```


## Local Setup Instructions (Web Application)

1. **Install Python**
   - Recommended: Python 3.11 or newer

2. **Clone the repository**
   ```powershell
   git clone https://github.com/DvTanviR/Flame-Watch.git
   cd Flame-Watch/Application
   ```

3. **(Optional but recommended) Create a virtual environment**
   ```powershell
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/macOS
   ```

4. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

5. **Apply migrations**
   ```powershell
   python manage.py migrate
   ```

6. **Run the development server**
   ```powershell
   python manage.py runserver
   ```
   - Access the app at `http://127.0.0.1:8000/`

---

## Model Setup & Usage

1. **Clone the repository**
   ```powershell
   git clone https://github.com/DvTanviR/Flame-Watch.git
   cd Flame-Watch/Model
   ```

2. **Create a Python virtual environment (recommended)**
   ```powershell
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/macOS
   ```

3. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Train the model (optional)**
   ```powershell
   python Model/training.py
   ```

5. **Run tests or make predictions**
   ```powershell
   python Model/testing_usingdat.py
   ```


## Deployment

You can deploy the Django application using any standard method (Heroku, PythonAnywhere, VPS, etc.). No special steps or API keys are required. All necessary files are packaged in the `Application/` folder.


## Model Details

- Pre-trained models: `best_model.pkl`, `best_model_tuned.pkl` (see `Model/`)
- Training scripts and datasets: Provided in `Model/` for reference and experimentation

### Model Performance

| Metric     | Score |
|------------|-------|
| Accuracy   | 93%   |
| Precision  | 92%   |
| Recall     | 91%   |

These metrics indicate the model's strong capability in correctly predicting wildfire occurrences, balancing false positives and false negatives effectively.


## How It Works

1. **Data ingestion:** Satellite and weather data from NASA APIs are preprocessed and merged.
2. **Feature extraction:** Important variables (temperature, humidity, NDVI, wind speed, etc.) are selected.
3. **Model training:** A Random Forest classifier learns patterns distinguishing wildfire vs. non-wildfire conditions.
4. **Prediction:** The trained model evaluates new input data and predicts the risk of wildfire.
5. **Output:** Risk scores can be visualized or integrated into alerting systems.

## Features

- **Wildfire risk prediction:** Predicts fire occurrence based on climate variables like temperature, humidity, wind speed, and satellite thermal hotspot data.
- **NASA data integration:** Uses publicly available NASA FIRMS and POWER datasets.
- **Random Forest classifier:** Proven machine learning algorithm providing high accuracy and interpretability.
- **Balanced dataset training:** Trained with both fire and no-fire data to reduce false positives.
- **Performance metrics:** Achieves over 90% accuracy, precision, and recall in validation tests.
- **MIT licensed:** Free for commercial and non-commercial use.

## Learn More

To understand or retrain the ML model, explore the scripts and datasets in the `Model/` directory. The Django app in `Application/` is ready to use and can be customized as needed.

---
For any questions or contributions, feel free to open an issue or pull request.
