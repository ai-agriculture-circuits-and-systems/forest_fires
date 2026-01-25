# Forest Fires Dataset

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-green?logo=creativecommons&logoColor=white)](https://creativecommons.org/licenses/by/4.0/)
[![Version](https://img.shields.io/badge/version-1.0.0-blue?logo=semver&logoColor=white)](https://github.com/your-repo/forest_fires)
[![GitHub stars](https://img.shields.io/github/stars/your-repo/forest_fires?style=flat&logo=github&label=Stars&color=orange&labelColor=orange&logoColor=white)](https://github.com/your-repo/forest_fires)
[![GitHub forks](https://img.shields.io/github/forks/your-repo/forest_fires?style=flat&logo=github&label=Forks&color=yellow&labelColor=yellow&logoColor=white)](https://github.com/your-repo/forest_fires)
[![GitHub watchers](https://img.shields.io/github/watchers/your-repo/forest_fires?style=flat&logo=github&label=Watchers&color=cyan&labelColor=cyan&logoColor=white)](https://github.com/your-repo/forest_fires)
[![GitHub issues](https://img.shields.io/github/issues/your-repo/forest_fires?style=flat&logo=github&label=Issues&color=red&labelColor=red&logoColor=white)](https://github.com/your-repo/forest_fires/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/your-repo/forest_fires?style=flat&logo=github&label=PRs&color=lime&labelColor=lime&logoColor=white)](https://github.com/your-repo/forest_fires/pulls)
[![GitHub contributors](https://img.shields.io/github/contributors/your-repo/forest_fires?style=flat&logo=github&label=Contributors&color=purple&labelColor=purple&logoColor=white)](https://github.com/your-repo/forest_fires/graphs/contributors)
[![GitHub last commit](https://img.shields.io/github/last-commit/your-repo/forest_fires?style=flat&logo=github&label=Last%20Commit&color=gray&labelColor=gray&logoColor=white)](https://github.com/your-repo/forest_fires/commits)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.xxxxx-indigo?logo=doi&logoColor=white)](https://doi.org/10.5281/zenodo.xxxxx)

A comprehensive dataset containing meteorological and spatial data about forest fires from the Montesinho Natural Park in the northeast region of Portugal, collected and organized for machine learning and data mining research in agricultural and environmental applications.

- **Project page**: `https://archive.ics.uci.edu/ml/datasets/Forest+Fires`
- **Original paper**: `A Data Mining Approach to Predict Forest Fires using Meteorological Data`
- **Dataset repository**: `https://archive.ics.uci.edu/ml/datasets/Forest+Fires`

## TL;DR

- **Task**: Regression (forest fire burned area prediction)
- **Modality**: Tabular data (meteorological and spatial features)
- **Platform**: Field measurements
- **Real/Synthetic**: Real
- **Samples**: 517 forest fire records
- **Features**: 12 features (spatial, temporal, FWI components, weather data)
- **Target**: Burned area in hectares (0.00 to 1090.84)
- **Format**: CSV and JSON
- **License**: CC BY 4.0 (see LICENSE)
- **Citation**: See below

## Table of Contents

- [Download](#download)
- [Dataset Structure](#dataset-structure)
- [Data Schema](#data-schema)
- [Stats and Splits](#stats-and-splits)
- [Quick Start](#quick-start)
- [Evaluation and Baselines](#evaluation-and-baselines)
- [Datasheet (Data Card)](#datasheet-data-card)
- [Known Issues and Caveats](#known-issues-and-caveats)
- [License](#license)
- [Citation](#citation)
- [Changelog](#changelog)
- [Contact](#contact)

## Download

- **Original dataset**: `https://archive.ics.uci.edu/ml/datasets/Forest+Fires`
- **This repository**: Hosts standardized data formats (CSV and JSON) and conversion scripts
- **Local license file**: See `LICENSE` (CC BY 4.0).

## Dataset Structure

```
forest_fires/
├── data/
│   ├── forestfires.csv    # Dataset in CSV format
│   └── forestfires.json   # Dataset in JSON format
├── USAGE.md              # Detailed usage guide
├── convert_to_json.py    # CSV to JSON conversion utility
├── LICENSE               # MIT License
└── README.md             # This file
```

## Data Schema

### Spatial Features
- **X** (1 to 9): x-axis spatial coordinate within the park map
- **Y** (2 to 9): y-axis spatial coordinate within the park map

### Temporal Features
- **month** (jan to dec): Month of the year
- **day** (mon to sun): Day of the week

### FWI (Fire Weather Index) Components
- **FFMC** (18.7 to 96.20): Fine Fuel Moisture Code
- **DMC** (1.1 to 291.3): Duff Moisture Code
- **DC** (7.9 to 860.6): Drought Code
- **ISI** (0.0 to 56.10): Initial Spread Index

### Weather Data
- **temp** (2.2 to 33.30): Temperature in Celsius degrees
- **RH** (15.0 to 100): Relative humidity in %
- **wind** (0.40 to 9.40): Wind speed in km/h
- **rain** (0.0 to 6.4): Outside rain in mm/m2

### Target Variable
- **area** (0.00 to 1090.84): Burned area of the forest in hectares

## Stats and Splits

- **Total samples**: 517 forest fire records
- **Number of features**: 12 (spatial, temporal, FWI components, weather data)
- **Target variable**: 1 (burned area in hectares)
- **Missing values**: None
- **Feature types**:
  - Numerical: 10 features
  - Categorical: 2 features (month, day)
- **Data formats**: CSV and JSON formats available

## Quick Start

### Loading the Data

```python
import pandas as pd
import json

# Using CSV format
df = pd.read_csv('data/forestfires.csv')

# Using JSON format
with open('data/forestfires.json', 'r') as f:
    data = json.load(f)
    df = pd.DataFrame(data)
```

### Converting CSV to JSON

If you need to regenerate JSON from CSV:

```bash
python convert_to_json.py
```

### Dependencies

**Required**:
- `pandas>=1.5.0` (for data manipulation)

Install with:
```bash
pip install pandas
```

For more detailed usage examples and guidelines, please refer to [USAGE.md](USAGE.md).

## Evaluation and Baselines

- **Primary metric**: Mean squared error (MSE) or mean absolute error (MAE) for regression
- **Baseline results**: See original paper for baseline results using data mining approaches.

## Datasheet (Data Card)

### Motivation

This dataset was created to support research in forest fire prediction using meteorological data, which is crucial for fire prevention and management in forested areas.

### Composition

The dataset consists of:
- **Data types**: Tabular data with meteorological and spatial features
- **Samples**: 517 forest fire records from Montesinho Natural Park, Portugal
- **Features**: 12 features (spatial coordinates, temporal data, FWI components, weather measurements)
- **Target**: Burned area in hectares (regression task)

### Collection Process

- **Source**: Montesinho Natural Park in the northeast region of Portugal
- **Collection method**: Field measurements and meteorological data collection
- **Authors**: Paulo Cortez and Aníbal Morais (2007)
- **Validation**: Data validated and published in UCI Machine Learning Repository

### Preprocessing

- Data organized in standardized CSV and JSON formats
- No missing values in the dataset
- Features include both numerical and categorical variables

### Distribution

- Dataset is available from UCI Machine Learning Repository
- Dataset is distributed under CC BY 4.0 license
- This repository provides standardized formats and conversion utilities

### Maintenance

- Dataset structure has been standardized
- Conversion utilities provided for format transformations
- Original data preserved from UCI repository

## Known Issues and Caveats

- **Target variable distribution**: The burned area has a highly skewed distribution, with many small fires and few large fires
- **Categorical encoding**: Month and day features are categorical and may need encoding for machine learning models
- **Feature scaling**: Numerical features have different scales and may benefit from normalization
- **Data source**: Original data from UCI Machine Learning Repository; cite according to their terms

## License

This dataset is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

This dataset is provided by the UCI Machine Learning Repository and should be cited according to their terms.

See `LICENSE` file for full license text.

## Citation

If you use this dataset in your research, please cite:

```bibtex
@article{cortez2007data,
  title={A data mining approach to predict forest fires using meteorological data},
  author={Cortez, Paulo and Morais, Aníbal},
  journal={Proceedings of the 13th Portuguese Conference on Artificial Intelligence},
  pages={512--523},
  year={2007},
  publisher={APPIA}
}
```

## Changelog

- **V1.0.0** (2025): Initial standardized structure and JSON conversion utility

## Contact

- **Maintainers**: (to be added)
- **Original authors**: Paulo Cortez, Aníbal Morais
- **Institution**: University of Minho, Portugal
- **Source**: `https://archive.ics.uci.edu/ml/datasets/Forest+Fires`
