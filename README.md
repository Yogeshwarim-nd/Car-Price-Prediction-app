# 🚗 Car Price Prediction MLOps Project

An end-to-end Machine Learning and MLOps project for predicting used car prices using an XGBoost model. This project demonstrates the complete ML lifecycle including model training, API deployment, testing, containerization, and interactive visualization.

## Project Overview

This project predicts the price of a used car based on vehicle-related attributes such as:

- Kilometers driven
- Mileage
- Vehicle age
- Fuel type (`Petrol`, `Diesel`, `Electric`)

The project was built to demonstrate practical Machine Learning engineering and MLOps concepts including:

- Machine Learning model development
- Model serving through REST APIs
- Interactive UI using Streamlit
- Unit testing and CI readiness
- Docker containerization

---

## Features

✅ Used XGBoost Regression model for price prediction  
✅ Interactive Streamlit web application for real-time predictions  
✅ Flask REST API endpoint for inference serving  
✅ Pytest-based unit testing for CI/CD readiness  
✅ Dockerized application for deployment portability  
✅ Modular and production-friendly project structure

---

## Tech Stack

| Category | Tools/Technologies |
|----------|--------------------|
| Programming | Python |
| ML Model | XGBoost |
| Data Processing | Pandas, NumPy |
| API Development | Flask |
| Frontend | Streamlit |
| Testing | Pytest |
| Containerization | Docker |
| Serialization | Pickle / Joblib |

---

## Machine Learning Pipeline

### Input Features

The model uses the following input features:

| Feature | Description |
|---------|-------------|
| `km_driven` | Total distance driven by vehicle |
| `mileage` | Fuel efficiency of vehicle |
| `age` | Age of vehicle |
| `Petrol` | Fuel type encoded feature |
| `Diesel` | Fuel type encoded feature |
| `Electric` | Fuel type encoded feature |

### Model Used

- **Algorithm:** XGBoost Regressor
- **Problem Type:** Regression
- **Objective:** Predict resale price of a car

Why XGBoost?

- Handles non-linear relationships effectively
- Robust against overfitting
- High predictive performance for tabular datasets
- Industry-standard boosting algorithm

---

## Project Architecture

```text
                    User Input
                         │
          ┌──────────────┴──────────────┐
          │                             │
     Streamlit UI                  Flask API
          │                             │
          └──────────────┬──────────────┘
                         │
                   XGBoost Model
                         │
                  Predicted Price
```

---

## Project Structure

```text
car-price-prediction-mlops/
│
├── app.py                     # Streamlit application
├── api.py                     # Flask API endpoint
├── model/
│   └── model.pkl              # Trained XGBoost model
│
├── tests/
│   └── test_model.py          # Unit tests using pytest
│
├── notebook/
│   └── training.ipynb         # Model development notebook
│
├── requirements.txt
├── Dockerfile
├── README.md
└── .github/
    └── workflows/
        └── ci.yml             # CI pipeline configuration
```

---

## Streamlit Application

A Streamlit interface was developed to simulate a real-world business use case where users can enter car specifications and instantly receive a predicted resale price.

### Inputs Accepted

- KM Driven
- Mileage
- Vehicle Age
- Fuel Type

### Output

- Predicted car price

Run locally:

```bash
streamlit run app.py
```

---

## Flask API Endpoint

A REST API endpoint was created using Flask for serving model predictions.

### API Request

**Endpoint**

```http
POST /predict
```

### Example JSON Input

```json
{
    "km_driven": 50000,
    "mileage": 18,
    "age": 5,
    "Petrol": 1,
    "Diesel": 0,
    "Electric": 0
}
```

### Example Response

```json
{
    "predicted_price": 450000
}
```

Run API locally:

```bash
python api.py
```

---

## Testing and CI Readiness

Basic unit tests were implemented using Pytest to validate critical functionalities and ensure model-serving reliability.

### Example Validations

- Model loads successfully
- Prediction pipeline executes correctly
- API response validation
- Input handling checks

Run tests:

```bash
pytest
```

This project is structured to support CI/CD workflows and automated testing pipelines.

---

## Dockerization

The project was containerized using Docker to demonstrate deployment portability and reproducibility.

### Build Docker Image

```bash
docker build -t car-price-prediction .
```

### Run Docker Container

```bash
docker run -p 8501:8501 car-price-prediction
```

Benefits of Dockerization:

- Environment consistency
- Simplified deployment
- Easy portability across systems
- Production-ready packaging

---

## Business Use Case

Used car resale price estimation is a common problem in automotive marketplaces. This project helps estimate a car's market value using historical attributes and ML-based prediction logic.

Potential use cases include:

- Online car marketplaces
- Vehicle valuation systems
- Insurance estimation systems
- Automobile analytics platforms

---

## MLOps Concepts Demonstrated

- Model Training and Serialization
- REST API Model Serving
- Streamlit-based Model Consumption
- Unit Testing with Pytest
- CI/CD Readiness
- Docker Containerization
- Modular Project Structure

---

## Future Improvements

- Cloud deployment using AWS/GCP/Azure
- CI/CD automation using GitHub Actions
- Model monitoring and logging
- Feature engineering improvements
- Database integration

---

## Author

Yogeshwari

Machine Learning | Data Analytics | MLOps Enthusiast
