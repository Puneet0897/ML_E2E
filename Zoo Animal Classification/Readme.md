# Zoo Animal Classification
## Overview
- This is a small dataset containing 101 animal records with their features and classes.Also a file with animals with respective classes which are present in zoo are mentioned.This dataset is present on kaggle.Please check [here](https://www.kaggle.com/uciml/zoo-animal-classification) for more details on dataset. 

## Motivation
- I love animals a lot. So I chose this dataset to understand how can we predict classes of animals based on their features

-  This model is trained on very less data. But this model would give you appropriate results.

## Project Structure
- [main.py](https://github.com/Puneet0897/ML_E2E/blob/54c1e57a9ee4142be044301003549c4082e35965/Zoo%20Animal%20Classification/main.py): This file has the flask application which is created.

- [utils.py](https://github.com/Puneet0897/ML_E2E/blob/54c1e57a9ee4142be044301003549c4082e35965/Zoo%20Animal%20Classification/utils.py) : This file has all the helper functions which are required to run the application.

- [constants.py](https://github.com/Puneet0897/ML_E2E/blob/54c1e57a9ee4142be044301003549c4082e35965/Zoo%20Animal%20Classification/constants.py) : This file has all the constant variables required in developing the application.

- [templates](https://github.com/Puneet0897/ML_E2E/tree/54c1e57a9ee4142be044301003549c4082e35965/Zoo%20Animal%20Classification/templates) : This folder has all the templates which are rendered in the application

- [requirements.txt](https://github.com/Puneet0897/ML_E2E/blob/54c1e57a9ee4142be044301003549c4082e35965/Zoo%20Animal%20Classification/requirements.txt) : This file has all the packages used to code and build the application.

- [AnimalClassClassifier.ipynb](https://github.com/Puneet0897/ML_E2E/blob/54c1e57a9ee4142be044301003549c4082e35965/Zoo%20Animal%20Classification/AnimalClassClassifier.ipynb) : This jupyter notebook has the code for making models.

## Problem Objective
- To build a model which can classify animals based on thier features.

## Methodology

### Feature Engineering
- This dataset is almost preprocessed already and hence no need to do feature engineering.

- The features are already one-hot encoded.

- This is an imbalanced dataset. Some of the animal classes have very few records. So I have handled then using weights. I have assigned weights to the classes by using Counts to Length Ratio. Check notebook for understanding about this.

### Feature Selection
- As there are very less number of features, I have used all of them to make model.

### Model Making

- I have built a RandomForestRegressor model with default hyperparameters.

- I chose this model just because I thought ensemble model would work better. But you can try different models too.

### Metrics

- I have used 'accuracy' as my metric here. You can use any different metric for classification.


### DATA SOURCE
- [Zoo Animal Classification Dataset](https://www.kaggle.com/uciml/zoo-animal-classification)

### Notebook
- [Animal Class Classifier](https://github.com/Pratik872/ML/blob/main/E2E%20Project/Zoo%20Animal%20Classification/AnimalClassClassifier.ipynb)

### Built with 🛠️
- Packages/Repo : Pandas,Numpy,Sklearn,Flask,Pickle,Git

- Dataset : Kaggle

- Coded on : Jupter Notebook (modelling), VSCode(building application)



