import pandas as pd
import numpy as np

df = pd.read_csv("/home/claude/HR-Analytics-Dashboard/dataset/HR_Employee_Data.csv")

def pct(x, n=1):
    return f"{x*100:.{n}f}%"

print("=== HEADLINE ===")
total = len(df)
attr_yes = (df.Attrition=="Yes").sum()
attr_rate = attr_yes/total
print("Total employees:", total)
print("Attrition count:", attr_yes, pct(attr_rate,2))
print("Active employees:", total-attr_yes)

print("\n=== BY DEPARTMENT ===")
dept = df.groupby("Department").agg(headcount=("EmployeeID","count"),
    attrition_rate=("Attrition", lambda x:(x=="Yes").mean()),
    avg_salary=("Salary","mean")).sort_values("attrition_rate", ascending=False)
print(dept.round(2))

print("\n=== BY JOB ROLE (top attrition) ===")
role = df.groupby("JobRole").agg(headcount=("EmployeeID","count"),
    attrition_rate=("Attrition", lambda x:(x=="Yes").mean())).sort_values("attrition_rate", ascending=False)
print(role.round(3))

print("\n=== ATTRITION SHARE CONCENTRATION (Pareto check) ===")
role_attr_counts = df[df.Attrition=="Yes"].groupby("JobRole").size().sort_values(ascending=False)
cum_share = (role_attr_counts.cumsum()/role_attr_counts.sum())
print(role_attr_counts)
print(cum_share.round(3))
n_roles_80 = (cum_share <= 0.80).sum() + 1
print(f"Roles needed to reach ~80% of all attrition: {n_roles_80} of {role_attr_counts.shape[0]} roles")

print("\n=== AGE GROUP ATTRITION ===")
bins = [18,25,30,35,40,45,50,60]
labels = ["18-25","26-30","31-35","36-40","41-45","46-50","51-60"]
df["AgeGroup"] = pd.cut(df.Age, bins=bins, labels=labels, right=True)
age = df.groupby("AgeGroup", observed=True).agg(headcount=("EmployeeID","count"),
    attrition_rate=("Attrition", lambda x:(x=="Yes").mean()))
print(age.round(3))

print("\n=== OVERTIME vs ATTRITION ===")
ot = df.groupby("OverTime").agg(headcount=("EmployeeID","count"),
    attrition_rate=("Attrition", lambda x:(x=="Yes").mean()))
print(ot.round(3))

print("\n=== SALARY QUARTILE vs ATTRITION ===")
df["SalaryQuartile"] = pd.qcut(df.Salary, 4, labels=["Q1 (Lowest)","Q2","Q3","Q4 (Highest)"])
sal = df.groupby("SalaryQuartile", observed=True).agg(headcount=("EmployeeID","count"),
    attrition_rate=("Attrition", lambda x:(x=="Yes").mean()))
print(sal.round(3))

print("\n=== GENDER DISTRIBUTION ===")
print(df.Gender.value_counts(normalize=True).round(3))
print(df.groupby("Gender").agg(attrition_rate=("Attrition", lambda x:(x=="Yes").mean())).round(3))

print("\n=== EDUCATION FIELD vs PERFORMANCE ===")
edu = df.groupby("EducationField").agg(avg_perf=("PerformanceRating","mean"),
    headcount=("EmployeeID","count")).sort_values("avg_perf", ascending=False)
print(edu.round(2))

print("\n=== PROMOTIONS ===")
promo = df.PromotionLastYear.value_counts()
print(promo)
promo_attr = df.groupby("PromotionLastYear").agg(attrition_rate=("Attrition", lambda x:(x=="Yes").mean()))
print(promo_attr.round(3))

print("\n=== TENURE & EXPERIENCE ===")
print("Avg tenure (years):", round(df.YearsAtCompany.mean(),2))
print("Avg experience (years):", round(df.Experience.mean(),2))
print("Median tenure:", round(df.YearsAtCompany.median(),2))

print("\n=== TRAINING HOURS BY DEPARTMENT ===")
train = df.groupby("Department").TrainingHours.mean().sort_values(ascending=False)
print(train.round(1))

print("\n=== PERFORMANCE DISTRIBUTION ===")
print(df.PerformanceRating.value_counts(normalize=True).sort_index().round(3))

print("\n=== HIRING TREND (by month number, seasonality) ===")
df["HireMonth"] = pd.to_datetime(df.HireDate).dt.month
print(df.HireMonth.value_counts(normalize=True).sort_index().round(3))

print("\n=== RESIGNATION TREND (by month number) ===")
exits = df[df.Attrition=="Yes"].copy()
exits["ExitMonth"] = pd.to_datetime(exits.ExitDate).dt.month
print(exits.ExitMonth.value_counts(normalize=True).sort_index().round(3))

print("\n=== REMOTE vs OFFICE ===")
print(df.RemoteWork.value_counts(normalize=True).round(3))
print(df.groupby("RemoteWork").agg(attrition_rate=("Attrition", lambda x:(x=="Yes").mean())).round(3))

print("\n=== SATISFACTION AVERAGES ===")
print("Avg job satisfaction:", round(df.JobSatisfaction.mean(),2))
print("Avg env satisfaction:", round(df.EnvironmentSatisfaction.mean(),2))
print("Avg work-life balance:", round(df.WorkLifeBalance.mean(),2))

print("\n=== WORK LIFE BALANCE vs ATTRITION ===")
print(df.groupby("WorkLifeBalance").agg(attrition_rate=("Attrition", lambda x:(x=="Yes").mean())).round(3))

print("\n=== TOP DEPT SALARY ===")
print(df.groupby("Department").Salary.mean().sort_values(ascending=False).round(0))

print("\n=== LOCATIONS BY HEADCOUNT ===")
print(df.groupby(["Country","City"]).size().sort_values(ascending=False).head(10))

print("\n=== REASON FOR LEAVING ===")
print(exits.ReasonForLeaving.value_counts(normalize=True).round(3))

print("\n=== BONUS & SALARY GROWTH proxy ===")
print("Avg bonus:", round(df.Bonus.mean(),0))
print("Avg bonus as % of salary:", pct((df.Bonus/df.Salary).mean(),2))

print("\n=== ABSENTEEISM vs JOB SAT ===")
print(df.groupby("JobSatisfaction").Absenteeism.mean().round(2))

print("\n=== DISTANCE FROM HOME vs ATTRITION ===")
df["DistBucket"] = pd.cut(df.DistanceFromHome, [0,5,10,20,50], labels=["0-5","6-10","11-20","21+"])
print(df.groupby("DistBucket", observed=True).agg(attrition_rate=("Attrition", lambda x:(x=="Yes").mean())).round(3))
