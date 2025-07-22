# us_old_vhicalprice_prediction
🚗Vehicle Price Prediction – Machine Learning Project ,Project Objective  This project aims to build a machine learning model that predicts the selling price of used vehicles based on features like year, condition, mileage (odometer), fuel type, and more. The model is designed to help buyers and sellers estimate the fair market price of vhicalr

# 🚗 Vehicle Price Prediction using XGBoost

## 📌 Project Objective

This project focuses on building a **machine learning model** to predict the **selling price of used vehicles** based on features such as manufacturing year, vehicle condition, mileage, fuel type, brand, and more. The goal is to provide accurate price estimates to assist buyers, sellers, and resellers in making informed decisions.

---

## 📂 Dataset Overview

The dataset was sourced from a used vehicle listing platform and includes features such as:

- `year`: Year of manufacture  
- `condition`: Condition of the vehicle (e.g., Excellent, Good, Fair)  
- `odometer`: Mileage driven  
  - `seller`: name of seller 
- `make`: Vehicle manufacturer  
- `model`: Vehicle model  
- `state`: Location of the listing  
- `sellingprice`: **Target variable** (price to predict)

---

## 🧹 Data Preprocessing

- Handled **missing values** appropriately (dropped or imputed).
- Applied **LabelEncoder** or **OneHotEncoder** to categorical columns.
- Used **StandardScaler** on numerical columns like `odometer`.
- Transformed the target variable `sellingprice` using **log1p** or **PowerTransformer** to reduce skewness.
- Dropped irrelevant columns such as `VIN`,`trim`,`seller`

---

## 🧠 Feature Engineering

- transform columns such as `make`, `model`, and `state` to form a single text-based feature: `changed_features`.

- Created reusable **pipelines** to keep preprocessing and modeling clean and modular.

---

## 🧪 Cross-Validation Strategy

Used **K-Fold Cross-Validation (k=5)** instead of a simple train-test split to improve generalization and ensure model stability across different splits.

---

## 🔁 Pipeline Creation

Used Scikit-learn's `Pipeline` to chain preprocessing steps and the model together.  
Pipeline included:
- `OneHotEncoder` for categorical columns  
- `StandardScaler` for numeric columns  
- `FunctionTransformer(np.log1p)` for the target  
- `XGBoostRegressor` as the final estimator

---

## 🤖 Model Used: XGBoost Regressor
📊 Model Evaluation
After tuning, the best model was XGBoostRegressor, which achieved the following metrics:

✅ R² Score: ~0.93

✅ RMSE: ~0.27

✅ MAE: ~0.19

These metrics show that the model performs exceptionally well in predicting used vehicle prices.

Chose **XGBoostRegressor** for its speed, performance, and ability to handle non-linear relationships.

### 🔍 Hyperparameter Tuning

Used **RandomizedSearchCV** to efficiently search through combinations of hyperparameters instead of `GridSearchCV` (which was slow due to high data volume).

```python
from xgboost import XGBRegressor
from sklearn.model_selection import RandomizedSearchCV

xgb_model = XGBRegressor(random_state=42)

param_dist = {
    "n_estimators": [100, 200, 300],
    "learning_rate": [0.01, 0.05, 0.1, 0.2],
    "max_depth": [3, 5, 7, 10],
    "subsample": [0.7, 0.8, 1.0],
    "colsample_bytree": [0.7, 0.9, 1.0]
}

random_search = RandomizedSearchCV(
    estimator=xgb_model,
    param_distributions=param_dist,
    n_iter=20,
    scoring='neg_root_mean_squared_error',
    cv=5,
    verbose=2,
    random_state=42,
    n_jobs=-1
)

random_search.fit(X, y)

