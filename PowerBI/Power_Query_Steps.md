# Power Query (M) Transformation Steps

Applied to `HR_Employee_Data.csv` after importing into Power BI Desktop (Get Data → Text/CSV → Transform Data).

## 1. Set correct data types
```m
= Table.TransformColumnTypes(Source,{
    {"EmployeeID", type text}, {"Age", Int64.Type}, {"Salary", Int64.Type},
    {"Bonus", Int64.Type}, {"MonthlyIncome", type number},
    {"Experience", type number}, {"YearsAtCompany", type number},
    {"YearsInCurrentRole", type number}, {"TrainingHours", Int64.Type},
    {"PerformanceRating", Int64.Type}, {"JobSatisfaction", Int64.Type},
    {"EnvironmentSatisfaction", Int64.Type}, {"WorkLifeBalance", Int64.Type},
    {"HireDate", type date}, {"ExitDate", type date},
    {"DistanceFromHome", Int64.Type}, {"Absenteeism", Int64.Type},
    {"LeaveBalance", Int64.Type}
})
```
**Why:** the CSV importer defaults numeric and date columns to text; DAX aggregations (SUM/AVERAGE) and time intelligence fail silently on text columns.

## 2. Remove duplicates
```m
= Table.Distinct(#"Changed Type", {"EmployeeID"})
```
**Why:** guards against duplicate exports being appended twice — a common real-world HRIS export issue.

## 3. Handle missing values (blank ExitDate / ReasonForLeaving for active employees)
```m
= Table.ReplaceValue(#"Removed Duplicates", null, "Still Employed", Replacer.ReplaceValue, {"ReasonForLeaving"})
```
**Why:** blank ReasonForLeaving is expected for active employees, but Power BI slicers render nulls awkwardly — an explicit label reads better on a filter pane. `ExitDate` is left as a true blank/null (not text) so date-based measures like `DATEDIFF` continue to work correctly for active employees.

## 4. Fix inconsistent text (trim/clean + proper case)
```m
= Table.TransformColumns(#"Replaced Value",{
    {"Department", Text.Trim, type text},
    {"JobRole", Text.Trim, type text},
    {"City", Text.Proper, type text}
})
```
**Why:** source exports from HRIS systems frequently contain leading/trailing whitespace and inconsistent casing that silently breaks GROUP BY-style visuals (two "Sales " and "Sales" rows becoming separate categories).

## 5. Split / derive columns from HireDate
```m
= Table.AddColumn(#"Trimmed Text", "HireYear", each Date.Year([HireDate]), Int64.Type)
= Table.AddColumn(#"Added HireYear", "HireMonth", each Date.Month([HireDate]), Int64.Type)
= Table.AddColumn(#"Added HireMonth", "HireMonthName", each Date.MonthName([HireDate]), type text)
```
**Why:** enables monthly/yearly hiring-trend visuals without relying on DAX to parse dates at query time.

## 6. Merge columns — build a single Location field
```m
= Table.AddColumn(#"Added HireMonthName", "Location", each [City] & ", " & [State] & ", " & [Country], type text)
```
**Why:** a single concatenated field is easier to use as a map visual tooltip and drill-through label than three separate columns.

## 7. Replace values — standardize Yes/No flags to a Boolean-friendly indicator
```m
= Table.AddColumn(#"Added Location", "IsActive", each if [Attrition] = "No" then 1 else 0, Int64.Type)
```
**Why:** an integer flag (0/1) is more efficient for DAX SUM-based measures than repeatedly evaluating text comparisons.

## 8. Calculated column — Tenure Band
```m
= Table.AddColumn(#"Added IsActive", "TenureBand", each
    if [YearsAtCompany] < 2 then "0-2 yrs"
    else if [YearsAtCompany] < 5 then "2-5 yrs"
    else if [YearsAtCompany] < 10 then "5-10 yrs"
    else "10+ yrs", type text)
```
**Why:** pre-bucketing tenure in Power Query (rather than a DAX calculated column) keeps the data model lighter and the logic reusable across visuals without re-evaluating row context.

## 9. Calculated column — Age Group
```m
= Table.AddColumn(#"Added TenureBand", "AgeGroup", each
    if [Age] <= 25 then "18-25"
    else if [Age] <= 30 then "26-30"
    else if [Age] <= 35 then "31-35"
    else if [Age] <= 40 then "36-40"
    else if [Age] <= 45 then "41-45"
    else if [Age] <= 50 then "46-50"
    else "51-60", type text)
```

## 10. Create a Date dimension table (new blank query)
```m
let
    StartDate = #date(2016,1,1),
    EndDate = #date(2026,12,31),
    DayCount = Duration.Days(EndDate - StartDate) + 1,
    Dates = List.Dates(StartDate, DayCount, #duration(1,0,0,0)),
    #"Converted to Table" = Table.FromList(Dates, Splitter.SplitByNothing(), {"Date"}),
    #"Changed Type" = Table.TransformColumnTypes(#"Converted to Table",{{"Date", type date}}),
    #"Added Year" = Table.AddColumn(#"Changed Type", "Year", each Date.Year([Date]), Int64.Type),
    #"Added Month" = Table.AddColumn(#"Added Year", "Month", each Date.Month([Date]), Int64.Type),
    #"Added MonthName" = Table.AddColumn(#"Added Month", "MonthName", each Date.MonthName([Date]), type text),
    #"Added Quarter" = Table.AddColumn(#"Added MonthName", "Quarter", each "Q" & Text.From(Date.QuarterOfYear([Date])), type text)
in
    #"Added Quarter"
```
**Why:** a dedicated Date table is required for reliable DAX time intelligence (YoY growth, running totals, previous-month comparisons) — using the fact table's own date columns directly produces incorrect or non-contiguous results.

## Final applied steps (in order)
1. Changed Type
2. Removed Duplicates
3. Replaced Value (ReasonForLeaving)
4. Trimmed Text (Department, JobRole, City)
5. Added HireYear / HireMonth / HireMonthName
6. Added Location (merged column)
7. Added IsActive (replaced Yes/No with 1/0 flag)
8. Added TenureBand (calculated column)
9. Added AgeGroup (calculated column)
10. Date dimension table created as a separate query and marked as a Date Table in the model
