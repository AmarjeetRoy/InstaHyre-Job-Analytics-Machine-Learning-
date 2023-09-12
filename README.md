# Instahyre Job Analytics

Welcome to the **Instahyre Job Analytics** repository! This project offers insightful analysis and visualization of the job market trends, gathered through web scraping and data analysis.

## Project Overview

The **Instahyre Job Analytics** project revolves around comprehensively understanding the job market dynamics using data-driven insights. Our team, consisting of dedicated members, embarked on a journey to extract, preprocess, and analyze job posting data from Instahyre and LinkedIn, shedding light on the employment landscape.

## Team Members

- Amarjeet Roy
- Priya Bhardwaj
- Ajay Kumar
- Bharat Sharma

## Aim

The project's scope was divided into two core segments:

1. **Data Extraction and Preprocessing:**
   - We utilized the Selenium library to extract job posting data from Instahyre's website.
   - The `Extraction` directory contains the extraction script `Extraction_Code.py` and extracted CSV files.
   - The `Processing` directory features `Data Preprocessing and Clustering.ipynb` for data cleaning and K-means clustering.

2. **Interactive Website:**
   - To visualize insights, we built an interactive website using Flask, HTML, and CSS.
   - Users can input their skills, explore summarized job details, and dive into comprehensive job postings.
   - The `Application` directory houses the website's code, templates, and processed data.

## Key Components

- `Extraction` Directory: Web scraping code and extracted data.
- `Processing` Directory: Data preprocessing and K-means clustering notebooks.
- `Application` Directory: Flask application and interactive website templates.
- `Processed_file.csv`: Processed data with class information for website display.

## Repository Structure
- `Extraction`: Directory containing code and files related to web scraping and data extraction.
  - `Extraction_Code.py`: Python script for web scraping job posting data and LinkedIn information.
  - `Job webLink.csv`: Contains web links of all job pages.
  - `merged Data.csv`: Merged data from Instahyre and LinkedIn.
  - `New Updated Csv.csv`: Preprocessed data with some initial modifications.
  - `Table`: Directory containing tables created from extracted data.
    - `jobs.csv`: Contains job-related information with attributes `job_id`, `company_id`, `location`, `designation`, and `details_id`.
    - `company.csv`: Contains company-related information with attributes `company_id`, `name`, `estab_year`, and `employees_count`.
    - `details.csv`: Contains job details with attributes `details_id`, `involvement`, `skills`, and `hr_name`.
    - `merged Data.csv`: Merged data from Instahyre and LinkedIn.

- `Processing`: Directory containing code and files related to data preprocessing and clustering.
  - `Data Preprocessing and Clustering.ipynb`: Jupyter Notebook containing data preprocessing and building the K-means clustering model using Python libraries.
  - `Processed_file.csv`: Processed data with class information and details for display on the website.
  - `New Updated Csv.csv`: Preprocessed data with some initial modifications.
  

- `Application`: Directory containing the code for the interactive website.
  - `app.py`: Flask application to handle user inputs and serve web pages.
  - `templates`: Directory containing HTML templates for the website pages.
    - `first.html`: Landing page for user input.
    - `second.html`: Page displaying summarized job market insights.
    - `Job_details.html`: Page showing detailed job posting information.
  - `Processed_file.csv`: Processed data with class information and details for display on the website.

- `Job Analytics Presentation.pptx`: Presentation showcasing project details and insights.
  
- `README.md`: This file, providing an overview of the project, its structure, and usage instructions.


## Visuals
<p align="center"> 
  <img src="https://user-images.githubusercontent.com/137817362/267353293-27d23cde-2fb6-49b6-98e4-2720931bb80c.png" style="display: inline-block; margin: 0 auto; width:600px;">

   <br>
   <img src="https://user-images.githubusercontent.com/137817362/267353688-45a6e12d-ee36-4c28-9b64-043621a4a833.png" style="display: inline-block; margin: 0 auto; width:600px;">  
</p>

## Key Findings
1. **Most Common Experience Level**: The analysis reveals that "Mid-Level" is the most frequently required experience level for job postings, indicating a substantial number of opportunities in this category.

2. **Top Industries**: The dominant industry in the job market is Information Technology (IT), followed by Finance, Healthcare, and Engineering.

3. **Company Size and Job Availability**: Companies with moderate employee counts, such as 100-500 employees, have the highest number of job listings. This suggests that mid-sized companies offer significant employment opportunities.

4. **In-Demand Skills**: Key skills like Python, Java, SQL, and Data Analysis are highly sought after in job postings.

5. **Types of Involvement**: Full-time positions are the most common, reflecting a strong preference for full-time employment.

6. **HR Contact Information**: HR personnel contact information is available, enabling direct communication between job seekers and hiring managers.

7. **Clustered Companies**: The project utilizes K-means clustering to categorize companies based on employee count and LinkedIn followers, aiding job seekers in targeting companies aligned with their career goals.

8. **User-Friendly Web Interface**: The project offers an interactive web interface for users to input their skills and receive summarized insights, including the most common experience level, top industries, and predominant company size in their field of interest.


## Challeneges and Learnings 


## Usage

1. Explore the extracted data and preprocessing steps in the `Extraction` and `Processing` directories.
2. Dive into the interactive website in the `Application` directory, run `app.py`, and visit the local server.
3. Gain insights into job market trends, industry preferences, and job posting details.

## Acknowledgments

Special thanks to the project providers for entrusting us with this opportunity. We also extend our gratitude to the supportive mentors and faculty members.

Thank you for your interest in the **Instahyre Job Analytics** project!

