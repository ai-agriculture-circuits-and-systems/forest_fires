# Forest Fires Prediction

A machine learning project to predict the burned area of forest fires using meteorological and spatial data from the northeast region of Portugal (Montesinho park).

## Dataset Description

This project uses the Forest Fires dataset from the UCI Machine Learning Repository. The dataset contains 517 instances of forest fires recorded in the Montesinho park in Portugal, with the goal of predicting the burned area.

### Dataset Features

The dataset includes the following features:

1. **X** - x-axis spatial coordinate within the Montesinho park map: 1 to 9
2. **Y** - y-axis spatial coordinate within the Montesinho park map: 2 to 9
3. **month** - month of the year: 'jan' to 'dec'
4. **day** - day of the week: 'mon' to 'sun'
5. **FFMC** - Fine Fuel Moisture Code index from the FWI system: 18.7 to 96.20
6. **DMC** - Duff Moisture Code index from the FWI system: 1.1 to 291.3
7. **DC** - Drought Code index from the FWI system: 7.9 to 860.6
8. **ISI** - Initial Spread Index from the FWI system: 0.0 to 56.10
9. **temp** - temperature in Celsius degrees: 2.2 to 33.30
10. **RH** - relative humidity in %: 15.0 to 100
11. **wind** - wind speed in km/h: 0.40 to 9.40
12. **rain** - outside rain in mm/m2: 0.0 to 6.4
13. **area** - the burned area of the forest (in ha): 0.00 to 1090.84 (target variable)

The target variable `area` is highly skewed towards 0.0, which suggests that a logarithmic transformation might be appropriate for modeling purposes.

## Research Background

According to the original paper by Cortez and Morais (2007), the best prediction results were achieved by a Gaussian Support Vector Machine (SVM) using only 4 direct weather conditions (temperature, relative humidity, wind, and rain), which obtained a Mean Absolute Deviation (MAD) of 12.71.

The SVM model was particularly effective at predicting smaller fires, which constitute the majority of cases in the dataset.

## Project Structure

```
forest_fires/
├── data/
│   ├── forestfires.csv    # Raw dataset
│   └── forestfires.names  # Dataset description
├── models/               # Directory for trained models
├── notebooks/            # Jupyter notebooks for exploration and analysis
├── src/                  # Source code
└── README.md             # This file
```

## Getting Started

### Prerequisites

```
# Dependencies will be listed here
```

### Installation

```
# Installation instructions will be here
```

## Usage

```
# Usage examples will be here
```

## Model Performance

In the original study:

- The best MAD (Mean Absolute Deviation) value was 12.71 ± 0.01, achieved by a Gaussian SVM with only 4 weather variables.
- The best RMSE (Root Mean Square Error) was attained by a naive mean predictor.
- Analysis of the regression error curve (REC) showed that the SVM model predicts more examples within a lower admitted error, particularly for smaller fires.

## References

- Cortez, P., & Morais, A. (2007). A Data Mining Approach to Predict Forest Fires using Meteorological Data. In Proceedings of the 13th Portuguese Conference on Artificial Intelligence (EPIA 2007), 512-523. APPIA.
- [UCI Machine Learning Repository - Forest Fires Dataset](https://archive.ics.uci.edu/ml/datasets/Forest+Fires)
- [TensorFlow Datasets - Forest Fires](https://www.tensorflow.org/datasets/catalog/forest_fires)

## Acknowledgments

- Dua, D. and Graff, C. (2019). UCI Machine Learning Repository. Irvine, CA: University of California, School of Information and Computer Sciences.
- Paulo Cortez and Aníbal de Jesus Raimundo Morais for creating and sharing the original dataset. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. The dataset is provided by the UCI Machine Learning Repository and should be cited according to their terms.
