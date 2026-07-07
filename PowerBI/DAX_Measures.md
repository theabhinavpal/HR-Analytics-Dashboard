# DAX Measures

All measures reference the fact table `HR_Employee_Data` and, where noted, the `DateTable` dimension. Expected outputs are computed against the actual 5,400-row dataset in this repo.

---

### 1. Total Employees
**Purpose:** Core headcount KPI card.
```dax
Total Employees = COUNTROWS(HR_Employee_Data)
```
**Explanation:** Simple row count of the fact table.
**Expected output:** 5,400

---

### 2. Active Employees
**Purpose:** Current workforce size, excluding attrition.
```dax
Active Employees = CALCULATE([Total Employees], HR_Employee_Data[Attrition] = "No")
```
**Expected output:** 4,420

---

### 3. Attrition Count
**Purpose:** Numerator for attrition rate.
```dax
Attrition Count = CALCULATE([Total Employees], HR_Employee_Data[Attrition] = "Yes")
```
**Expected output:** 980

---

### 4. Attrition Rate
**Purpose:** Headline HR KPI — the % of the workforce that has left.
```dax
Attrition Rate = DIVIDE([Attrition Count], [Total Employees], 0)
```
**Explanation:** DIVIDE avoids divide-by-zero errors when a filter context returns no employees (e.g., a department with zero headcount).
**Expected output:** 18.15%

---

### 5. Average Salary
```dax
Average Salary = AVERAGE(HR_Employee_Data[Salary])
```
**Expected output:** $98,984

---

### 6. Average Experience
```dax
Average Experience = AVERAGE(HR_Employee_Data[Experience])
```
**Expected output:** 9.69 years

---

### 7. Average Age
```dax
Average Age = AVERAGE(HR_Employee_Data[Age])
```
**Expected output:** 38.9

---

### 8. Average Performance Rating
```dax
Average Performance Rating = AVERAGE(HR_Employee_Data[PerformanceRating])
```
**Expected output:** 2.98 / 4

---

### 9. Average Job Satisfaction
```dax
Average Job Satisfaction = AVERAGE(HR_Employee_Data[JobSatisfaction])
```
**Expected output:** 2.93 / 4

---

### 10. Average Work-Life Balance
```dax
Average Work-Life Balance = AVERAGE(HR_Employee_Data[WorkLifeBalance])
```
**Expected output:** 2.99 / 4

---

### 11. Average Training Hours
```dax
Average Training Hours = AVERAGE(HR_Employee_Data[TrainingHours])
```
**Expected output:** 43.5 hrs

---

### 12. Monthly Attrition (uses DateTable)
**Purpose:** Feeds the resignation trend line chart.
```dax
Monthly Attrition =
CALCULATE(
    [Attrition Count],
    USERELATIONSHIP(HR_Employee_Data[ExitDate], DateTable[Date])
)
```
**Explanation:** ExitDate is an inactive relationship to DateTable (HireDate is the active one); USERELATIONSHIP activates it just for this measure so exits are placed on the timeline by exit month, not hire month.

---

### 13. Yearly Attrition
```dax
Yearly Attrition =
CALCULATE(
    [Attrition Count],
    USERELATIONSHIP(HR_Employee_Data[ExitDate], DateTable[Date]),
    DATESYTD(DateTable[Date])
)
```

---

### 14. Department-wise Salary
```dax
Department Avg Salary = AVERAGE(HR_Employee_Data[Salary])
```
**Explanation:** identical formula to measure 5 — placed on a Department-sliced matrix/bar chart, context transition does the segmentation. (Kept as a separate named measure for dashboard clarity/tooltips.)
**Expected output (top 3):** IT $121,057 · R&D $112,011 · Finance $106,499

---

### 15. Average Tenure
```dax
Average Tenure = AVERAGE(HR_Employee_Data[YearsAtCompany])
```
**Expected output:** 5.59 years

---

### 16. Employee Growth (Net Headcount Change YTD)
```dax
Employee Growth =
CALCULATE([Total Employees], USERELATIONSHIP(HR_Employee_Data[HireDate], DateTable[Date]), DATESYTD(DateTable[Date]))
- CALCULATE([Attrition Count], USERELATIONSHIP(HR_Employee_Data[ExitDate], DateTable[Date]), DATESYTD(DateTable[Date]))
```

---

### 17. Hiring Rate
```dax
Hiring Rate =
DIVIDE(
    CALCULATE([Total Employees], USERELATIONSHIP(HR_Employee_Data[HireDate], DateTable[Date]), DATESYTD(DateTable[Date])),
    [Total Employees], 0
)
```

---

### 18. Promotion Rate
```dax
Promotion Rate = DIVIDE(
    CALCULATE([Total Employees], HR_Employee_Data[PromotionLastYear] = "Yes"),
    [Total Employees], 0
)
```
**Expected output:** 13.48%

---

### 19. Average Bonus
```dax
Average Bonus = AVERAGE(HR_Employee_Data[Bonus])
```
**Expected output:** $11,850

---

### 20. Bonus as % of Salary
```dax
Bonus Pct of Salary = DIVIDE([Average Bonus], [Average Salary], 0)
```
**Expected output:** 11.97%

---

### 21. Salary Growth (YoY, avg new hire salary vs prior year)
```dax
Salary Growth YoY =
VAR CurrentYearAvg = CALCULATE([Average Salary], USERELATIONSHIP(HR_Employee_Data[HireDate], DateTable[Date]), DATESYTD(DateTable[Date]))
VAR PriorYearAvg = CALCULATE([Average Salary], USERELATIONSHIP(HR_Employee_Data[HireDate], DateTable[Date]), SAMEPERIODLASTYEAR(DATESYTD(DateTable[Date])))
RETURN DIVIDE(CurrentYearAvg - PriorYearAvg, PriorYearAvg, 0)
```

---

### 22. Running Total — Cumulative Hires
```dax
Cumulative Hires =
CALCULATE(
    [Total Employees],
    USERELATIONSHIP(HR_Employee_Data[HireDate], DateTable[Date]),
    FILTER(ALLSELECTED(DateTable), DateTable[Date] <= MAX(DateTable[Date]))
)
```

---

### 23. Year-over-Year Growth (Headcount)
```dax
Headcount YoY Growth =
VAR CurrentYear = [Total Employees]
VAR PriorYear = CALCULATE([Total Employees], SAMEPERIODLASTYEAR(DateTable[Date]))
RETURN DIVIDE(CurrentYear - PriorYear, PriorYear, 0)
```

---

### 24. Previous Month Comparison (Attrition)
```dax
Attrition Prev Month =
CALCULATE(
    [Monthly Attrition],
    USERELATIONSHIP(HR_Employee_Data[ExitDate], DateTable[Date]),
    DATEADD(DateTable[Date], -1, MONTH)
)
```

---

### 25. Dynamic KPI Value (for a "Select a Metric" what-if slicer)
```dax
Selected KPI Value =
VAR Selection = SELECTEDVALUE(MetricSelector[Metric], "Attrition Rate")
RETURN
SWITCH(
    Selection,
    "Attrition Rate", [Attrition Rate],
    "Average Salary", [Average Salary],
    "Average Tenure", [Average Tenure],
    "Promotion Rate", [Promotion Rate],
    BLANK()
)
```
**Explanation:** `MetricSelector` is a small disconnected table (Metric column with the 4 label values) used to drive a dynamic single-card visual + dynamic title.

---

### 26. Conditional Formatting Measure — Attrition Rate Status Color
```dax
Attrition Status Color =
SWITCH(
    TRUE(),
    [Attrition Rate] > 0.18, "#D64550",
    [Attrition Rate] > 0.12, "#F2B84B",
    "#3FA796"
)
```
**Explanation:** returns a hex string consumed by a visual's conditional formatting ("Format by: Field value") to color KPI cards red/amber/green against the thresholds in `KPIs.md`.

---

### 27. Ranking Measure — Department Attrition Rank
```dax
Department Attrition Rank =
RANKX(ALL(HR_Employee_Data[Department]), [Attrition Rate], , DESC)
```
**Expected output:** Sales = Rank 1 (23.7%)

---

### 28. Top Departments by Headcount
```dax
Department Headcount Rank = RANKX(ALL(HR_Employee_Data[Department]), [Total Employees], , DESC)
```
**Expected output:** Sales = Rank 1 (1,204 employees)

---

### 29. Top Job Roles by Attrition
```dax
Job Role Attrition Rank = RANKX(ALL(HR_Employee_Data[JobRole]), [Attrition Rate], , DESC)
```
**Expected output:** Sales Representative = Rank 1 (32.0%)

---

### 30. Overtime Attrition Gap
**Purpose:** Quantifies overtime's impact for the executive insights page.
```dax
Overtime Attrition Gap =
VAR OTYes = CALCULATE([Attrition Rate], HR_Employee_Data[OverTime] = "Yes")
VAR OTNo  = CALCULATE([Attrition Rate], HR_Employee_Data[OverTime] = "No")
RETURN OTYes - OTNo
```
**Expected output:** 28.6% − 13.2% = **+15.4 points**

---

### 31. Average Absenteeism
```dax
Average Absenteeism = AVERAGE(HR_Employee_Data[Absenteeism])
```

---

### 32. Average Leave Balance
```dax
Average Leave Balance = AVERAGE(HR_Employee_Data[LeaveBalance])
```

---

### 33. % Working Overtime
```dax
Pct Overtime = DIVIDE(CALCULATE([Total Employees], HR_Employee_Data[OverTime]="Yes"), [Total Employees], 0)
```
**Expected output:** 31.9%

---

### 34. % Remote / Hybrid / Onsite
```dax
Pct Remote Work =
DIVIDE(
    CALCULATE([Total Employees], HR_Employee_Data[RemoteWork] = SELECTEDVALUE(HR_Employee_Data[RemoteWork])),
    [Total Employees], 0
)
```

---

### 35. Gender Diversity Ratio
```dax
Gender Ratio Female = DIVIDE(CALCULATE([Total Employees], HR_Employee_Data[Gender]="Female"), [Total Employees], 0)
```
**Expected output:** 50.0%

---

### 36. Salary Quartile Attrition Spread
```dax
Salary Quartile Attrition Spread =
VAR Q1 = CALCULATE([Attrition Rate], HR_Employee_Data[SalaryQuartile] = "Q1 (Lowest)")
VAR Q4 = CALCULATE([Attrition Rate], HR_Employee_Data[SalaryQuartile] = "Q4 (Highest)")
RETURN Q1 - Q4
```
**Expected output:** 22.2% − 14.9% = **+7.3 points** (lowest-paid quartile leaves at 1.5x the rate of the highest-paid)
*Note: SalaryQuartile is added as a calculated column: `SalaryQuartile = SWITCH(TRUE(), ... )` bucketed on `Salary` quartile breakpoints, or generated in Power Query.*

---

### 37. Dynamic Title — Selected Department
```dax
Dynamic Page Title =
"Attrition Analysis — " &
IF(
    ISFILTERED(HR_Employee_Data[Department]),
    SELECTEDVALUE(HR_Employee_Data[Department], "Multiple Departments"),
    "All Departments"
)
```

---

### 38. Promotion Impact on Attrition
```dax
Promotion Attrition Gap =
VAR PromotedRate = CALCULATE([Attrition Rate], HR_Employee_Data[PromotionLastYear] = "Yes")
VAR NotPromotedRate = CALCULATE([Attrition Rate], HR_Employee_Data[PromotionLastYear] = "No")
RETURN NotPromotedRate - PromotedRate
```
**Expected output:** 19.5% − 9.2% = **+10.3 points**

---

### 39. Top Attrition Concentration (Pareto Measure)
```dax
Pct Attrition from Top 5 Roles =
VAR Top5 = TOPN(5, VALUES(HR_Employee_Data[JobRole]), CALCULATE([Attrition Count]), DESC)
VAR Top5Attrition = SUMX(Top5, CALCULATE([Attrition Count]))
RETURN DIVIDE(Top5Attrition, [Attrition Count], 0)
```
**Expected output:** ~35% of all attrition comes from just 5 of 27 job roles.

---

### 40. Average Distance from Home (Attrition Segment)
```dax
Avg Distance Leavers = CALCULATE(AVERAGE(HR_Employee_Data[DistanceFromHome]), HR_Employee_Data[Attrition]="Yes")
```

---

### 41. Total Bonus Payout
```dax
Total Bonus Payout = SUM(HR_Employee_Data[Bonus])
```

---

### 42. Headcount Same Period Last Year (for KPI trend arrows)
```dax
Headcount SPLY = CALCULATE([Total Employees], SAMEPERIODLASTYEAR(DateTable[Date]))
```

---

## Design principles used across these measures
- **Always use `DIVIDE()`**, never the `/` operator, to avoid divide-by-zero blanks/errors on filtered slicer states.
- **`USERELATIONSHIP`** is used deliberately wherever ExitDate needs to drive a time-based visual, since only one active relationship can exist between the fact table and `DateTable`.
- **Base measures are composed**, not repeated — e.g., Attrition Rate always calls `[Attrition Count]` and `[Total Employees]` rather than re-writing `CALCULATE(COUNTROWS(...))` inline, so a single definition change propagates everywhere.
- **RANKX/TOPN** measures back the "Top Departments"/"Top Roles" visuals and dynamic drill-through targeting.
