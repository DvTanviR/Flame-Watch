# Flame-Watch

## Project Overview

Flame-Watch is an interactive web application for wildfire prediction, powered by a custom-trained machine learning model. The application is built using Django and provides an easy-to-use interface for users to predict wildfire risks based on provided data. The ML models and training scripts are included in the `Model/` directory, allowing users to explore, retrain, or understand the prediction logic.

### Key Features
- Wildfire risk prediction using a custom ML model
- Interactive web interface built with Django
- Reference datasets and model training scripts included
- Easy local setup and deployment

## Directory Structure

- `Application/` - Main Django application (source code, templates, static files)
- `Model/` - ML models (`.pkl` files), training scripts, and reference datasets

## Local Setup Instructions

1. **Install Python**
   - Recommended: Python 3.11 or newer

2. **Clone the repository**
   ```powershell
   git clone <your-repo-url>
   cd Project/Application
   ```

3. **Install dependencies**
   - All required libraries are listed in `requirements.txt`.
   ```powershell
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```powershell
   python manage.py migrate
   ```

5. **Run the development server**
   ```powershell
   python manage.py runserver
   ```
   - Access the app at `http://127.0.0.1:8000/`

## Deployment

You can deploy the Django application using any standard method (Heroku, PythonAnywhere, VPS, etc.). No special steps or API keys are required. All necessary files are packaged in the `Application/` folder.

## Model Details

- Pre-trained models: `best_model.pkl`, `best_model_tuned.pkl` (see `Model/`)
- Training scripts and datasets: Provided in `Model/` for reference and experimentation

## Learn More

To understand or retrain the ML model, explore the scripts and datasets in the `Model/` directory. The Django app in `Application/` is ready to use and can be customized as needed.

---
For any questions or contributions, feel free to open an issue or pull request.
