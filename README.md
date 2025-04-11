# Forest Fires Dataset

A comprehensive dataset containing meteorological and spatial data about forest fires from the Montesinho Natural Park in the northeast region of Portugal. The dataset was created by Paulo Cortez and Aníbal Morais (2007).

## Dataset Description

The dataset contains 517 instances of forest fire records from the Montesinho Natural Park. Each record includes spatial, temporal, and weather-related features along with the burned area of the forest.

### Features Description

1. **Spatial Features**
   - **X** (1 to 9): x-axis spatial coordinate within the park map
   - **Y** (2 to 9): y-axis spatial coordinate within the park map

2. **Temporal Features**
   - **month** (jan to dec): Month of the year
   - **day** (mon to sun): Day of the week

3. **FWI (Fire Weather Index) Components**
   - **FFMC** (18.7 to 96.20): Fine Fuel Moisture Code
   - **DMC** (1.1 to 291.3): Duff Moisture Code
   - **DC** (7.9 to 860.6): Drought Code
   - **ISI** (0.0 to 56.10): Initial Spread Index

4. **Weather Data**
   - **temp** (2.2 to 33.30): Temperature in Celsius degrees
   - **RH** (15.0 to 100): Relative humidity in %
   - **wind** (0.40 to 9.40): Wind speed in km/h
   - **rain** (0.0 to 6.4): Outside rain in mm/m2

5. **Target Variable**
   - **area** (0.00 to 1090.84): Burned area of the forest in hectares

## Data Formats

The dataset is available in two formats:
- CSV format: `data/forestfires.csv`
- JSON format: `data/forestfires.json`

## Directory Structure

```
forest_fires/
├── data/
│   ├── forestfires.csv    # Dataset in CSV format
│   └── forestfires.json   # Dataset in JSON format
├── USAGE.md              # Detailed usage guide
└── README.md             # This file
```

## Basic Usage

### Loading the Data

```python
# Using CSV format
import pandas as pd
df = pd.read_csv('data/forestfires.csv')

# Using JSON format
df = pd.read_json('data/forestfires.json')
```

For more detailed usage examples and guidelines, please refer to [USAGE.md](USAGE.md).

## Data Statistics

- Number of instances: 517
- Number of attributes: 13 (12 features + 1 target)
- Missing values: None
- Feature types: 
  - Numerical: 10
  - Categorical: 2 (month, day)

## Citation

If you use this dataset in your research, please cite:

```
@article{cortez2007data,
  title={A data mining approach to predict forest fires using meteorological data},
  author={Cortez, Paulo and Morais, Aníbal},
  journal={Proceedings of the 13th Portuguese Conference on Artificial Intelligence},
  pages={512--523},
  year={2007},
  publisher={APPIA}
}
```

## References

- [UCI Machine Learning Repository - Forest Fires Dataset](https://archive.ics.uci.edu/ml/datasets/Forest+Fires)
- Cortez, P., & Morais, A. (2007). A Data Mining Approach to Predict Forest Fires using Meteorological Data.

## License

This dataset is provided by the UCI Machine Learning Repository and should be cited according to their terms. The data collection and organization scripts in this repository are licensed under the MIT License.
