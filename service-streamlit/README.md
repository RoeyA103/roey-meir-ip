# Streamlit Minikube App

A simple Streamlit application that demonstrates basic data visualization with random data. This app generates and displays line charts, bar charts, and an interactive map.

## Features

- **Line Chart**: Visualize three columns of random numerical data in a line chart format
- **Bar Chart**: Display random data from a single column as a bar chart
- **Interactive Map**: View randomly generated geographic coordinates on an interactive map (centered around coordinates 32.09°N, 34.82°E)
- **Raw Data Viewer**: Expandable section to inspect the underlying dataset

## Requirements

- Python 3.7+
- Dependencies listed in `requirements.txt`

Key dependencies:
- `streamlit==1.52.1` - Web app framework
- `pandas==2.3.3` - Data manipulation
- `numpy==2.3.5` - Numerical computing
- `pydeck==0.9.1` - Map visualization

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application with:
```bash
streamlit run main.py
```

The app will start a local web server and open in your default browser (typically at `http://localhost:8501`).

## Project Structure

```
streamlit_minikube_app/
├── main.py           # Main Streamlit application
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## How It Works

The application:
1. Generates 100 rows of random data across 3 columns (a, b, c)
2. Displays the raw data in an expandable section
3. Creates a line chart showing all three columns
4. Creates a bar chart showing only column "a"
5. Generates 50 random geographic coordinates and displays them on an interactive map

## Notes

- All data is generated randomly on each run - no persistent data is stored
- The map is centered around coordinates (32.09°N, 34.82°E) with random offsets
- The application requires an internet connection for the map visualization to work properly
