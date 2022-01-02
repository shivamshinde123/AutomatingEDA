
#Imports
import os.path
import matplotlib.pyplot as plt


# Creating a class called EDA which will contain all the methods needed for the exploratory data analysis of given file
class EDA:

    def __init__(self,data):
        # Getting the extension of data file entered
        datafile_extension = os.path.splitext(data)[1]
        # Checking whether the entered file is csv file or not
        self.data = data


    ## Creating methods to get the basic info of entered data file
    def shape_of_dataset(self):
        try:
            print(f"The shape of the dataset is {self.data.shape}/n")
        except Exception as e:
            print(e)

    def no_of_rows(self):
        try:
            print(f"Dataset has {self.data.shape[0]} rows/n")
        except Exception as e:
            print(e)

    def no_of_columns(self):
        try:
            print(f"Dataset has {self.data.shape[1]} columns/n")
        except Exception as e:
            print(e)

    def dataset_info(self):
        try:
            print("Dataset Info:")
            return self.data.info()
        except Exception as e:
            print(e)

    def dataset_description(self):
        try:
            print("/n")
            return self.data.describe()
        except Exception as e:
            print(e)

    def uniques_values(self):
        try:
            print('/n')
            for feature in self.data.columns:
                print(f"The feature {feature} has {self.data[feature].nunique()} unique values")
            print('/n')
        except Exception as e:
            print(e)

    def feature_types(self):
        try:
            numerical_features = [feature for feature in self.data.columns if self.data[feature].dtypes != 'O']
            categorical_features = [feature for feature in self.data.columns if feature not in numerical_features]
            numerical_discrete_features = [feature for feature in numerical_features if self.data[feature].nunique() < 10]
            numerical_continuous_features = [feature for feature in numerical_features if feature not in numerical_discrete_features]

            print(f"Numerical discrete features in the dataset are: {numerical_discrete_features}")
            print(f"Numerical continuous features in the dataset are: {numerical_continuous_features}")
            print(f"Categorical features in the dataset are: {categorical_features}")
        except Exception as e:
            print(e)

    def percentage_of_na(self):
        try:
            for feature in self.data.columns:
                print(f"The feature {feature} has {self.data[feature].isnull().mean()*100} % missing values")
        except Exception as e:
            print(e)

    def graphs(self):
        try:
            numerical_features = [feature for feature in self.data.columns if self.data[feature].dtypes != 'O']
            categorical_features = [feature for feature in self.data.columns if feature not in numerical_features]
            numerical_discrete_features = [feature for feature in numerical_features if self.data[feature].nunique() < 10]
            numerical_continuous_features = [feature for feature in numerical_features if feature not in numerical_discrete_features]
        except Exception as e:
            print(e)

        print("Visualizing relationship between dependent feature and numerical discrete features:/n")
        try:
            for feature in numerical_discrete_features:
                self.data.groupby(feature)[self.data.columns[-1]].median().plot(kind='bar')
                plt.xlabel(feature)
                plt.ylabel('Median value')
                plt.title(feature)
                plt.show()
        except Exception as e:
            print("Error occurred while visualizing discrete numerical features.")
            print("Error: "+str(e))

        print("Visualizing relationship between dependent feature and numerical continuous features:/n")
        try:
            for feature in numerical_continuous_features:
                self.data[feature].hist()
                plt.xlabel(feature)
                plt.ylabel('Count')
                plt.title(feature)
                plt.show()
        except Exception as e:
            print("Error occurred while visualizing continuous numerical features.")
            print("Error: "+str(e))

        print("Visualizing relationship between dependent feature and categorical features:/n")
        try:
            for feature in categorical_features:
                self.data.groupby(feature)[self.data.columns[-1]].median().plot(kind='bar')
                plt.xlabel(feature)
                plt.ylabel('Median value')
                plt.title(feature)
                plt.show()
        except Exception as e:
            print("Error occurred while visualizing categorical feature.")
            print("Error: "+str(e))