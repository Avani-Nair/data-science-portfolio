# Healthcare Cost Classification

**Module:** Analysis of Data  
**Degree:** BSc (Hons) Data Science, University of Greenwich  
**Language:** R

## Overview

This project explored whether patients could be classified into high- or low-cost categories using healthcare-related variables.

The dataset contained **55,500 patient records** and was a synthetic healthcare dataset sourced from Kaggle.

## Methods

- Data cleaning and preparation
- Creation of a high/low cost target variable based on median billing amount
- 70/30 training and testing split
- Decision tree classification using `rpart`
- Decision tree visualisation using `rpart.plot`
- Model evaluation using a confusion matrix
- Accuracy, precision and recall

## Results

The decision tree identified **Medical Condition** as the main variable used for the first split.

The model was evaluated on the test set using a confusion matrix. The resulting accuracy was **49.8%**, with precision and recall also calculated for the two cost categories.

The project highlighted the importance of critically evaluating model performance and considering limitations of synthetic datasets.

## What I Learned

This project helped me develop my understanding of classification, target and predictor variables, training and testing data, decision trees and model evaluation in R.
