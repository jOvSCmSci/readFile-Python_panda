# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 14:48:47 2022

@author: Jovena
"""
""" Machine learning Act3 Jovena Mae Serrano BSCS 4A
Reading CSV File and Displaying the Data in the Form of Scatter Plot

Create a code in Python that will read the CSV file "insurance.csv" 
using the Python's PANDAS library and display the columns "Age" and 
"BMI" as an X & Y pair in a Scatter Plot using MatPlotLib Library of Python.  
Display also the ratio of Male to Female in the form of Pie Chart also using MatPlotLib.

Compute for the Mean of the AGE and BMI column and display the results on the screen. 
 Use NumPy Library for this activity.
"""
#importing modules / libraries needed for execution 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
# Reading csv file using pandas library, to access the csv file enter the csv path 
file = pd.read_csv('C:\\Users\\Jovena\\Machine_Learning.py\\.spyproject\\insurance.csv')

# function declaration executing the mean of Age and BMI 
# and outputs the Age and BMI in a form of Scatter plot using MatPlotLib
def scatter_plot(file): 
    # this will convert the column age and bmi from csv file into a list 
    x = file['age'].tolist() 
    y = file['bmi'].tolist()
    
    plt.scatter(x, y) # setting for scatter plot
    plt.xlabel("x (Age)", fontsize = 20, color = 'b') # adding labels 
    plt.ylabel("y (BMI)", fontsize = 20, color = 'r') # adding labels
    plt.show # outputs the scatter plot
    
    mean_x = np.mean(x) # this will get the mean value for x(Age) using NumPy
    mean_y = np.mean(y) # thsi will get the mean value for y(bmi) using NumPy
    
    #outputs the rounded mean value for age and bmi
    print("The mean value for Age is: ", round(mean_x, 4))
    print("The mean value for BMI is: ", round(mean_y, 4))

# function declaration that outputs the pie chart base from the male and female ratio
def pie_chart(num):
    
    return f'{num / 100 * len(file):.0f}\n{num:.0f}%'
# user interface
print("-------------------------------------------------------------------")
print(" Machine Learning Activity 3, Serrano Jovena Mae_BSCS 4A")
print(" Execution..........")
print("-------------------------------------------------------------------")
print("\n -> insurance.csv <- \n")

print(file) # outputs the csv file
print("\n--> Mean value of Age and BMI using NumPy Lib <--")
print("--> Scatter Plot using MatPlotLib <--")
print("--> Outputs the ratio of Male and Female in a form of Pie Chart <--\n")
scatter_plot(file) #function call
#execution for the pie chart 
fig, ax1 = plt.subplots(ncols=1, figsize=(10,5))

file.groupby('sex').size().plot(kind = 'pie', autopct = pie_chart, textprops = 
            {'fontsize' : 20}, colors = ['y', 'c'], ax =ax1, shadow = True)




    
