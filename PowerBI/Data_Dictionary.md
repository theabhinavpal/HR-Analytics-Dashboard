# Data Dictionary — HR_Employee_Data.csv

5,400 rows × 38 columns. One row = one employee record (active or exited).

| Field | Type | Description | Example |
|---|---|---|---|
| EmployeeID | Text | Unique employee identifier | EMP10001 |
| EmployeeName | Text | Full name (synthetic) | Sarah Johnson |
| Gender | Text | Male / Female | Female |
| Age | Integer | Age in years (21–60) | 34 |
| MaritalStatus | Text | Single / Married / Divorced | Married |
| Education | Text | High School / Bachelor's / Master's / PhD | Bachelor's |
| EducationField | Text | Field of study | Computer Science |
| Department | Text | One of 8 departments | Sales |
| JobRole | Text | Specific role within department | Sales Executive |
| JobLevel | Integer | Seniority level, 1 (entry) – 5 (executive) | 2 |
| BusinessUnit | Text | Regional business unit | EMEA |
| Manager | Text | Manager ID | Mgr-045 |
| City / State / Country | Text | Work location | Berlin / Berlin / Germany |
| Salary | Integer | Annual base salary (USD) | 78,000 |
| Bonus | Integer | Annual bonus (USD) | 9,200 |
| MonthlyIncome | Decimal | Salary ÷ 12 | 6,500.00 |
| Experience | Decimal | Total years of professional experience | 9.5 |
| YearsAtCompany | Decimal | Tenure at this company | 5.6 |
| YearsInCurrentRole | Decimal | Years in current role | 2.1 |
| PromotionLastYear | Text | Yes/No — promoted in the last 12 months | No |
| TrainingHours | Integer | Training hours completed (annual) | 42 |
| PerformanceRating | Integer | 1 (low) – 4 (high) | 3 |
| JobSatisfaction | Integer | 1 (low) – 4 (high) | 3 |
| EnvironmentSatisfaction | Integer | 1 (low) – 4 (high) | 4 |
| WorkLifeBalance | Integer | 1 (poor) – 4 (excellent) | 3 |
| OverTime | Text | Yes/No — regularly works overtime | Yes |
| RemoteWork | Text | Remote / Hybrid / Onsite | Hybrid |
| EmploymentType | Text | Full-Time / Contract / Part-Time | Full-Time |
| HireDate | Date | Date of hire | 2019-09-14 |
| ExitDate | Date | Date of exit (blank if still active) | 2024-06-02 |
| Attrition | Text | Yes/No — has the employee left | No |
| ReasonForLeaving | Text | Populated only if Attrition = Yes | Compensation |
| TravelFrequency | Text | No Travel / Rarely / Frequently | Rarely |
| DistanceFromHome | Integer | Commute distance in km | 12 |
| Absenteeism | Integer | Unplanned absence days (annual) | 5 |
| LeaveBalance | Integer | Remaining leave days | 14 |

## Notes on data generation
This is a fully synthetic dataset (no real employee data), generated in Python/pandas with engineered — not random — business patterns so every insight in this repo has a defensible, reproducible ground truth:

- **Attrition is driven by a weighted model**, not a coin flip: overtime, low job satisfaction, low work-life balance, younger age, and specific job roles (Sales Executive, Sales Representative, Support Representative) each add measurable probability; promotions and long tenure reduce it.
- **Pareto concentration**: attrition is concentrated in a minority of job roles — 18 of 27 roles (67%) account for ~80% of all resignations, with Sales Representative and Sales Executive alone contributing 18% of total attrition.
- **Departmental salary differentiation**: base salary bands differ by department (IT and R&D pay the most, Customer Support the least) and scale with job level (1×–3× multiplier).
- **Seasonality**: hiring peaks in January (new budget cycles) and September (post-summer hiring), and dips in June/December; resignations spike in January/February (post-bonus-payout exits) and June.
