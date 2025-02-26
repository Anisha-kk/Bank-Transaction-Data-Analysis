# Bank-Transaction-Data-Analysis
## Overview
The goal of this project is to analyse Bank Transaction data to detect fraudulent transactions. The project used Random Forest Classifier to perform the classification. The model achieved a recall score of 83% on the test set. A basic Flask app is created to predict whether a new transaction is fraudulent or not.
## Problem Understanding
Fraudulent behavior can be seen across many different fields such as e-commerce, healthcare, payment and banking systems. Fraud is a billion-dollar business and it is increasing every year. We need a mechanism to detect fraudulent transactions. Machine Learning can be used for this purpose. A machine learning model can be trained with bank transaction data already calssified as normal and fraud. This model can then be used to predict the nature of a new transaction.
## Data Understanding
Source: https://www.kaggle.com/code/kartik2112/fraud-detection-banksim/data?select=bs140513_032310.csv

The fraudulent transactions are detected from the Banksim dataset. This synthetically generated dataset consists of payments from various customers made in different time periods and with different amounts. There are 594643 rows in the dataset.
The dataset has 9 feature columns and a target column. The feature columms are :

•	Step: This feature represents the day from the start of simulation. It has 180 steps so simulation ran for virtually 6 months.

•	Customer: This feature represents the customer id

•	zipCodeOrigin: The zip code of origin/source.

•	Merchant: The merchant's id

•	zipMerchant: The merchant's zip code

•	Age: Categorized age
<br>0: <= 18,
<br>1: 19-25,
<br>2: 26-35,
<br>3: 36-45,
<br>4: 46:55,
<br>5: 56:65,
<br>6: > 65
<br>U: Unknown

•	Gender: Gender for customer: 
<br>E : Enterprise,
<br>F: Female,
<br>M: Male,
<br>U: Unknown

•	Category: Category of the purchase. Following are the categories and their count:
<br>'es_transportation'  -      505119
<br>'es_food'            -       26254
<br>'es_health'           -      16133
<br>'es_wellnessandbeauty' -     15086
<br>'es_fashion'         -        6454
<br>'es_barsandrestaurants'-      6373
<br>'es_hyper'        -           6098
<br>'es_sportsandtoys'  -         4002
<br>'es_tech'          -          2370
<br>'es_home'         -           1986
<br>'es_hotelservices'  -         1744
<br>'es_otherservices'  -          912
<br>'es_contents'      -           885
<br>'es_travel'       -            728
<br>'es_leisure'     -             499

It seems that the highest number of transactions are done for transportation.
•	Amount: Amount of the purchase

•	Fraud: Target variable which shows if the transaction fraudulent(1) or benign(0)

Fraud data will be imbalanced like you see in the plot below: 
![Screenshot (4723)](https://github.com/user-attachments/assets/58ba7d71-dfbe-4c4a-bc80-ad574d31a01d)

To balance the dataset one can perform oversampling or undersampling techniques. Oversampling is increasing the number of the minority class by generating instances from the minority class . Undersampling is reducing the number of instances in the majority class by selecting random points from it to where it is equal with the minority class. Both operations have some risks: Oversample will create copies or similar data points which sometimes would not be helpful for the case of fraud detection because fraudulent transactions may vary. Undersampling means that we lost data points thus information. Here, an oversampled technique called SMOTE (Synthetic Minority Over-sampling Technique) is used. SMOTE creates new data points from minority class using the neighbour instances so generated samples are not exact copies but they are similar to existing instances.
## Modeling and Evaluation
A Random Forest classifier is used to train the dataset. The resultant model has a recall score of **83%**. Since the class distribution is highly unbalanced, accuracy is not a good performance metric for this problem. Another metric used to evaluate the performance is ROC - AUC curve. 
![Screenshot (4724)](https://github.com/user-attachments/assets/bda75856-e935-4340-bff8-111f54ccc753)


An AUC of 0.91 indicates a good classification. 

An app is created from the model to predict the nature of a new transaction using Flask and Python. Below is the screenshots of the app homepage:
![Screenshot (4720)](https://github.com/user-attachments/assets/43dcdb8e-a1a4-4b0f-ab6e-0ddad2b50249)

Example of a transaction predicted as normal:
![Screenshot (4721)](https://github.com/user-attachments/assets/aeff9afb-f4dd-47f4-9e0f-50e4a8c1a10e)

Example of a transaction predicted as fraudulent:
![Screenshot (4722)](https://github.com/user-attachments/assets/505e27db-b943-42a1-8245-6ab641bd3134)

## Conclusion
This project classifies bank transaction data into normal and fraudulent transactions. The resultant model is used to predict the nature of a new transaction through a Flask app.







