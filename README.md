# NYC Taxi Zones Visualization

[DEMO](https://zachpinto.com/projects/visualizations/nyc_taxi_video.mp4)

## Overview
This project visualizes the volume of taxi trips in New York City taxi zones by week from 2018 to 2022. 

## Features
- NYC Taxi Zones GeoJSON data via NYC Open Data for geographical data structures
- NYC Taxi volume data via NYC Open Data's API.
- Data processing and aggregation into a SQLite database.
- Dynamic visualization through time-lapse video generation.

## Getting Started
### Prerequisites
- Python 3.8+
- PostgreSQL
- Libraries: Pandas, Folium, Selenium, MoviePy

### Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/zachpinto/nyc-taxi-zones.git
cd nyc-taxi-zones
pip install -r requirements.txt
```

## Usage

### Data Collection
Run the data collection scripts for each year:
```bash
python src/data/2018.py
python src/data/2019.py
python src/data/2020.py
python src/data/2021.py
python src/data/2022.py
```
### Data Processing
Merge yearly data and aggregate it using the provided scripts:
```bash
python src/data/merge_data.py
psql -d your_database -f src/data/aggregate.sql
```

### Visualization
Generate and capture the map visualizations, then compile them into a time-lapse video:
```bash
python src/visualization/visualize.py
python src/visualization/maps_screenshots_test.py # OPTIONAL
python src/visualization/maps_screenshots_selenium.py
python src/visualization/maps_screenshot_finish.py
python src/visualization/maps_merged_movie.py
python src/visualization/edit_merged_video.py
python src/visualization/matplotlib_spectrum.py
python src/visualization/overlay_matplotlib_spectrum_on_mp4.py
python src/visualization/year_week_overlays.py
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- NYC Open Data for providing the taxi trip and GeoJSON data.

## Directory Structure

```plaintext
nyc-taxi-zones/
│
├── data/
│   ├── external/       # GeoJSON files and external datasets
│   ├── interim/        # Intermediate data processing files
│   ├── processed/      # Processed data ready for visualization
│   └── raw/           # Raw data from NYC Open Data API
├── docs/               # Documentation files and project notes
├── reports/            # Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures/        # Generated graphics and figures to be used in reporting
├── src/                # Source code for use in this project
│   ├── __init__.py     # Makes src a Python module
│   ├── data/           # Scripts to download or generate data
│   ├── features/       # Scripts to turn raw data into features for modeling
│   ├── models/         # Scripts to train models and then use trained models to make predictions
│   └── visualization/  # Scripts to create exploratory and results oriented visualizations
├── LICENSE             # The full license description
├── Makefile            # Makefile with commands like `make data` or `make train`
├── README.md           # The top-level README for developers using this project
├── requirements.txt    # The requirements file for reproducing the analysis environment
├── setup.py            # Makes project pip installable (pip install -e .) so src can be imported
├── test_environment.py # Test python environment is set-up correctly
└── tox.ini             # tox file with settings for running tox; see tox.readthedocs.io

