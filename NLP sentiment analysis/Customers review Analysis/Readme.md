# Hotel Customers Sentiment Analysis
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites) 
* [Reading Dataset](#reading-dataset)
* [Exploratory Data Analysis](#exploratory-data-analysis)
  * [Observations](#observations)
* [Data Cleansing and Training Model](#data-cleansing-and-training-model)
* [Testing Model](#testing-model)
<!-- ABOUT THE PROJECT -->
## About The Project
![images](https://raw.githubusercontent.com/Surekha-honey/Deep-Learning-Projects/master/NLP%20sentiment%20analysis/Customers%20review%20Analysis/Images/1.png)

Main focus of this project is to analyse customers sentiment weather they are satisfied with hotel services or not with the help of customers Feedback.
A list of commonly used resources that I find helpful are listed in the acknowledgements.

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites
Programming Language :Python Version : 3.7  <br>
 Packages: pandas, numpy, sklearn, matplotlib, seaborn, 
 * To analyze Users Sentiment [NLTK](https://www.nltk.org/) very useful. <br>
    `pip install nltk`  <br>
 * KNeighbors Classifier ,Logistic Regression ,RandomForestClassifier all these algorithms are Classification in Supervised Learning .
### Reading Dataset
![](https://raw.githubusercontent.com/Surekha-honey/Deep-Learning-Projects/master/NLP%20sentiment%20analysis/Customers%20review%20Analysis/Images/3.png)

### Exploratory Data Analysis
![images](https://raw.githubusercontent.com/Surekha-honey/Deep-Learning-Projects/master/NLP%20sentiment%20analysis/Customers%20review%20Analysis/Images/4.png)
   ### Observations
* Most of customers to give feedback they had been used Firefox 7367 peoples and Microsoft edge 7134 people's mostly used compare to all other browsers.
* In very few peoples in the sense only 362 customers had been used operamini to give feedback .

![images](https://raw.githubusercontent.com/Surekha-honey/Deep-Learning-Projects/master/NLP%20sentiment%20analysis/Customers%20review%20Analysis/Images/5.png)

   ### Observations
* From here we can observe one thing most of the customers who gave feedback they mostly used Desktop compare Mobile and Tablet .

## Data Cleansing and Training Model
   * This steps plays an key role while training model 
   * For Cleansing data on text data best methods are regular expressions,Lambda functions , Stop words removal and some other techniques .
   * To train model we have to follow some steps:
       * Splitting dataset into training and testing
       * applying algorithms 
       * Selecting Best algorithm based on error and accuracy 
       * Finally tuning model 
       * Check it out complete project [here](https://github.com/Surekha-honey/Deep-Learning-Projects/blob/master/NLP%20sentiment%20analysis/Customers%20review%20Analysis/Restraunt%20Customers%20%20Review%20Analysis%20Weather%20it's%20Positive%20or%20Negative.ipynb)
       



## Testing Model

![images](https://raw.githubusercontent.com/Surekha-honey/Deep-Learning-Projects/master/NLP%20sentiment%20analysis/Customers%20review%20Analysis/Images/6.png)









