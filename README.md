# Instahyre Job Analytics

Welcome to the **Instahyre Job Analytics** repository! This project offers insightful analysis and visualization of the job market trends, gathered through web scraping and data analysis.

## Project Overview

The **Instahyre Job Analytics** project revolves around comprehensively understanding the job market dynamics using data-driven insights. Our team, consisting of dedicated members, embarked on a journey to extract, preprocess, and analyze job posting data from Instahyre and LinkedIn, shedding light on the employment landscape.

## Team Members

- Amarjeet Roy
- Priya Bhardwaj
- Ajay Kumar
- Bharat Sharma

## Project Scope

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


## Usage

1. Explore the extracted data and preprocessing steps in the `Extraction` and `Processing` directories.
2. Dive into the interactive website in the `Application` directory, run `app.py`, and visit the local server.
3. Gain insights into job market trends, industry preferences, and job posting details.

## Acknowledgments

Special thanks to the project providers for entrusting us with this opportunity. We also extend our gratitude to the supportive mentors and faculty members.

Thank you for your interest in the **Instahyre Job Analytics** project!

