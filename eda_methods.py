
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
        return self.data.shape

    def no_of_rows(self):
        return self.data.shape[0]

    def no_of_columns(self):
        return self.data.shape[1]

    def dataset_info(self):
        return self.data.info()

    def dataset_description(self):
        return self.data.describe()

