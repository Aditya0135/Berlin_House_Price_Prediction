# Berlin House Price Prediction

End-to-end machine learning project to predict **house prices in Berlin** using structured housing data.  
The project follows an **industry-style ML architecture** including data pipelines, experiment tracking, containerization, and cloud deployment.

---

## Project Overview

This project implements a complete ML workflow:

- Data ingestion and validation
- Data transformation and preprocessing
- Training and evaluation of multiple regression models
- Automatic selection of the best-performing model
- Prediction serving using a Flask web application
- Experiment tracking with MLflow
- Docker containerization and AWS deployment

---

## Features

Input features:

- area
- rooms
- heating
- energy
- zipcode

Target variable:

```

price

```

Dataset source:

```

https://www.kaggle.com/code/elhamrajabnezhad/real-estate-listings-apr2023-berlin

```

---

## Machine Learning Pipeline

```

Data Ingestion
↓
Data Validation
↓
Data Transformation
↓
Model Training
↓
Model Evaluation
↓
Prediction Application

```

Multiple models were trained (Linear Regression, Random Forest, Gradient Boosting, SVR, etc.), and the **best model was selected based on performance**.

---

## Run the Project Locally

Clone repository

```

git clone https://github.com/Aditya0135/Berlin_House_Price_Prediction
cd Berlin_House_Price_Prediction

```

Create virtual environment

```

python -m venv venv
venv\Scripts\activate

```

Install dependencies

```

pip install -r requirements.txt

```

Run the ML pipeline

```

python main.py

```

Run the web application

```

python app.py
ulr/train (train the model throgh webapp before predicting)

```

---

## MLflow Tracking

Example usage:

```

import mlflow

with mlflow.start_run():
mlflow.log_param("parameter", "value")
mlflow.log_metric("metric", 1)

```

---

## AWS Deployment (Docker + ECR + EC2)

General deployment workflow:

1. Build Docker image
2. Push image to AWS ECR
3. Pull image on EC2 instance
4. Run container to serve the application

---

## Project Workflow

```

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update entity classes
5. Update configuration manager
6. Implement components
7. Implement pipeline stages
8. Run main.py
9. Deploy with app.py

```

---

## Tech Stack

- Python
- Scikit-learn
- Flask
- MLflow
- Docker
- AWS (ECR, EC2)
- GitHub Actions
