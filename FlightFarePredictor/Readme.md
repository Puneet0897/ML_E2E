# Flight Fare Predictor


## Overview
- The dataset consists of records for different airlines,travel routes,stops,sources,destination,date of journeyprice,etc.Price is the target variable.This dataset is present on kaggle.Please check [here](https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh/) for more details on dataset. 

- The train dataset has about 10682 records. The test dataset is a different file and you will have to test on that. 

## Motivation
- I like to travel a lot. So for this purpose I thought it would be better if try to analyse this data and make a model out of it just for academic purpose.

- As I am a traveller, I found this project interesting as I would analyse how different features affect the flight prices.

-  This model would give you approximate fare value and not the exact!

## Project Structure
- [main.py](https://github.com/Puneet0897/ML_E2E/blob/250de5702cf549f57caeaf9811f06d47a75fae78/FlightFarePredictor/main.py) : This file has the flask application which is created.

- [utils.py](https://github.com/Puneet0897/ML_E2E/blob/250de5702cf549f57caeaf9811f06d47a75fae78/FlightFarePredictor/utils.py) : This file has all the helper functions which are required to run the application.

- [constants.py](https://github.com/Puneet0897/ML_E2E/blob/250de5702cf549f57caeaf9811f06d47a75fae78/FlightFarePredictor/constants.py) : This file has all the constant variables required in developing the application.

- [templates](https://github.com/Puneet0897/ML_E2E/tree/250de5702cf549f57caeaf9811f06d47a75fae78/FlightFarePredictor/templates) : This folder has all the templates which are rendered in the application

- [readme_resources](https://github.com/Puneet0897/ML_E2E/tree/250de5702cf549f57caeaf9811f06d47a75fae78/FlightFarePredictor/readme_resources) : This folder has all the images used to create readme file.

- [requirements.txt](https://github.com/Puneet0897/ML_E2E/blob/250de5702cf549f57caeaf9811f06d47a75fae78/FlightFarePredictor/requirements.txt) : This file has all the packages used to code and build the application.

- [Flight Fare Prediction.ipynb](https://github.com/Puneet0897/ML_E2E/blob/250de5702cf549f57caeaf9811f06d47a75fae78/FlightFarePredictor/Flight%20Fare%20Prediction.ipynb) : This jupyter notebook has the code for making models.

## Problem Objective
- To build a model which predict the prices of flight using a dataset

## Methodology

### EDA (Exploratory Data Analysis)
- I have plotted various graphs to visualize the data. Some of them are as follows : 

![PriceVsAirline](https://github.com/Puneet0897/ML_E2E/blob/250de5702cf549f57caeaf9811f06d47a75fae78/FlightFarePredictor/readme_resources/AirlineVsPrice.png)
![PriceVsDest](https://github.com/Puneet0897/ML_E2E/blob/250de5702cf549f57caeaf9811f06d47a75fae78/FlightFarePredictor/readme_resources/DestinationVsPrice.png)
![PriceVsSource](https://github.com/Puneet0897/ML_E2E/blob/250de5702cf549f57caeaf9811f06d47a75fae78/FlightFarePredictor/readme_resources/SourceVsPrice.png)
![PriceVsStops](https://github.com/Puneet0897/ML_E2E/blob/250de5702cf549f57caeaf9811f06d47a75fae78/FlightFarePredictor/readme_resources/StopsVsPrice.png)

- Required Graphs are plotted using seaborn,matplotlib libraries.

- Also heatmap is plotted for checking the corelation between target and predictor variables.
![Heatmap](https://github.com/Puneet0897/ML_E2E/blob/250de5702cf549f57caeaf9811f06d47a75fae78/FlightFarePredictor/readme_resources/heatmap.png)

### Feature Engineering
- I have derived many useful features from existing features so that I can use them in my model. You can check the notebook attached.

- I have handled categorical variables i.e nominal ar well as ordinal by using one-hot-encoding and label encoding whereever necessary.

### Feature Selection
- I have used ExtraTreesRegressor for checking feature importances.

- I have also used barplot for visualising them:
![Feature_Imp](https://github.com/Puneet0897/ML_E2E/blob/250de5702cf549f57caeaf9811f06d47a75fae78/FlightFarePredictor/readme_resources/feature%20importances.png)

### Model Making

- I have built a RandomForestRegressor model with default hyperparameters initially.

- I chose this model just because I thought ensemble model would work better. But you can try different models too.

### Hyper-Parameter Tuning

- I have tuned the hyperparameters 'n_estimators', 'max_depth', 'max_features' by using RandomisedSearchCV. I used  this because this works faster than GridSearchCV.

- I again built a RF model with best hyper-parameters selected from CV.

### Metrics

- I have used 'r2_score' as my metric here. You can use any different metric for regression.

- Further I have plotted and checked error terms also to check whether they are normally distributed around 0.

### DATA SOURCE
- [Flight Fare Dataset](https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh/)

### Notebook
- [Flight Fare Predictor](https://github.com/Puneet0897/ML_E2E/blob/250de5702cf549f57caeaf9811f06d47a75fae78/FlightFarePredictor/Flight%20Fare%20Prediction.ipynb)

### Built with 🛠️
- Packages/Repo : Pandas,Numpy,Seaborn,Matplotlib,Sklearn,Flask,Pickle,Git

- Dataset : Kaggle

- Coded on : Jupter Notebook (modelling), VSCode(building application)


