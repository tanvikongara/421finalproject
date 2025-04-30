Data  
http://cicresearch.ca/IOTDataset/CIC_IOT_Dataset2023/Dataset/CSV/MERGED_CSV/  

# Steps to Getting the Data
  
### 1. Download from Google Drive  
Here is the link: https://drive.google.com/file/d/1OaBAN5_LsKojzBmzmV7jONfvSnz4CIBz/view?usp=sharing.
  
### 2. Add to Your Cloned Copy of the Repo  
After cloning the repository locally, make a Data folder.  
Within the data folder, add the total_merged_data.parquet.


# Our Process  
  
### 1. EDA  
We started off our goal of classifying between all these different cyber attacks with EDA. We started off with basic data pre-processing and performed tasks like removing null values and exploring our features and targets. Then, we realized that we had a severe class imbalanced dataset with many features and many predictors. We're actually in a unique situation where


### Conclusion
Our best model was the XGBOOST model where we got an accuracy of 0.74. If we had more time, I think the direction we would work toward would be to undersample majority classes and not perform SMOTE but apply class weights to the MLP. 