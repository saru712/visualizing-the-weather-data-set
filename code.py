# --------------
# Import the required Libraries
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import calendar
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# Generate a line chart that visualizes the readings in the months

def line_chart(df,period,col):
    dict={'Year':'A','month':'M','day':'D'}
    lc=df.groupby(pd.Grouper(freq=dict[period]))[[col]].mean()
    # print(lc)
    plt.plot(pd.DatetimeIndex(lc.index).month_name(),lc)
    plt.ylim(-7,25)
    plt.xlabel("Months")
    plt.title('Temperature Trend,2012')
    plt.ylabel('Temp (C)')
    plt.xticks(rotation=90)
    plt.show()
    """ A line chart that visualizes the readings in the months
    
    This function accepts the dataframe df ,period(day/month/year) and col(feature), which plots the aggregated value of the feature based on the periods. Ensure the period labels are properly named.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    period - Period of time over which you want to aggregate the data
    col - Feature of the dataframe
    
    """
   
    
    







# Function to perform univariate analysis of categorical columns
def plot_categorical_columns(df):
    plt.figure(figsize=[14,8])
    plt.xlabel("Weather")
    plt.ylabel("No of categorical weather")
    plt.title("Distribution of weather across different types")
    cate=df['Weather'].value_counts(ascending=False)
    # print(cate)
    cate.plot(kind="bar")
    plt.show()
    """ Univariate analysis of categorical columns
    
    This function accepts the dataframe df which analyzes all the variable in the data and performs the univariate analysis using bar plot.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    
    """
    








# Function to plot continous plots
def plot_cont(df,plt_typ):
    if plt_typ=='Dist_plot':
        for col in df.columns:
            plt.figure(figsize=(10,4))
            sns.distplot(df[col].value_counts())
    else:
        for col in df.columns:
            plt.figure(figsize=(10,4))
            df.plot.box(df[col].value_counts())
            
            
    """ Univariate analysis of Numerical columns
    
    This function accepts the dataframe df, plt_type(boxplot/distplot) which analyzes all the variable in the data and performs the univariate analysis using boxplot or distplot plot.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    plt_type - type of plot through which you want to visualize the data
    
    """
    
    







# Function to plot grouped values based on the feature
def group_values(df,col1,agg1,col2):
    aggregate = {'mean':np.mean,'max':np.max,'min':np.min,'sum':np.sum,'len':len}
    grouping = df.groupby(col1).agg(aggregate[agg1])
    ty=grouping[col2]
    plt.figure(figsize=[14,8])
    ty.plot(kind="bar")
    plt.xlabel("Weather")
    plt.show()
    """ Agrregate values by grouping
    
    This function accepts a dataframe, 2 column(feature) and aggregated function(agg1) which groupby the dataframe based on the column and plots the bar plot.
   
    Keyword arguments:
    df - Pandas dataframe which has the data.
    col1 - Feature of the dataframe on which values will be aggregated.
    agg1 - Dictionary of aggregate functions with feature as the key and func as the value
    col2 - Feature of the dataframe to be plot against grouped data.
    
    Returns:
    grouping - Dataframe with all columns on which it is grouped on.
    """
    
    




# Read the Data and pass the parameter as parse_dates=True, index_col='Date/Time'
weather_df=pd.read_csv(path,index_col='Date/Time', parse_dates=True)



# Lets try to generate a line chart that visualizes the temperature readings in the months.
# Call the function line_chart() with the appropriate parameters.

line_chart(weather_df,'month','Temp (C)')


# Now let's perform the univariate analysis of categorical features.
# Call the "function plot_categorical_columns()" with appropriate parameters.
plot_categorical_columns(weather_df)


# Let's plot the Univariate analysis of Numerical columns.
# Call the function "plot_cont()" with the appropriate parameters to plot distplot

plot_cont(weather_df,'Dist_plot')


# Call the function "plot_cont()" with the appropriate parameters to plot boxplot

plot_cont(weather_df,'box_plot')

# Groupby the data by Weather and plot the graph of the mean visibility during different weathers. Call the function group_values to plot the graph.
# Feel free to try on diffrent features and aggregated functions like max, min.
group_values(weather_df,'Weather','mean','Visibility (km)')



