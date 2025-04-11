# Forest Fires Dataset Usage Guide

This guide explains how to use the Forest Fires dataset from the Montesinho Natural Park in Portugal. The dataset is designed for predicting the burned area of forest fires using meteorological and spatial data.

## Dataset Overview

The dataset contains 517 instances of forest fire records with 13 attributes, making it suitable for:
- Regression analysis to predict burned areas
- Environmental impact studies
- Fire prevention planning
- Machine learning model development

## Data Format

The data is available in two formats:
- CSV format: `data/forestfires.csv`
- JSON format: `data/forestfires.json`

### Data Structure

Each record contains the following fields:

```json
{
  "X": 1-9 (int),           // X-axis spatial coordinate
  "Y": 2-9 (int),           // Y-axis spatial coordinate
  "month": "jan-dec" (str), // Month of the year
  "day": "mon-sun" (str),   // Day of the week
  "FFMC": 18.7-96.20 (float), // Fine Fuel Moisture Code
  "DMC": 1.1-291.3 (float),   // Duff Moisture Code
  "DC": 7.9-860.6 (float),    // Drought Code
  "ISI": 0.0-56.10 (float),   // Initial Spread Index
  "temp": 2.2-33.30 (float),  // Temperature in Celsius
  "RH": 15.0-100 (float),     // Relative Humidity in %
  "wind": 0.40-9.40 (float),  // Wind speed in km/h
  "rain": 0.0-6.4 (float),    // Rain in mm/m2
  "area": 0.00-1090.84 (float) // Burned area in hectares (target variable)
}
```

## Common Use Cases

1. **Fire Area Prediction**
   - Predict the burned area size based on weather conditions and spatial data
   - Useful for fire management and resource allocation

2. **Risk Assessment**
   - Analyze patterns between weather conditions and fire occurrence
   - Identify high-risk conditions and areas

3. **Weather Impact Analysis**
   - Study the relationship between meteorological factors and fire spread
   - Understand which weather conditions contribute most to fire intensity

## Example Code Snippets

### Python with Pandas

```python
import pandas as pd
import numpy as np

# Load the data
df = pd.read_json('data/forestfires.json')
# or
df = pd.read_csv('data/forestfires.csv')

# Basic preprocessing
# Log transform the target variable (area) due to its skewed distribution
df['log_area'] = np.log1p(df['area'])

# Split features and target
X = df.drop(['area', 'log_area'], axis=1)
y = df['log_area']

# Convert categorical variables
X = pd.get_dummies(X, columns=['month', 'day'])
```

### Feature Importance Analysis

```python
from sklearn.ensemble import RandomForestRegressor

# Train a random forest model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X, y)

# Get feature importance
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=False)
```

## Best Practices

1. **Data Preprocessing**
   - Handle missing values (though this dataset is complete)
   - Scale numerical features
   - Encode categorical variables (month and day)
   - Apply log transformation to the target variable (area) due to its skewed distribution

2. **Model Selection**
   - For regression tasks, start with:
     - Support Vector Regression (best performer in original research)
     - Random Forest Regression
     - Gradient Boosting Regression

3. **Evaluation Metrics**
   - Mean Absolute Deviation (MAD)
   - Root Mean Square Error (RMSE)
   - R-squared score
   - Consider using cross-validation due to the dataset's size

## Research Findings

According to the original research by Cortez and Morais (2007):
- Best results were achieved using only 4 weather variables (temp, RH, wind, rain)
- Gaussian SVM achieved MAD of 12.71
- Models perform better on smaller fires, which are more common
- The dataset exhibits high skewness in the target variable

## Tips for Model Development

1. **Feature Engineering**
   - Create interaction terms between weather variables
   - Consider seasonal features from month information
   - Calculate fire danger indices from weather variables

2. **Validation Strategy**
   - Use k-fold cross-validation
   - Consider temporal splits if working with time-series aspects
   - Stratify based on fire size ranges

3. **Model Interpretability**
   - Use SHAP values or LIME for explaining predictions
   - Analyze feature importance
   - Consider partial dependence plots

## References

For more detailed information, refer to:
- Original paper: Cortez and Morais (2007) "A Data Mining Approach to Predict Forest Fires using Meteorological Data"
- [UCI Machine Learning Repository - Forest Fires Dataset](https://archive.ics.uci.edu/ml/datasets/Forest+Fires) 