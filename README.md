# Miami Public Transit Analysis

## Project Overview

Miami's growing population and vehicle count have led to significant infrastructure challenges, including increased traffic congestion, longer commutes, higher fuel consumption, and more accidents. This project aims to optimize public transit routes in Miami to reduce traffic congestion and enhance road safety by analyzing the relationship between bus routes and traffic incidents.

## Goals and Objectives

The main goals of this project are to:

1. Develop an interpretable predictive model that can identify high-risk traffic areas.
2. Provide actionable insights and visualizations for decision-makers in urban planning to enhance public transportation coverage and reduce congestion.
   
Key objectives include:

- Analyzing the correlation between bus routes and traffic incidents on various road segments.
- Developing a model that recommends optimal locations for introducing additional bus routes.
- Identifying factors that heavily impact the classification of a traffic incident as likely or unlikely.

## Motivation

The motivation for this project stems from the pressing need to address traffic congestion and accident rates in Miami. As the population continues to grow, there is an increasing strain on infrastructure, leading to longer commute times and a rise in traffic-related incidents. This project aims to provide urban planners and city officials with data-driven insights to optimize bus routes, improve traffic flow, and enhance overall safety.

## Data Sources

The datasets used in this project come from multiple sources, including:

- **TomTom Traffic APIs**: Provides data on traffic incidents and traffic flow speeds.
- **Miami-Dade County (MDC) Datasets**: Includes data on traffic signals, bus routes, street maintenance, county zoning, and US Census Tract boundaries.
- **Florida Department of Transportation (FDOT)**: Provides annual average daily traffic data.

## Tools and Implementation

The project was implemented using Python and various libraries, such as:

- **Geopandas**: For handling geographic data.
- **NumPy**: For numerical operations.
- **Matplotlib** and **Seaborn**: For data visualization.
- **Pandas**: For data manipulation and analysis.
- **QGIS**: For geospatial data processing.
- **Scikit-learn** and **XGBoost**: For machine learning model development.

The project is divided into four phases:

1. **Data Collection and Preprocessing**: Gathering and integrating data from various sources, followed by cleaning and feature engineering.
2. **Exploratory Data Analysis (EDA)**: Identifying correlations and visualizing data patterns.
3. **Model Selection and Refinement**: Building and tuning models using Decision Trees, Random Forests, and XGBoost to predict traffic incidents.
4. **Results and Analysis**: Evaluating model performance and identifying key features that impact traffic conditions.

## Installation Instructions

To run this project locally:

1. Clone the repository:
    ```bash
    git clone https://github.com/riefreid/Miami-Public-Transit-Analysis.git
    ```
2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Download and prepare the datasets as described in the `data` folder.

## Usage

1. Run the Jupyter Notebook `notebook.ipynb` to follow the data processing and modeling steps.
2. Use the scripts in the `src` folder to replicate or modify the analysis as needed.
3. Visualizations and model results can be found in the `results` folder.

## Contributors

- **Sharief Reid**: Data collection, preprocessing, exploratory data analysis, class balancing, and data splitting.
- **Jonathan Obas**: Model selection, hyperparameter tuning, model performance analysis, and feature importance analysis.
