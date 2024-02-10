# ClaimSights
### Machine Learning Foresights into Health Insurance Claims

## Overview
ClaimSight's is a websited designed to predict whether a user's insurance claim is going to be accepted or rejected. The user input's their general data by selecting the corresponding options (Sex, Age, and Diagnosis Code) that queries the parameters via Flask which launches a query and fetches the prediction given by the machine learning model, and returns the binary result with a popup stating 'COVERED' and 'REJECTED' respectively. The site is powered by AWS.


## Exploratory Data Analysis: 
The dataset was provided by an insurance company with a confidentiality agreement, with the data spanning to over 250k rows. 

Data Cleaning : Using numpy, scipy.stat to reduce column clutter, correct datatypes and rid of null values. 'Diagnosis_Code' was binned into a broader code category 'Diagnosis_Group' for better machine training purposes later on. 

Data Analysis: Columns of interest were graphed using matplotlib, to assess general trends in data. 

Findings: 1) data was made up of nearly twice as many male's than females.
![image](https://github.com/Yasmin-9/Project-4-Group-5/assets/136015250/4965bde5-90c9-432a-bbe8-443a4fdb25c2)

          2) The age distribution was a normal bell curve from age's 0 - 100+, with the peak age group being between 30-50.
![image](https://github.com/Yasmin-9/Project-4-Group-5/assets/136015250/a789e502-952a-49ae-a8b4-71008a76b31d)

          3) the diagnosis group with highest frequency was I2, making over 25,000+ rows of data.
![image](https://github.com/Yasmin-9/Project-4-Group-5/assets/136015250/328536c7-828a-4ed1-a351-22a5377eefc7)

## ETL, and Data Preprocessing 
The database was loaded in using POSTGRES, connected to engine via SQL

## Machine Modeling: Unsupervised learning

to BE CONNTINUED
K_means model

Optimization: 


### Machine Results:
- add accuracy results
- 
#### Classification Report:

![image](https://github.com/Yasmin-9/Project-4-Group-5/assets/136015250/678e8285-fb55-4d18-8fbd-af85987d4133)


### Front-end Development
The site page's were developed using bootstrap frameworks for styling, with other styling tools such as Google Font's, and CSS. Powered by Flask APP and rendering templates and using request to store user interactive input's.

 
## Summary

