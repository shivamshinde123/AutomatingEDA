
#Imports
import pandas as pd
import sweetviz as sv



# Creating a class called EDA which will contain all the methods needed for the exploratory data analysis of given file
class EDA:

    def __init__(self,url):
        self.data = pd.read_csv(url)

    def report_creation(self):
        ## Sweetviz library only supports numerical dependent feature
        ## That's why, when the dependent feature is numerical, we will provide it as target feature in analyze function
        ## else, we won't supply it
        if self.data[self.data.columns[-1]].dtypes != 'O':
            my_report = sv.analyze(self.data,self.data.columns[-1])
        else:
            my_report = sv.analyze(self.data)
        my_report.show_html('templates/results.html',open_browser=False)

