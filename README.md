# ClaimSights ![image](https://github.com/Yasmin-9/Project-4-Group-5/assets/136015250/58cb8a22-2ca9-4add-a323-46eb023cbc25)
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

## Machine Modeling: Supervised learning
The most ideal model for this data type was random forest classifier as the data had binary and multiclass features with a large number of total features. To balance the distribution of the data sampling between the 'status' category, a ```class_weight``` hyperparameter was used to enhance the machines ability to predict more accurately. 

```RandomForestClassifier(class_weight={'Paid': 1, 'Rejected': 2}, min_samples_split=4, n_estimators=500, random_state=42)```

### Optimization: 
6 seperate optimization models were ran in order to increase the accuracy and scores of the classification report of the model:

1. Hypertuning the parameters
2. Setting class_weight to 'balanced' for proportioning
3. Utilizing SMOTE to oversample 'Rejected' class
4. Manually modifying class_weights
5. Combining SMOTE and TomkeLinks to oversample 'Rejected' class and undersample 'Paid' class for even distribution
6. Swapping a core feature, with an alternatively close but broader feature ('Diagnosis_Family')

Optimization #4 resulted in the best evaluation score of the model, with the following accuracy score:

```Accuracy:  0.7802148861548739```

#### Classification Report:

![image](https://github.com/Yasmin-9/Project-4-Group-5/assets/136015250/678e8285-fb55-4d18-8fbd-af85987d4133)

All scores for the 'Paid' are over 80%, implying the model predicted 80% of all True-Positives (refer to recall score), whereas the 'Rejected' class scored lower in comparison and only 68% in its recall score. This was expected as the distribution of data had more than twice as many instances of 'Paid' classes, leaving less sampling data for the model to train on for the latter class.

### Front-end Development
The site page's were developed using bootstrap frameworks for styling buttons and tooltips and other layouts. Along with other styling tools such as Google Font's, and CSS. Powered by Flask APP and rendering templates and using request to store user interactive input's, 

 
## Summary

