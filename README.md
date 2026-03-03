# Berlin House Price Prediction

End-to-end machine learning pipeline to predict house prices in Berlin using structured housing data.
This project is designed with an **industry-style ML architecture**, where each stage of the pipeline is modular, configurable, and reproducible.

---

# Project Goal

The objective of this project is to build a production-like machine learning system that:

* Ingests raw housing data
* Validates dataset structure
* Cleans and transforms data
* Trains multiple regression models
* Evaluates model performance
* Serves predictions through an application

This project focuses not only on modeling but also on **ML system design**.

---

# Features Used

The model currently uses these input features:

* area
* rooms
* heating
* energy
* zipcode

Target variable:

```
price
```

---

# Machine Learning Pipeline

## 1. Data Ingestion

Responsible for:

* Loading dataset
* Extracting raw files
* Storing data in artifacts folder

Output:

```
artifacts/data_ingestion/
```

---

## 2. Data Validation

Ensures dataset quality before training.

Validation checks include:

* Column existence
* Schema validation
* Data types
* Dataset consistency

All validation rules are defined in:

```
schema.yaml
```

---

## 3. Data Transformation

This stage performs **data cleaning and preprocessing**.

Operations include:

* Cleaning categorical columns
* Removing commas and unnecessary text
* Handling rare categories
* Outlier removal
* Missing value imputation
* Feature encoding (One-Hot Encoding)
* Train/Test split
* Feature scaling

Output:

```
Cleaned and transformed dataset
```

---

## 4. Model Training

Multiple models are trained and evaluated:

* Linear Regression
* Ridge
* Lasso
* ElasticNet
* Random Forest
* Gradient Boosting
* Support Vector Regressor

Evaluation metrics:

* R² Score
* Mean Squared Error

The best-performing model is selected automatically.

---

# Configuration System

The pipeline is controlled using configuration files.

## config.yaml

Defines pipeline paths and folder structure.

Example:

```
artifacts_root: artifacts

data_ingestion:
  root_dir: artifacts/data_ingestion
```

---

## schema.yaml

Defines dataset structure and expected data types.

Example:

```
COLUMNS:
  area: float64
  rooms: float64
  heating: object
  energy: object
  zipcode: float64
  price: float64

TARGET_COLUMN:
  name: price
```

---

## params.yaml

Contains model hyperparameters.

Example:

```
RandomForest:
  n_estimators: 100
  max_depth: 10
```

---

# How to Run the Project

## 1. Clone the Repository

```
git clone <your-repository-url>
cd Berlin_House_Price_Prediction
```

## 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

## 3. Install Dependencies

```
pip install -r requirements.txt
```

## 4. Run the Pipeline

```
python main.py
```

## 5. Run the Application

```
python app.py
```

---

# Pipeline Execution Flow

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

---

# Design Philosophy

This project follows:

* Modular ML architecture
* Config-driven pipeline
* Clean code structure
* Reproducible experiments
* Industry-style workflow

Each stage of the pipeline is independent and easy to extend.

---

# Future Improvements

Possible future upgrades:

* Feature engineering
* Hyperparameter tuning pipeline
* Cross-validation system
* Model tracking (MLflow)
* API deployment
* Docker support
* Cloud deployment
* Automated retraining pipeline

---

# Workflow Used in This Project

The development of this project follows this order:

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

This ensures a structured and scalable ML project workflow.
