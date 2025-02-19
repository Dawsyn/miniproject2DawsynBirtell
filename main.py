'''
INF601 - Programming in Python
Assignment - Mini Project 2
I, Dawsyn Birtell, affirm that the work submitted for this assignment is entirely my own. 
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials.
I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards.
I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. 
By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''

""" 
(5/5 points) Initial comments with your name, class and project at the top of your .py file.
Done
(5/5 points) Proper import of packages used.
DONE
(20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
Think of some question you would like to solve such as:
"How many homes in the US have access to 100Mbps Internet or more?"
"How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
Here are some other great datasets: https://www.kaggle.com/datasets
(10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
DONE
(10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
(10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset into a pandas dataframe | Added incoding to fix error
models = pd.read_csv("Mobiles Dataset (2025).csv", index_col=0, parse_dates=True, encoding="Windows-1252")

# iphone models to graph
iphone_models = ["iPhone 16", "iPhone 15", "iPhone 14", "iPhone 13", "iPhone 12"]


# Loop through each iPhone model and plot
for model in iphone_models:
    filtered_data = models[models['Model Name'].str.contains(model, na=False, case=False)]
    plt.plot(filtered_data['Model Name'], filtered_data['Launched Price (USA)'], marker='o', linestyle='-', label=model)
    plt.xlabel('Model')
    plt.ylabel('Launch Price (USA)')
    plt.title("iPhone Launch Prices")
    plt.xticks(rotation=45, ha='right')
    plt.show()

#plt.plot(models[models['Model Name'].str.contains("16")], models['Launched Price (USA)'])


