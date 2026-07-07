# Dashboard Design Specification

This is the page-by-page build guide for assembling `HR_Analytics_Dashboard.pbix` in Power BI Desktop from `HR_Employee_Data.csv` + the DAX measures and Power Query steps in this folder.

## Data Model (Star Schema)
```
                     ┌───────────────┐
                     │   DateTable   │  (dimension, hidden Date/Year/Month/Quarter)
                     │  (Date PK)    │
                     └───────┬───────┘
                        1 │ * (active: HireDate)
                        1 │ * (inactive: ExitDate, via USERELATIONSHIP)
                             │
                     ┌───────┴───────┐
                     │HR_Employee_Data│  (fact table, 5,400 rows)
                     │  EmployeeID PK │
                     └───────┬───────┘
                             │ * : 1 (disconnected, slicer only)
                     ┌───────┴───────┐
                     │ MetricSelector │  (disconnected table for dynamic KPI card)
                     └───────────────┘
```
**Why one fact table, not a normalized snowflake:** at 5,400 rows and 38 columns, splitting Department/JobRole/Location into separate dimension tables adds modeling overhead without a performance benefit at this scale. The single denormalized fact table plus a proper Date dimension is the right level of "star schema" for this dataset size — over-normalizing a dataset this small is itself an anti-pattern reviewers will flag. Relationships: DateTable[Date] (1) → HR_Employee_Data[HireDate] (*, active) and DateTable[Date] (1) → HR_Employee_Data[ExitDate] (*, inactive, activated via USERELATIONSHIP in time-intelligence measures). Filter direction: single, Date → Fact.

## Page 1 — Executive Overview
- **KPI cards (top row):** Total Employees (5,400) · Active Employees (4,420) · Attrition Rate (18.15%) · Average Salary ($98,984) · Average Tenure (5.59 yrs)
- **Slicers:** Department, Business Unit, Year (HireDate)
- **Line chart:** Monthly hiring trend vs. monthly resignation trend (dual-line, DateTable[MonthName] on axis)
- **Map:** Headcount by Country/City (bubble size = headcount)
- **Bar chart:** Headcount by Department
- **Dynamic title:** "Executive Overview — [Selected Department / All Departments]"

## Page 2 — Attrition Analysis
- **Bar chart:** Attrition Rate by Department (Sales highest at 23.7%)
- **Bar chart:** Attrition Rate by Gender (near-parity: 18.1% F vs 18.2% M)
- **Column chart:** Attrition Rate by Age Group (18-25 and 26-30 both ~28%, more than double the 31-50 bands)
- **Bar chart:** Attrition Rate by Education Field
- **Bar/Line combo:** Attrition Rate by Salary Quartile (22.2% → 14.9%, Q1 to Q4)
- **Donut chart:** Reason for Leaving (Better Opportunity 21.1% is the top reason)
- **Heatmap (Matrix with conditional formatting):** Department × Job Role attrition rate
- **Card:** Overtime Attrition Gap measure (+15.4 points)
- **Drill-through page:** "Role Detail" — right-click a job role to see its full attrition/salary/tenure profile

## Page 3 — Employee Demographics
- **Donut chart:** Gender distribution (50/50)
- **Column chart:** Age group distribution
- **Bar chart:** Education level distribution
- **Treemap:** Headcount by Department → Job Role
- **Map:** Employees by location
- **Bar chart:** Marital status distribution

## Page 4 — Performance Analysis
- **Column chart:** Performance rating distribution (59% rate "3 - Meets Expectations")
- **Bar chart:** Average training hours by department (range 42.5–44.1 hrs, IT highest)
- **Scatter chart:** Training Hours (x) vs Performance Rating (y), sized by headcount
- **Bar chart:** Promotion rate by department
- **Matrix:** Manager → average performance rating, average tenure
- **KPI card:** Promotion Rate (13.5%) with conditional color

## Page 5 — Salary Dashboard
- **Bar chart:** Average salary by department (IT $121,057 → Customer Support $74,015)
- **Box-and-whisker style (or ribbon chart):** Salary distribution by job level
- **Bar chart:** Average bonus by department
- **Line chart:** Average monthly income trend by hire year (salary growth for new hires over time)
- **Card group:** Bonus as % of salary (11.97%)

## Page 6 — Executive Insights
- Static/curated text boxes + summary KPI cards pulling from `reports/Business_Insights.md`
- **Key findings visual (table):** top 5 insights with supporting numbers
- **Recommendations panel:** action items mapped to each insight
- **Navigation buttons** back to Pages 1–5

## Power BI Features to Demonstrate
| Feature | Where used |
|---|---|
| Bookmarks | Toggle between "All Departments" and "Sales Only" views on Page 1 |
| Navigation buttons | Page 6 → back to Pages 1-5; consistent header nav bar on all pages |
| Dynamic titles | Page 1 and Page 2 titles change based on slicer selection (measures #25, #37) |
| Conditional formatting | KPI cards (measure #26), Department × Role heatmap on Page 2 |
| Tooltips | Custom tooltip page showing Department detail on hover over map bubbles |
| Drill-through | Page 2 → Role Detail page |
| Sync slicers | Department and Business Unit slicers synced across Pages 1–5 |
| Custom theme | Corporate theme JSON (navy/teal palette) applied via View → Themes → Browse for themes |
| Row-Level Security | See Bonus Features in README — RLS role suggested by BusinessUnit for regional HR partners |

## Visual Selection Rationale
- **Cards** for single-number KPIs — fastest to scan.
- **Bar (not pie) charts** for department/role comparisons — more than 4 categories makes pie charts hard to compare; used donut charts only for true part-of-whole breakdowns with ≤5 categories (gender, reason for leaving).
- **Line charts** for time trends (hiring/resignation) — trend direction is the point, not exact values.
- **Treemap** for Department→Role hierarchy — shows both proportion and hierarchy in one visual.
- **Matrix + conditional formatting** as heatmap — avoids needing a custom visual for a Department×Role grid.
- **Scatter** for Training Hours vs Performance — reveals correlation, not just individual averages.
