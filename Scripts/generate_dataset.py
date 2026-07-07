import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

N = 5400

departments = ["Sales", "Research & Development", "Human Resources", "Finance", "IT", "Operations", "Marketing", "Customer Support"]
dept_weights = [0.22, 0.20, 0.06, 0.10, 0.14, 0.13, 0.08, 0.07]

job_roles_by_dept = {
    "Sales": ["Sales Executive", "Sales Manager", "Account Manager", "Sales Representative"],
    "Research & Development": ["Research Scientist", "Research Director", "Lab Technician", "Data Scientist"],
    "Human Resources": ["HR Specialist", "HR Manager", "Recruiter"],
    "Finance": ["Financial Analyst", "Finance Manager", "Accountant"],
    "IT": ["Software Engineer", "IT Support Specialist", "DevOps Engineer", "IT Manager"],
    "Operations": ["Operations Analyst", "Operations Manager", "Logistics Coordinator"],
    "Marketing": ["Marketing Specialist", "Marketing Manager", "Content Strategist"],
    "Customer Support": ["Support Representative", "Support Team Lead", "Customer Success Manager"],
}

business_units = ["North America", "EMEA", "APAC", "LATAM"]
locations = {
    "North America": [("New York", "NY", "USA"), ("Chicago", "IL", "USA"), ("Austin", "TX", "USA")],
    "EMEA": [("London", "England", "UK"), ("Berlin", "Berlin", "Germany"), ("Dublin", "Leinster", "Ireland")],
    "APAC": [("Singapore", "Singapore", "Singapore"), ("Bangalore", "Karnataka", "India"), ("Sydney", "NSW", "Australia")],
    "LATAM": [("Sao Paulo", "SP", "Brazil"), ("Mexico City", "CDMX", "Mexico")],
}

education_levels = ["High School", "Bachelor's", "Master's", "PhD"]
education_fields = ["Life Sciences", "Medical", "Marketing", "Technical Degree", "Human Resources", "Business", "Computer Science", "Other"]
marital_status_opts = ["Single", "Married", "Divorced"]
reasons_for_leaving = ["Better Opportunity", "Compensation", "Relocation", "Retirement", "Personal Reasons", "Work-Life Balance", "Career Change", "Termination"]

first_names_m = ["James","Michael","David","John","Robert","William","Daniel","Joseph","Matthew","Andrew","Ryan","Kevin","Brian","Jason","Eric","Raj","Arjun","Wei","Hiroshi","Carlos","Diego","Liam","Noah","Ethan"]
first_names_f = ["Mary","Patricia","Jennifer","Linda","Elizabeth","Susan","Jessica","Sarah","Karen","Nancy","Priya","Anita","Mei","Yuki","Maria","Sofia","Emma","Olivia","Ava","Isabella","Laura","Anna"]
last_names = ["Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis","Rodriguez","Martinez","Wilson","Anderson","Taylor","Thomas","Moore","Jackson","Martin","Lee","Perez","Thompson","White","Harris","Sanchez","Clark","Ramirez","Lewis","Robinson","Walker","Young","Allen","King","Wright","Scott","Torres","Nguyen","Hill","Flores","Green","Adams","Nelson"]

def rand_name():
    gender = random.choice(["Male", "Female"])
    first = random.choice(first_names_m if gender == "Male" else first_names_f)
    last = random.choice(last_names)
    return f"{first} {last}", gender

# Department base salary multipliers (margin/salary differences by dept)
dept_salary_base = {
    "Sales": 62000, "Research & Development": 78000, "Human Resources": 58000,
    "Finance": 75000, "IT": 82000, "Operations": 60000, "Marketing": 65000, "Customer Support": 52000,
}

job_level_multiplier = {1: 1.0, 2: 1.3, 3: 1.7, 4: 2.3, 5: 3.0}

# Hiring seasonality: more hires in Jan (new budget) and Sep (post-summer), fewer in Jun/Dec
hire_month_weights = np.array([1.4, 1.1, 1.0, 0.9, 0.8, 0.6, 0.8, 0.9, 1.5, 1.2, 1.0, 0.6])
hire_month_weights = hire_month_weights / hire_month_weights.sum()

start_range = pd.date_range("2016-01-01", "2025-12-31", freq="D")

records = []
today = datetime(2026, 6, 30)

for i in range(1, N + 1):
    emp_id = f"EMP{10000 + i}"
    name, gender = rand_name()
    dept = np.random.choice(departments, p=dept_weights)
    role = random.choice(job_roles_by_dept[dept])
    bu = random.choice(business_units)
    city, state, country = random.choice(locations[bu])

    job_level = np.random.choice([1,2,3,4,5], p=[0.35,0.30,0.20,0.10,0.05])
    age = int(np.clip(np.random.normal(35 + job_level*2, 8), 21, 60))

    # hire date w/ seasonality
    hire_year = np.random.choice(range(2016, 2026), p=None)
    hire_month = np.random.choice(range(1,13), p=hire_month_weights)
    hire_day = np.random.randint(1, 28)
    hire_date = datetime(int(hire_year), int(hire_month), int(hire_day))
    if hire_date > today:
        hire_date = today - timedelta(days=random.randint(30, 900))

    years_at_company = round((today - hire_date).days / 365.25, 1)
    experience = round(years_at_company + max(0, np.random.normal(4, 3)), 1)
    years_in_role = round(min(years_at_company, max(0.2, np.random.exponential(2.2))), 1)

    education = np.random.choice(education_levels, p=[0.08, 0.45, 0.37, 0.10])
    edu_field = random.choice(education_fields)
    marital = np.random.choice(marital_status_opts, p=[0.42, 0.45, 0.13])

    overtime = np.random.choice(["Yes", "No"], p=[0.30, 0.70])
    remote = np.random.choice(["Remote", "Hybrid", "Onsite"], p=[0.20, 0.45, 0.35])
    employment_type = np.random.choice(["Full-Time", "Contract", "Part-Time"], p=[0.86, 0.09, 0.05])

    distance = int(np.clip(np.random.exponential(9), 1, 45))
    travel = np.random.choice(["No Travel", "Rarely", "Frequently"], p=[0.30, 0.55, 0.15])

    # Job & environment satisfaction (1-4), work-life balance (1-4)
    job_sat = np.random.choice([1,2,3,4], p=[0.12,0.18,0.35,0.35])
    env_sat = np.random.choice([1,2,3,4], p=[0.10,0.20,0.38,0.32])
    wlb = np.random.choice([1,2,3,4], p=[0.10 if overtime=="Yes" else 0.05,
                                          0.30 if overtime=="Yes" else 0.15,
                                          0.40, 0.20 if overtime=="Yes" else 0.40])

    perf_rating = np.random.choice([1,2,3,4], p=[0.03, 0.17, 0.60, 0.20])
    training_hours = int(np.clip(np.random.normal(35 + (perf_rating*3), 15), 0, 100))

    base = dept_salary_base[dept] * job_level_multiplier[job_level]
    salary = round(base * np.random.normal(1.0, 0.10), -2)
    salary = max(salary, 30000)
    bonus = round(salary * np.random.uniform(0.03, 0.18) * (1 + 0.15*(perf_rating-2)), -1)
    monthly_income = round(salary / 12, 2)

    promotion_last_year = np.random.choice(["Yes", "No"], p=[0.14, 0.86]) if years_at_company >= 1 else "No"
    absenteeism = int(np.clip(np.random.poisson(4 + (4 - job_sat)), 0, 25))
    leave_balance = int(np.clip(np.random.normal(12, 5), 0, 30))

    # ----- Attrition model (Pareto-flavored: concentrated in a few roles/segments) -----
    attrition_score = 0.06  # base
    if overtime == "Yes":
        attrition_score += 0.16
    if age < 30:
        attrition_score += 0.10
    if job_sat <= 2:
        attrition_score += 0.12
    if wlb <= 2:
        attrition_score += 0.08
    if role in ["Sales Executive", "Support Representative", "Sales Representative"]:
        attrition_score += 0.14
    if job_level == 1:
        attrition_score += 0.06
    if promotion_last_year == "Yes":
        attrition_score -= 0.10
    if years_at_company > 8:
        attrition_score -= 0.07
    attrition_score = np.clip(attrition_score, 0.01, 0.85)

    attrition = np.random.choice(["Yes", "No"], p=[attrition_score, 1 - attrition_score])

    exit_date = ""
    reason_leaving = ""
    if attrition == "Yes":
        # exit seasonality similar shape but slightly shifted (more exits in Jan/Feb post-bonus, June)
        exit_month_weights = np.array([1.5, 1.3, 1.0, 0.9, 0.8, 1.2, 0.9, 0.8, 1.0, 0.9, 0.8, 0.7])
        exit_month_weights = exit_month_weights / exit_month_weights.sum()
        min_exit = hire_date + timedelta(days=90)
        if min_exit >= today:
            exit_dt = today - timedelta(days=random.randint(1,60))
        else:
            span_days = (today - min_exit).days
            exit_dt = min_exit + timedelta(days=random.randint(0, span_days))
            target_month = int(np.random.choice(range(1,13), p=exit_month_weights))
            exit_dt = exit_dt.replace(month=target_month, day=min(exit_dt.day, 28))
        exit_date = exit_dt.strftime("%Y-%m-%d")
        if job_sat <= 2 and wlb <= 2:
            reason_leaving = np.random.choice(reasons_for_leaving, p=[0.28,0.10,0.08,0.03,0.10,0.30,0.08,0.03])
        else:
            reason_leaving = np.random.choice(reasons_for_leaving, p=[0.22,0.18,0.15,0.08,0.12,0.10,0.10,0.05])

    records.append({
        "EmployeeID": emp_id,
        "EmployeeName": name,
        "Gender": gender,
        "Age": age,
        "MaritalStatus": marital,
        "Education": education,
        "EducationField": edu_field,
        "Department": dept,
        "JobRole": role,
        "JobLevel": job_level,
        "BusinessUnit": bu,
        "Manager": f"Mgr-{random.randint(1,120):03d}",
        "City": city,
        "State": state,
        "Country": country,
        "Salary": int(salary),
        "Bonus": int(bonus),
        "MonthlyIncome": monthly_income,
        "Experience": experience,
        "YearsAtCompany": years_at_company,
        "YearsInCurrentRole": years_in_role,
        "PromotionLastYear": promotion_last_year,
        "TrainingHours": training_hours,
        "PerformanceRating": perf_rating,
        "JobSatisfaction": job_sat,
        "EnvironmentSatisfaction": env_sat,
        "WorkLifeBalance": wlb,
        "OverTime": overtime,
        "RemoteWork": remote,
        "EmploymentType": employment_type,
        "HireDate": hire_date.strftime("%Y-%m-%d"),
        "ExitDate": exit_date,
        "Attrition": attrition,
        "ReasonForLeaving": reason_leaving,
        "TravelFrequency": travel,
        "DistanceFromHome": distance,
        "Absenteeism": absenteeism,
        "LeaveBalance": leave_balance,
    })

df = pd.DataFrame(records)
df.to_csv("/home/claude/HR-Analytics-Dashboard/dataset/HR_Employee_Data.csv", index=False)
print(df.shape)
print(df["Attrition"].value_counts(normalize=True))
print(df.groupby("Department")["Attrition"].apply(lambda x: (x=="Yes").mean()).sort_values(ascending=False))
