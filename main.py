'''
INF601 - Programming in Python
Assignment - Mini Project 2
I, Dawsyn Birtell, affirm that the work submitted for this assignment is entirely my own. 
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials.
I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards.
I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. 
By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''


import pandas as pd
import os
import matplotlib.pyplot as plt

os.makedirs('charts', exist_ok=True)

# Load the dataset into a pandas dataframe | Added incoding to fix error
models = pd.read_csv("Mobiles Dataset (2025).csv", index_col=0, parse_dates=True, encoding="Windows-1252")

# iphone models to graph
iphone_models = ["iPhone 16", "iPhone 15", "iPhone 14", "iPhone 13", "iPhone 12"]

# Region launch prices
region_prices = ['Launched Price (USA)', 'Launched Price (India)', 'Launched Price (China)', 'Launched Price (Dubai)', 'Launched Price (Pakistan)']

i = 0 # index for iphone_models

# Loop through each iPhone model and plot
for model in iphone_models:
    # Filter data to only include the selected model
    filtered_data = models[models['Model Name'].str.contains(model, na=False, case=False)][['Model Name'] + region_prices]

    # Ensure there is data before proceeding
    if not filtered_data.empty:
        plt.figure(figsize=(10, 10))

        # Separate x (Model Name) and y (Prices) before plotting
        x_axis = filtered_data['Model Name']  # X-axis (Model names)
        
        for region in region_prices:
            y_axis = filtered_data[region]  # Y-axis (Prices for each region)
            plt.plot(x_axis, y_axis, marker='o', linestyle='-', label=region)  # Plot each region separately

        plt.xlabel('iPhone Model') # x-axis label
        plt.ylabel("Regional Launch Price") # y-axis label
        plt.title("iPhone Launch Prices") # title of the graph  
        plt.xticks(rotation=30, ha='right') # rotate x-axis labels
        plt.legend()
        plt.savefig(f'charts//{iphone_models[i]}.png') # save the graph as a png file
        i += 1 # increment index for file names 
        

