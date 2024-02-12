# ClaimSights ![image](https://github.com/Yasmin-9/Project-4-Group-5/assets/136015250/58cb8a22-2ca9-4add-a323-46eb023cbc25)
### Machine Learning Foresights into Health Insurance Claims

## Overview
ClaimSight is a website specifically created to forecast the likelihood of acceptance or rejection of an insurance claim submitted by a user. The process involves users inputting their general information, including sex, age, and diagnosis code, through the selection of corresponding options. These parameters are then queried via Flask, which initiates a request and retrieves predictions from a machine learning model. The outcome, presented as a binary result, is displayed to the user through a popup indicating either 'COVERED' or 'DENIED.' The  platform is hosted on AWS. 

## Exploratory Data Analysis: 
The dataset was provided by an insurance company with a confidentiality agreement, with the data spanning to over 250k rows. 

Data Cleaning : Using numpy, scipy.stat to reduce column clutter, correct datatypes and rid of null values. 'Diagnosis_Code' was binned into a broader code category 'Diagnosis_Group' for better machine training purposes later on. 

Data Analysis: Columns of interest were graphed using matplotlib, to assess general trends in data. 

Findings:
          
          1) data was made up of nearly twice as many male's than females.
![image](https://github.com/Yasmin-9/Project-4-Group-5/assets/136015250/4965bde5-90c9-432a-bbe8-443a4fdb25c2)

          2) The age distribution was a normal bell curve from age's 0 - 100+, with the peak age group being between 30-50.
![image](https://github.com/Yasmin-9/Project-4-Group-5/assets/136015250/a789e502-952a-49ae-a8b4-71008a76b31d)

          3) the diagnosis group with highest frequency was I2, making over 25,000+ rows of data.
![image](https://github.com/Yasmin-9/Project-4-Group-5/assets/136015250/328536c7-828a-4ed1-a351-22a5377eefc7)

## ETL, and Data Preprocessing 
The database was loaded in using POSTGRES, connected to engine via SQL. After the data was loaded, steps were taken to prepare data for machine training. 

- Replaced string values "Male" and "Female" to integers (0 and 1 respectively) 
- Applied standard scaling on relevant columns for consistency
- Two seperate encoding methods were applied to utilize it across various machine learning (ML) models for better optimization:
          - Dummy Data: Due to the nature of Diagnosis code's being multiclass and categorical, the                         Diagnosis_Group was dummified to make it usable in the ML model.
          - One hot encoding: This method was applied to 'Diagnosis_Family' as per the reason listed above

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

Insights: Optimization #4 resulted in the best evaluation score of the model, with the following score:
```Accuracy:  0.7802148861548739```. Repeated trialing showed that when utilizing the 'Diagnosis_Family' over 'Diagnosis_Group', the broader of the two features, produced results with lower accuracy and overall f1 scores inidicating a more distinctive feature was better off for a random forest classifier.

#### Classification Report of the Best Optimization Model (#4):

In the selected model, the 'Status' class was encoded to integers from ```['Paid', 'Rejected']``` to ```[1,2]``` setting the weights manually and the input columns were converted to strings. The changes were applied and trained to the model with.

![image](https://github.com/Yasmin-9/Project-4-Group-5/assets/136015250/678e8285-fb55-4d18-8fbd-af85987d4133)

All scores for the 'Paid' are over 80%, implying the model predicted 80% of all True-Positives (refer to recall score), whereas the 'Rejected' class scored lower in comparison and only 68% in its recall score. This was expected as the distribution of data had more than twice as many instances of 'Paid' classes, leaving less sampling data for the model to train on for the latter class.

### Front-end Development
HTML, JavaScript, Bootstrap, and CSS were fundamental to create a cohesive and user-friendly interface. Utilizing built-in HTML functions and Bootstrap frameworks to implement features like buttons, dropdowns and tooltips to assist or aid a user's experience. To maintain a consistent layout across different screens, CSS was employed , organizing styling within classes, ID's and div elements in the HTML structure. This approach ensured a seamless user experience regardless of the user's device, minimizing the impact of varying screen sizes on the site's design.

#### Flask & Front-End Connection
The user interactions on ClaimSights was linked to the ML model with flask, using request form from flask to create forms that retrieves the users submitted data and runs query in our machine model to get the prediction result of the insurance claim status, as either ‘APPROVED’ or ‘DENIED’. The results are then stored and loaded inside a new dataframe and sent back to the site essentially which triggers a response by the site by producing one of two possible predictions, in the form of the button pop up.

 
## Challenges and Conclusion
Several challenges were faced during the course of this project such as data inconsistency or maxed out computer efficiency leading to further complexities. With the data not being in an ideal state for ML, data cleaning required a rigorous amount of effort, trialing through the columns and features to select only the important features for ML followed by encoding and binning data for better consistency during the training process. The optimization of the model posed additional challenges, as the length of the dataset prolonged the training and prediction periods. Recognizing the need for strategic planning to minimize processing time, critical thinking played a crucial role in devising advanced optimization strategies. This proactive approach aimed to streamline the machine's ability to efficiently process the data, mitigating the impact of the dataset's extensive size on the overall project timeline.

For future endeavours, having data from several insurance companies can enhance the credibility of the model, and allow the model to expand it's horizons towards greater target audiences, such as insurance companies themselves to run insurance claims to detect for fraudelant claims. 

Contriubtors: Yasmin, Allan, Qudsia, and Merve
