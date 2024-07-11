import streamlit as st
import pandas as pd

# Configuring the page
st.set_page_config(page_title="Miami-Dade Traffic Analysis", layout="wide", initial_sidebar_state="expanded")

# CSS for dark theme
st.markdown(
    """
    <style>
    .reportview-container {
        background: #111;
        color: #fff;
    }
    .sidebar .sidebar-content {
        background: #222;
        color: #fff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar for navigation
st.sidebar.title("Miami-Dade Traffic Analysis")
st.sidebar.subheader("Sharief Reid, Jonathan Obas")
st.sidebar.markdown("Mentor: Dr. Juan Caraces-Mancilla")
sections = ["Abstract", "Introduction", "Goals", "Objectives", "Motivations", "Prior Art & Challenges", "Data Sources", "Tools & Implementation", "Results", "Contributions & Conclusions"]
choice = st.sidebar.radio("Navigation", sections)

# Content for each section
if choice == "Abstract":
    st.title("Miami-Dade Traffic Analysis")
    st.header("Abstract")
    st.write("""
    Miami's growing population and vehicle count have led to significant infrastructure challenges, including increased traffic congestion, longer commutes, higher fuel consumption, and more accidents. 
    This study examines the relationship between bus routes and traffic incidents in Miami, aiming to optimize bus routes to reduce congestion and improve road safety. By analyzing spatial traffic data, the research provides actionable insights for decision-makers. 
    Utilizing machine learning, we develop an interpretable predictive model that incorporates traffic signals, bus routes, historical traffic counts, and street characteristics. 
    The model highlights key factors in predicting incident risks and provides visualizations of traffic incidents in relation to population density and public transportation coverage.
    This approach helps identify road segments needing more public transportation, supporting data-driven urban planning and enhancing overall safety and efficiency.
    """)

elif choice == "Introduction":
    st.header("Introduction")
    st.write("""
    As Miami continues to grow, the city’s infrastructure struggles to keep pace with the rising population and vehicle count. Traffic congestion has become a daily challenge, leading to longer commutes, higher fuel consumption, and increased accident rates. 
    These issues underscore the urgent need for effective solutions to improve urban mobility and safety. Public transportation plays a pivotal role in reducing traffic congestion by offering a viable alternative to personal vehicle usage. 
    However, gaps in the existing public transportation network limit its effectiveness. Addressing these gaps is essential to enhance the efficiency of the transportation system and improve overall urban mobility.
    This research aims to investigate the relationship between bus routes and traffic incidents in Miami, with a focus on identifying how optimizing bus routes can alleviate congestion and enhance road safety. 
    By analyzing spatial traffic data, we seek to provide actionable insights for decision makers. The findings of this research will contribute to the academic understanding of urban mobility and provide data-driven recommendations for optimizing public transportation routes. 
    These insights will not only help reduce traffic congestion but also improve the safety and quality of life for residents of Miami.
    """)

elif choice == "Goals":
    st.header("Goals")
    st.write("""
    Within the scope of model application and use cases, we have two goals: Develop an explainable predictive model and provide insights for decision makers. Using machine learning techniques, we want to build a model that incorporates various data points such as number of traffic signals and bus routes, historical traffic counts, and other street characteristics. 
    We want to ensure that the model outputs are interpretable, highlighting the significance of each factor in predicting incident risks. 
    Also, we strive to provide clear visualizations and reports illustrating the correlation between traffic incidents and factors such as population density and public transportation coverage.
    Regarding the scope of city planning, we anticipate being able to enhance public transportation planning and support data-driven urban planning. Stakeholders will be able to use the predictive model to pinpoint road segments that would benefit most from increased public transportation options by assessing current bus route coverage and identifying gaps where new routes could alleviate traffic congestion and improve safety. 
    We can support data-driven decision making by integrating various datasets – including incidents, road characteristics, historical traffic counts, and bus routes – into a comprehensive analysis framework. 
    This framework can be used to validate urban planning, ensuring that data insights are systematically used to inform policy and project development.
    """)

elif choice == "Objectives":
    st.header("Objectives")
    st.write("""
    The primary objectives of this research are:
    1. To analyze the correlation between the number of bus routes and the frequency of traffic incidents on various road segments.
    2. To identify road segments that are prone to traffic congestion and accidents and currently lack sufficient public transportation options.
    3. To develop a model that recommends optimal locations for introducing additional bus routes to enhance urban mobility and safety.
    4. Identify factors that heavily impact the classification of an incident as probable (1) or unlikely (0).
    The main deliverable for this project is a completed classification model that can classify a traffic incident under one of two classes: certain or unlikely. 
    This model could then be used to help city officials and other stakeholders pinpoint areas of congestion and determining where additional bus routes are needed to mitigate the risk of incidents.
    """)

elif choice == "Motivations":
    st.header("Motivations")
    st.write("""
    The motivation for this project stems from the pressing need to address traffic congestion and accident rates in urban areas, particularly in Miami. 
    As the population continues to grow, the existing infrastructure faces increasing strain, leading to longer commute times, higher fuel consumption, and a rise in traffic-related incidents. 
    Public transportation, especially bus routes, plays a crucial role in alleviating these issues by offering an alternative to personal vehicle use. 
    However, there are gaps in the current public transportation network that need to be identified and addressed.
    By analyzing the correlation between bus routes and traffic incidents, we aim to provide urban planners and city officials with data-driven insights to optimize bus routes, improve traffic flow, and enhance overall safety. 
    This project not only seeks to contribute to the academic understanding of urban mobility but also aims to have a tangible impact on the quality of life for residents in Miami.
    """)

elif choice == "Prior Art & Challenges":
    st.header("Prior Art & Challenges")
    st.write("""
    There have been previous studies that have explored various aspects of traffic congestion and public transportation efficiency, yet significant gaps remain in understanding the relationship between bus routes and traffic incidents. 
    For instance, while some research has focused on optimizing bus schedules and routes to reduce delays, it often lacks a comprehensive analysis that includes traffic incident data. 
    Other studies have examined traffic congestion patterns but unfortunately didn't adequately consider the role of public transportation.
    One of the primary challenges in our project is the integration of diverse datasets from multiple sources, such as TomTom Traffic APIs, Miami-Dade County, and FDOT. 
    Ensuring data consistency between sources, handling missing values, and accurately spatially merging these datasets were complex tasks that took most of our time. 
    Additionally, developing a classification model that can reliably predict traffic incidents while being interpretable to decision-makers was another significant challenge we had to consider. 
    However, we understood that overcoming these obstacles was crucial for providing actionable insights that can lead to effective interventions in urban mobility planning.
    """)

elif choice == "Data Sources":
    st.header("Data Sources")
    st.write("""
    The data used in this study comes from multiple sources, including the TomTom Traffic APIs, Miami-Dade County (MDC) datasets, and the Florida Department of Transportation (FDOT).
    The table below outlines the merged features, record count, and source for each dataset:
    """)

    data_sources = {
        "Dataset": ["Incident Details", "Traffic Flow", "Traffic Signals", "Bus Routes", "Street Maintenance", "County Zoning", "Tract 2020 (Census)", "2023 Avg Annual Daily Traffic (AADT)"],
        "Source": ["TomTom", "TomTom", "MDC", "MDC", "MDC", "MDC", "MDC", "FDOT"],
        "Merged Features": ["magnitudeOfDelay, description, startTime, geometry, from, to, length, probabilityOfOccurrence", "freeFlowSpeed, freeFlowTravelTime", "AssetID", "LINENAME", "SPEEDLIMIT, LANES, ST_WIDTH", "ZONE_DESC", "AREALAND, POP100", "AADT"],
        "Number of Records": [6666, 6666, 5, 106, 114919, 3984, 707, 100893]
    }

    df_data_sources = pd.DataFrame(data_sources)
    st.table(df_data_sources)

elif choice == "Tools & Implementation":
    st.header("Tools & Implementation")
    st.write("""
    Tools
    All preprocessing, model building and model testing for this project were ran using Python 3.0 on Jupyter Notebook on a MacBook Air, running on a 1.1 GHz Quad-Core Intel Core i5 processor with 16 GB of RAM and 208 GB hard drive. 
    The following python libraries and data tools were utilized for preprocessing, exploratory data analysis, and model building and testing:
    - Geopandas 
    - NumPy
    - Matplotlib 
    - Pandas
    - QGIS
    - Scikit-learn
    - Seaborn 
    - Shapely

    Implementation
    The experimental approach is performed in four phases as shown in the following sections of the report.

    **Phase One: Data Collection and Preprocessing**
    - Collected initial incident data via TomTom API call.
    - Appended traffic flow speeds and travel times at the coordinates of the incident.
    - Spatially merged API data with GeoJSON data from the MDC and FDOT site using QGIS software.
    - Cleaned and transformed data to ensure completeness and consistency.

    **Phase Two: Exploratory Data Analysis**
    - Created correlation matrix to visualize relationships between features.
    - Analyzed relationships between incident count and other features such as traffic lights, bus routes, and annual average daily traffic count.

    **Phase Three: Model Building and Tuning**
    - Built classification models (Decision Tree, Random Forest, XGBoost).
    - Applied Synthetic Minority Over-sampling Technique (SMOTE) for class balancing.
    - Performed hyperparameter tuning to optimize model performance.

    **Phase Four: Results Analysis and Feature Importance**
    - Analyzed model performance and evaluated feature importance to gain insights into predictive power and interpretability.
    """)

elif choice == "Results":
    st.header("Results")
    st.write("""
    **Model Performance Analysis**
    The XGBoost model performed the best among the three models in terms of precision-recall trade-off, with the highest PR AUC score of 0.99260.

    **Feature Importance Analysis**
    Key factors contributing to traffic congestion and accidents were identified. Areas with a higher density of bus routes tend to have a lower incidence of traffic-related incidents, highlighting the critical role of public transportation in mitigating traffic congestion and enhancing urban safety.

    **Model Results**
    The table below shows the accuracies across training and test sets for different models:

    | Model       | Train Baseline | Test Baseline | Train SMOTE | Test SMOTE | Train Tuning | Test Tuning |
    |-------------|----------------|---------------|-------------|------------|--------------|-------------|
    | Decision Tree | 0.997075       | 0.984975      | 0.997037    | 0.971619   | 0.993534     | 0.964942    |
    | Random Forest | 0.997075       | 0.986644      | 0.997037    | 0.984975   | 0.996767     | 0.983306    |
    | XGBoost       | 0.997075       | 0.986644      | 0.997037    | 0.984975   | 0.996767     | 0.986644    |

    **Confusion Matrix for Random Forest Model**
    The confusion matrix for the Random Forest model demonstrates strong predictive performance, with a high number of true positives (1072) and true negatives (155), showcasing the model's classification reliability.

    """)
    # You can add visualizations for the confusion matrix and feature importance here

elif choice == "Contributions & Conclusions":
    st.header("Contributions & Conclusions")
    st.write("""
    **Contributions**
    - Sharief: Data collection & integration, preprocessing, exploratory data analysis, class balancing, stratified data split.
    - Jonathan: Chose and built classification models, tuned hyperparameters, analyzed model performance, refined models.

    **Conclusions**
    - Areas with a higher density of bus routes tend to have a lower incidence of traffic-related incidents.
    - Public transportation plays a crucial role in mitigating traffic congestion and enhancing urban safety.
    - The XGBoost model was identified as the most effective in predicting traffic incidents based on various factors.
    - Data-driven insights can significantly improve urban planning and policy development.

    **Bibliography**
    - David Schrank, Bill Eisele, and Tim Lomax. "2019 Urban Mobility Report." Texas A&M Transportation Institute, 2019.
    - Litman, Todd. "Evaluating Public Transportation Health Benefits." Victoria Transport Policy Institute, 2010.
    - "Public Transportation Accessibility and Mobility." SpringerLink, Springer.
    - "Improving Public Transportation Efficiency Through Accurate Bus Passenger Demand." SpringerLink, Springer.
    - "The Complexity of Integrating Multiple Traffic Data Sources." SpringerLink, Springer.
    """)

