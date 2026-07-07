# KPI Definitions

Each KPI below is defined the way it should appear on the Executive Overview page, with its actual current value computed from `HR_Employee_Data.csv` so you can validate your Power BI build against a known-correct number.

| KPI | Formula (business logic) | Current Value |
|---|---|---|
| Total Employees | Count of all employee records | 5,400 |
| Active Employees | Count where Attrition = "No" | 4,420 |
| Attrition Count | Count where Attrition = "Yes" | 980 |
| Attrition Rate | Attrition Count ÷ Total Employees | 18.15% |
| Average Salary | Mean(Salary) | $98,984 |
| Average Bonus | Mean(Bonus) | $11,850 |
| Average Age | Mean(Age) | 38.9 |
| Average Tenure | Mean(YearsAtCompany) | 5.59 years |
| Average Experience | Mean(Experience) | 9.69 years |
| Average Performance Rating | Mean(PerformanceRating) | 2.98 / 4 |
| Average Job Satisfaction | Mean(JobSatisfaction) | 2.93 / 4 |
| Average Environment Satisfaction | Mean(EnvironmentSatisfaction) | 2.91 / 4 |
| Average Work-Life Balance | Mean(WorkLifeBalance) | 2.99 / 4 |
| Average Training Hours | Mean(TrainingHours) | 43.5 hrs |
| Promotion Rate (last 12 mo.) | Promoted Count ÷ Eligible Headcount | 13.5% |
| Overtime Attrition Gap | Attrition Rate (OT=Yes) − Attrition Rate (OT=No) | 28.6% vs 13.2% (+15.4 pts) |
| Highest-Attrition Department | Department with max attrition rate | Sales (23.7%) |
| Highest-Paying Department | Department with max avg salary | IT ($121,057) |
| Top Resignation Reason | Mode(ReasonForLeaving) | Better Opportunity (21.1%) |

## KPI Targets / Thresholds (for conditional formatting)
- Attrition Rate: Green ≤ 12%, Yellow 12–18%, Red > 18%
- Work-Life Balance avg: Green ≥ 3.2, Yellow 2.6–3.2, Red < 2.6
- Job Satisfaction avg: Green ≥ 3.2, Yellow 2.6–3.2, Red < 2.6
- Promotion Rate: Green ≥ 12%, Yellow 8–12%, Red < 8%

These thresholds are illustrative business targets for conditional formatting demos — adjust to your organization's actual policy when presenting this as a real dashboard.
