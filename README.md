<h1 align="center"> Instahyre Job Analytics </h1>

<img src="https://github.com/AmarjeetRoy/AmarjeetRoy/assets/137817362/089a3079-6ae4-4e1d-885a-6c162f720c66">
<br><br>

Welcome to the **Instahyre Job Analytics** repository! This project revolves around comprehensively understanding the job market dynamics using data-driven insights. Our team, consisting of dedicated members, embarked on a journey to extract, preprocess, and analyze job posting data from Instahyre and LinkedIn, shedding light on the employment landscape.

<br>

## 🧑🏽‍💻Team Members

- Amarjeet Roy (My Self)
- Priya Bhardwaj
- Ajay Kumar
- Bharat Sharma
<br>

## 🎯Aim
The aim of the Instahyre Job Analytics project is two-fold. First, our goal is to build a model that can effectively summarize job posting data, providing users with a concise overview of job market trends. Second, we aim to create an interactive webpage that allows users to easily access and explore these job market insights. This project seeks to empower job seekers and recruiters with valuable information for informed decision-making.
<br><br>

## 👁️Project Overview

The data extraction phase involves obtaining job posting data from Instahyre's website. This process is crucial for gathering raw data that will be later cleaned, processed, and analyzed.
<br>
### 🗒️Web Scraping
We gathered data by automating web scraping with Python's Selenium library. Our target was to scrape data like "job_id," "company_id," "location," "designation," "name," "estab_year," "employees_count," "involvement," "skills," and "hr_name" from the Instahyre website. This process was simplified by utilizing a custom Selenium script tailored for this specific task.

**Reference Files:**
- **[`Extraction_Code.ipynb`](Extraction/Extraction%20Code.ipynb)**: Python script for web scraping job posting data and LinkedIn information.
### 🗒️Data Preparation
After scraping the data, our next step involved comprehensive data cleaning and transformation using Python libraries. This step was essential for handling missing values, outliers, and ensuring data consistency. Additionally, we organized the cleaned data into three separate tables, these tables can be found in **[`Tables`](Extraction/Tables)** folder inside the **[`Extraction`](Extraction)** Folder:
- **[`Jobs Table`](Extraction/Tables/job.csv)**: This table contains information related to job postings, including "job_id," "location," "designation," "skills," and "hr_name."
- **[`Company Table`](Extraction/Tables/company.csv)**: Here, we stored company-specific data such as "company_id," "name," "estab_year," and "employees_count."
- **[`Details Table`](Extraction/Tables/Details.csv)**: This table holds additional details related to job postings and companies, including "involvement" and other relevant information.
- **[`Merged Table`](Extraction/Tables/Merged_data.csv)** : This Table contains all the scrpaed Details including Linkedin's data and all three table's data.

**Additional Files in Extraction Directory:**
  - **[`Job webLink.csv`](Extraction/Job%20webLinks.csv)**: Contains web links of all job pages.
  - **[`New Updated Csv.csv`](Extraction/New%20Updated%20CSV.csv)**: Preprocessed data with some initial modifications.

<br>

### 💻Data Preprocessing and Model Building

The data preprocessing and model building phase focus on refining the raw data and creating a clustering model for analysis.

### 💻Data Cleaning
In this phase, we performed comprehensive data cleaning and preprocessing using Python libraries. This step is essential for handling missing values, outliers, and ensuring data consistency. The cleaning process improved the quality of the data for subsequent analysis.

### 💻K-means Clustering Model
We used Scikit-learn to build a K-means clustering model. This model categorizes companies based on their LinkedIn followers and employee count, allowing us to understand different company classes. The K-means model helped us gain insights into the job market and classify companies effectively.All these work's code can be found in **[`Processing`](Processing)** folder's  **[`Data Preprocessing and Clustering.ipynb`](Processing/Data%20Preprocessing%20and%20Clustering.ipynb)** file which took **[`New Updated Csv.csv`](Processing/New%20Updated%20CSV.csv)** as input Dataframe and Generated **[Processed_file.csv (Processing/Processed_file.csv)** with details of Job Class and Changes made in Data Cleaning.

<br>

### 🕸️Website Development and Model Deployment

The website development and model deployment phase involved creating an interactive website to present our insights and model results to users.

### 🖼️Frontend Development

We designed and implemented the website's frontend using HTML and CSS. The website consists of three pages which are stored in **[`templates`](Application/templates)** :

- **[`first.html`](Application/templates/first.html)**: The landing page where users input their skills.
- **[`second.html`](Application/templates/second.html)**: A page that displays summarized job market insights.
- **[`Job_details.html`](Application/templates/job_details.html)**: A page presenting detailed job posting information.

### 💾Backend Integration

The Flask application **[`app.py`](Application/app.py)** handles user inputs and connects the front end to the back end. It enables users to interact with the data, explore insights, and retrieve specific job details.

## Additional Files

- **[`Job Analytics.pptx`](JOB%20ANALYTICS.pptx)**: A presentation summarizing the project's details and key insights.

<br>

## 🤩Website Overview
**Landing Page**
- The landing page serves as the entry point for users. It's where users can input their skills and interests to explore job market insights.

<p align="center"> 
  <img src="https://user-images.githubusercontent.com/137817362/267758828-92c5904b-432c-4b54-9028-54b79d5c8d32.png" style="display: inline-block; margin: 0 auto; width:800px;">
</p>

**Summarized Insights Page**
- The summarized insights page presents users with key information about the job market based on their input.
<p align="center"> 
   <img src="https://github.com/AmarjeetRoy/InstaHyre-Job-Analytics-Machine-Learning-/assets/137817362/9a133c9b-3ba2-458a-a585-a5d8036827f9" style="display: inline-block; margin: 0 auto; width:800px;">  
</p>

**Job Posting Details Page**
- Detailed information about individual job postings, including job title, company name, location, required skills, and HR contact details.
<p align="center"> 
   <img src="https://github.com/AmarjeetRoy/InstaHyre-Job-Analytics-Machine-Learning-/assets/137817362/74d7f80d-5e05-441d-849e-252ee78c636e" style="display: inline-block; margin: 0 auto; width:1000px;">  
</p>

<br>

## 📝Key Findings

1. **Experience Level**: "Mid-Level" is the most common experience level in job postings.

2. **Top Industries**: IT, Finance, Healthcare, and Engineering are the leading industries.

3. **Company Size**: Companies with 100-500 employees have the most job listings.

4. **In-Demand Skills**: Python, Java, SQL, and Data Analysis are highly sought after.

5. **Job Type**: Full-time positions dominate job postings.

6. **HR Contact**: HR contact information is available for direct communication.

7. **Clustered Companies**: Companies are categorized using K-means clustering based on employee count and LinkedIn followers.

<br>

## 💼Project Summary

The Instahyre Job Analytics project involved web scraping job posting data from Instahyre, followed by data preprocessing and clustering analysis. It culminated in the development of an interactive web application for users to explore job market insights.

### 💡Key Learnings

- Automating web scraping for data acquisition.
- Data preprocessing and clustering analysis techniques.
- Web development for user-friendly data presentation.

### 🪨Challenges

- Ensuring data consistency and accuracy.
- Developing and fine-tuning the clustering model.
- Creating an interactive web application.
- Handling large data volumes while considering data privacy.

In summary, the project successfully provided insights into the job market through data analysis and web development, despite various data-related challenges.🙏🏻
