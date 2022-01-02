
#Imports
import os.path

# Creating a class called EDA which will contain all the methods needed for the exploratory data analysis of given file
class EDA:

    def __init__(self,data):
        # Getting the extension of data file entered
        datafile_extension = os.path.splitext(data)[1]
        # Checking whether the entered file is csv file or not
        if datafile_extension == ".csv":
            self.data = data
        else:
            print("Please enter a file with .csv extension")

    ## Creating methods to get the basic info of entered data file
    def shape_of_dataset(self):
        print(f"The shape of the dataset is {self.data.shape}/n")

    def no_of_rows(self):
        print(f"Dataset has {self.data.shape[0]} rows/n")

    def no_of_columns(self):
        print(f"Dataset has {self.data.shape[1]} columns/n")

    def dataset_info(self):
        print("Dataset Info:")
        return self.data.info()

    def dataset_description(self):
        print("/n")
        return self.data.describe()

    def uniques_values(self):
        print('/n')
        for feature in self.data.columns:
            print(f"The feature {feature} has {self.data[feature].nunique()} unique values")
        print('/n')
    def feature_types(self):
        numerical_features = [feature for feature in self.data.columns if self.data[feature].dtypes != 'O']
        categorical_features = [feature for feature in self.data.columns if feature not in numerical_features]
        numerical_discrete_features = [feature for feature in numerical_features if self.data[feature].nunique() < 10]
        numerical_continuous_features = [feature for feature in numerical_features if feature not in numerical_discrete_features]

        print(f"Numerical discrete features in the dataset are: {numerical_discrete_features}")
        print(f"Numerical continuous features in the dataset are: {numerical_continuous_features}")
        print(f"Categorical features in the dataset are: {categorical_features}")

