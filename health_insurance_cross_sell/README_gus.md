
# - BUSINESS ASSUMPTIONS

**HYPOTHESIS**

According to the database information, **Annual_Premium** is the amount customer needs to pay as premium in the year. So, just to make it clearer, it refers to the value of the health insurance paid and not the automobile insurance offer.

Based on a survey on the references below, the **average cost of car insurance** was assumed as $1,000 per year. As most references below estimations are higher, the revenue estimations for this project are somewhat pessimistic.

It was assumed that **10%** of interested customers will buy the automobile insurance after being contacted.

References:

https://www.bankrate.com/insurance/car/average-cost-of-car-insurance/

https://www.policygenius.com/auto-insurance/learn/how-much-is-car-insurance/

https://www.businessinsider.com/personal-finance/average-cost-of-car-insurance

# - SOLUTION STRATEGY

![crisp-ds](pa004_gustavo_cunha/images/crisp-ds.png)

## Step 01. Data Extraction:
Using SQL, extract data from a PostgreSQL database on Amazon AWS cloud. Then, analyse the entity-relationship diagram and merge different tables.

## Step 02. Data Description:
Check column names, number of rows in the table, data types for each column and number o NA values (not-available values). Then use statistics metrics to identify data outside the scope of business.

## Step 03. Feature Engineering:
Create a hypothesis list to check on the fifth step (EDA). Then apply data transformations on the required columns.

## Step 04. Data Filtering:
Filter rows and select columns that do not contain information for modelling or do not match the scope of the business.

## Step 05. Exploratory Data Analysis:
Analyse each variable alone and then the relationship among variables. Then, explore the data further to validate the hypothesis list and raise insights.

## Step 06. Data Preparation:
Split data into train and validation and test. Then, prepare data so that the Machine Learning models can more easily learn and perform more accurately.

## Step 07. Feature Selection:
Select the most signiﬁcant attributes for training the model.

## Step 08. Machine Learning Modelling:
Test different Machine Learning models and select the one with the best performance in ranking customers according to their interest.

## Step 09. Hyperparameter Fine Tuning:
Choose the best values for each parameter of the selected ML model.

## Step 10. Performance Evaluation and Interpretation:
Check the learning performance and the generalization performance of the ML model (overfitting vs underfitting). Then convert the ML performance into business results.

## Step 11. Deployment:
Create an API (Application Programming Interface) to make predictions available on internet requests. Then, for the final user, create a google sheet that gets predictions directly from the API by just clicking a button.

# - TOP 3 INSIGHTS

## - H1. Considering people interested in automobile insurance, the number of customers interested in automobile insurance has a large variation according to customers' region.

> H1 IS TRUE. Different regions have a large variation in terms of the number of interested customers.
    
![h4_hypothesis](images/h4_hypothesis.png)
    
**Suggestion**: investigate further as there may be better regions to focus on sales.

## - H2. Different sales channels have a large variation in terms of the number of interested customers.

> H7 IS TRUE. The number of interested customers may vary largely among sales channels.

![h7_hypothesis](pa004_gustavo_cunha/images/h7_hypothesis.png) 

**Suggestion:** investigate further as there may be better channels to focus on sales.

## - H3. Considering people interested in automobile insurance, most of them contracted cheaper health insurance in the past.

> H3 IS FALSE. The number of interested customers doesn't always decrease with increasing annual health insurance premium of past contracts. There is a region of annual premium about 35000 where, the higher the annual premium, the higher the number of interested customers.

![h9_hypothesis](pa004_gustavo_cunha/images/h9_hypothesis.png) 

# - BUSINESS RESULTS

## Making 20.000 phone calls, what percentage of interested clients the sales team will get in contact with?

![20k_questions](pa004_gustavo_cunha/imagess/second_business_question.png)

## If the sales team expands its capacity to make 40.000 phone calls, what is the percentage of interested clients the sales team will get in contact with?

![80k_question](pa004_gustavo_cunha/images/third_business_question.png)

## How many phone calls do the sales team has to make to contact 80% of automobile insurance interested clients?

![80%_question](pa004_gustavo_cunha/images/fourth_business_question.png)

## Compiled business results

![compiled_questions](pa004_gustavo_cunha/images/compiled_business_question.png)

# - RANDOM MODEL vs ML MODEL

![random_vs_ml](pa004_gustavo_cunha/images/lift_business_question.png)

# - DEPLOYMENT

**Google Sheet**

A Google Sheet was created so that the sales team can easily check the likelihood of a customer being interested in automobile insurance. With this solution, the sales team can also easily sort customers according to their interests.

You can check how to make predictions via this spreadsheet by watching the following video:
https://youtu.be/l7lt7gji7oY

# - CONCLUSIONS

As this is my first Data Science project, it took me a while to go from the very beginning till the very end of the project (actually, it took me about three weeks). 

However, **even within just a few weeks, we can easily see that Data Science projects could increase the company revenue in expressive numbers**.

# - LESSONS LEARNED

**How to do an end-to-end Data Science project.**

**How to build a Flask API and host on Heroku cloud so that a google spreadsheet could request predictions within two clicks.**

**It's important to focus on business results and don't get lost in using different tools.**

**It's important to focus on how the business results will be improved, not what ML models will be applied.**

**On the first project cycle, it's important to keep things simple and not try to get the best solution because this can only be achieved through many project cycles.**

# - NEXT STEPS TO IMPROVE

**Google sheet**: improve user interface and make checkings on data input by the users.

**Features**: try different variables, scalers and encodings so that ML performance improves.

**API**: improve the interaction between API and spreadsheet so that users get more intuitive messages in case of errors.

**Data**: improve the quality of the data. One solution here may be to gather more data about the customers, especially new variables. 

**Code**: review the whole code once more to make it clearer and more efficient (faster and less resource-intensive).




# LICENSE

# All Rights Reserved - Comunidade DS 2021
