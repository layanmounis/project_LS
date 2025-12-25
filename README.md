# project_LS
DS project
1. Project Idea

The goal of this project is to build a simple real-world data science application.
We collect job data from the web, store it in JSON format, analyze it using Pandas, and apply Scikit-Learn preprocessing.

The project follows the steps taught in the course:

Web Scraping and Crawling

JSON File Manipulation

Data Analysis using Pandas

Data Preprocessing using Scikit-Learn

2. Tools and Libraries Used

In this project, we used the following Python libraries:

requests

BeautifulSoup

json

pandas

scikit-learn

ThreadPoolExecutor

Each library is used for a specific purpose, explained below.

3. Web Scraping and Crawling 🌐
What is Web Scraping?

Web scraping means collecting data from websites automatically.

What is Crawling?

Crawling means visiting web pages and extracting information from them.

Where Web Scraping is Used

We used requests to download the web page and BeautifulSoup to read the HTML content.

import requests
from bs4 import BeautifulSoup


requests.get() downloads the webpage

BeautifulSoup helps us search inside the HTML

We scraped job titles from a real job website.

4. Multithreading ⚡
What is Multithreading?

Multithreading means doing multiple tasks at the same time to make the program faster.

Why We Used Multithreading

Instead of scraping one page at a time, we scraped multiple pages in parallel.

from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(scrape_page, pages)


This improves performance and shows the use of multithreading as required.

5. JSON File Manipulation 📂
Why JSON?

JSON is a lightweight format used to store structured data.

Writing Data to JSON

After scraping, we saved the collected data into a JSON file.

import json

json.dump(jobs, file)


This created the file:

data/jobs.json

Reading Data from JSON

Later, we read the JSON file to analyze the data.

jobs = json.load(file)


This step shows JSON file manipulation.

6. Using Pandas for Data Analysis 🐼
What is Pandas?

Pandas is a Python library used for data manipulation and analysis.

Creating a DataFrame

We converted the JSON data into a Pandas DataFrame.

df = pd.DataFrame(jobs)


This allows us to work with data in rows and columns.

Data Cleaning with Pandas

We used Pandas to handle missing values.

df["job_title"] = df["job_title"].fillna("")


This prevents errors during analysis.

Data Exploration with Pandas

We used Pandas to:

Count total jobs

Display the first few job titles

print(len(df))
print(df["job_title"].head())


This helps us understand the dataset.

Saving Clean Data

After cleaning, we saved the processed data again.

df.to_json("data/clean_jobs.json", orient="records")

7. Scikit-Learn Preprocessing 
What is Data Preprocessing?

Preprocessing prepares raw data so it can be used in machine learning.

Why Scikit-Learn?

Machine learning models cannot work with text directly.
Scikit-Learn provides tools to convert text into numeric values.

Using LabelEncoder

We used LabelEncoder to convert job titles into numbers.

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df["job_title_encoded"] = le.fit_transform(df["job_title"])


This step is required preprocessing.
8. Project Workflow Summary

Scrape job data from the web

Use multithreading to speed up scraping

Save data into a JSON file

Load data using Pandas

Clean and analyze data with Pandas

Apply Scikit-Learn preprocessing

Save final processed data

9. Conclusion

In this project, we successfully implemented a simple data science application.
We used web scraping to collect data, Pandas for analysis, and Scikit-Learn for preprocessing.
All steps follow the course requirements and demonstrate practical data science skills
