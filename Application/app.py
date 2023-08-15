import numpy as np
import pandas as pd
from collections import Counter
from flask import Flask, request, render_template
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd

app = Flask(__name__)
import re
df=pd.read_csv(r"C:\Users\AMARJEET\Desktop\Masai\UNIT 5\ML Project\Instahyre Job Analysis\Application\Processed_file.csv")
skills = [i.strip() for i in list(set(','.join(df['Skills']).split(',')))]
df['Skills'].str.lower().str.split(',')






def data_frame(x):
#   x = ' pyThon , abc, jaVa , SQL, xyz' 
    x = [i.strip() for i in x.lower().split(',')]   
#   x = ['python', 'abc', 'java', 'sql', 'xyz']

    y = df['Skills'].str.lower().str.split(',')

    indices = []
    missing_skills = []

    for skill in x:
        skill_found = False
        for j in range(len(y)):
            if skill in y[j]:
                indices.append(j)
                skill_found = True
        if not skill_found:
            missing_skills.append(skill)

    if missing_skills:
        missing_skill_msg = ', '.join(missing_skills)
        missing_msg = f'There is no job for {missing_skill_msg}.'
        if len(indices) < 1:
            return missing_msg
        else:
            print(missing_msg)  # Print the missing skill message


    indices = sorted(list(set(indices)))

    df1 = df[df.index.isin(indices)]
    if len(df1) < 1:
        return 'There are no jobs for these skills'
    else:
        return df1


@app.route('/')
def index():
    return render_template("first.html")


@app.route('/final_output', methods=['POST'])


def final_output():
    if request.method == 'POST':
        x = request.form.get("Traas")
        df_result = data_frame(x)  # Pass 'x' as an argument to the function
        if isinstance(df_result, str):
            return df_result
        else:
            exp_level = df_result['level'].mode()[0]
            industry = df_result['Industry'].mode()[0]
            company_class = df_result['class'].mode()[0]
            job_count = df_result['Sr No.'].count()
            return render_template("second.html",
                                   skill=x,
                                   experience_level=exp_level,
                                   industry=industry,
                                   job_class=f"{company_class}",
                                   job_count=job_count)


@app.route('/job_details/<s_id>', methods=['GET'])
def job_details(s_id):
    skill = s_id
    job_data = data_frame(skill)
    job_data=job_data[['Company Name','Designation',"Skills",'Location','Experience']]
    job_data=job_data.to_html(render_links=True, classes='table table-bordered', index=False)  # Filter the data based on the provided skill   
    return render_template("job_details.html", job_data=job_data)

if __name__ == "__main__":
    app.run(debug=True)