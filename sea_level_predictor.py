import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df =pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'],color='blue')   
   
    # Create first line of best fit
    result=linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope = result.slope
    intercept = result.intercept
    x= df['Year'].to_numpy() 
    maximum =x.max() 
    i = np.array([i+1 for i in range(2050) if i>=maximum])
    # print(i)
    x = np.concatenate((x,i),axis=0)
    y = slope*x + intercept 
    # print(y)
    plt.plot(x,y,color="red")
    

    # Create second line of best fit
    x_linearize=np.array([year for year in range(2014) if year >=2000])
    x2=np.array([year for year in range(2051) if year >=2000])
    # print(x2)
    y_linearize = df['CSIRO Adjusted Sea Level'].loc[df.Year.isin(x_linearize)]
    # print(y_linearize)
    result2=linregress(x_linearize, y_linearize)
    slope2 = result2.slope
    intercept2 = result2.intercept
    y2 = slope2*x2 + intercept2 
    plt.plot(x2,y2,color="green")
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
draw_plot()