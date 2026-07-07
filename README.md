# HR Analytics Dashboard — Power BI

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat&logo=powerbi&logoColor=black)
![DAX](https://img.shields.io/badge/DAX-0078D4?style=flat&logo=microsoft&logoColor=white)
![Power Query](https://img.shields.io/badge/Power%20Query-217346?style=flat&logo=microsoftexcel&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)

An end-to-end HR analytics project — from synthetic data generation through a production-style Power BI data model, 40+ DAX measures, and executive-ready insights — built to demonstrate the full analyst workflow, not just a finished chart.

## Business Problem
A company with 5,400+ employees across 8 departments and 4 regions has rising attrition in specific pockets but no self-service way to quantify or explain it. This dashboard gives HR leadership a single source of truth for attrition, compensation, performance, and workforce composition — and answers the 50+ business questions in `PowerBI/Business_Requirements.md`.

## Headline Finding
**Overtime, not pay, is the strongest attrition driver in this data.** Employees who regularly work overtime leave at 28.6%, more than double the 13.2% rate for those who don't — a bigger effect than the 7.3-point gap between the lowest and highest salary quartiles. Full findings in `reports/Business_Insights.md`.

## Dataset
- 5,400 synthetic employee records, 38 fields, generated in Python/pandas with **engineered** (not random) business patterns:
  - Attrition driven by a weighted model (overtime, age, role, satisfaction, promotion history)
  - **Pareto concentration**: 18 of 27 job roles account for ~80% of all attrition
  - Department-level salary differentiation ($74K–$121K average by department)
  - Hiring/resignation seasonality (Jan/Sep hiring peaks, Jan/Feb/Jun resignation spikes)
- Full field-by-field documentation: `PowerBI/Data_Dictionary.md`
- Generation script (reproducible): `scripts/generate_dataset.py`

## Technology Stack
| Layer | Tools |
|---|---|
| Data generation & validation | Python, pandas, numpy |
| Data prep | Power Query (M) |
| Modeling | Power BI star schema (fact + Date dimension) |
| Analysis | DAX (42 measures) |
| Visualization | Power BI Desktop |
| Docs | Markdown |

## Power BI Features Demonstrated
Bookmarks · Dynamic titles · Conditional formatting · Drill-through · Sync slicers · Custom theme · RANKX/TOPN leaderboards · Time intelligence with dual active/inactive date relationships (`USERELATIONSHIP`)

## Dashboard Pages
1. **Executive Overview** — headcount, attrition rate, salary, tenure KPIs; hiring/resignation trend; location map
2. **Attrition Analysis** — attrition by department, role, age, gender, salary quartile; reason-for-leaving breakdown; department×role heatmap
3. **Employee Demographics** — gender, age, education, department/role treemap, location
4. **Performance Analysis** — performance distribution, training hours, promotion rate, training-vs-performance scatter
5. **Salary Dashboard** — salary/bonus by department and job level, income trend by hire year
6. **Executive Insights** — curated findings and recommendations for leadership

Full page-by-page build spec (including exact visuals and why each was chosen): `PowerBI/Dashboard_Design.md`

## Project Structure
```
HR-Analytics-Dashboard/
├── README.md
├── LICENSE
├── .gitignore
├── Interview_QA.md
├── dataset/
│   └── HR_Employee_Data.csv
├── scripts/
│   ├── generate_dataset.py         # reproducible synthetic data generation
│   └── validate_and_analyze.py     # computes every stat cited in the reports
├── PowerBI/
│   ├── HR_Analytics_Dashboard.pbix     # build in Power BI Desktop — see images/screenshots_placeholder.md
│   ├── HR_Analytics_Dashboard.pdf
│   ├── Power_Query_Steps.md
│   ├── DAX_Measures.md
│   ├── Dashboard_Design.md
│   ├── Business_Requirements.md
│   ├── KPIs.md
│   └── Data_Dictionary.md
├── reports/
│   ├── Business_Insights.md         # 30 grounded, numbers-first insights
│   └── Executive_Summary.md
└── images/
    └── screenshots_placeholder.md
```

## Installation / How to Open
1. Clone this repo.
2. Install [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (Windows).
3. Follow `PowerBI/Power_Query_Steps.md` to load and clean `dataset/HR_Employee_Data.csv`, then `PowerBI/DAX_Measures.md` and `PowerBI/Dashboard_Design.md` to build the 6-page report (see `images/screenshots_placeholder.md` for the full checklist — the `.pbix` and screenshots must be assembled locally in Power BI Desktop, since that step requires the desktop application itself).
4. To regenerate or modify the dataset: `pip install pandas numpy` then `python scripts/generate_dataset.py`.

## KPIs
See `PowerBI/KPIs.md` for the full list with current values and conditional-formatting thresholds. Headline KPIs: **18.15% attrition rate**, **$98,984 average salary**, **5.59-year average tenure**, **13.48% promotion rate**.

## Learning Outcomes
- Designing a star schema sized appropriately for the data volume (not over-normalizing a 5,400-row dataset)
- Handling dual date relationships (hire vs. exit) with `USERELATIONSHIP`
- Writing composable DAX (base measures reused across derived measures) rather than duplicating logic
- Translating chart-level findings into ranked, numbers-first business recommendations

## Future Improvements
- Row-Level Security by Business Unit for regional HR partners
- Incremental refresh + Power BI Service scheduled refresh
- A predictive attrition-risk score (logistic regression / gradient boosting) surfaced as a "flight risk" flag
- Mobile-optimized layout and a dark-theme variant
- Power BI Python/R visual integration for the training-vs-performance scatter

## Acknowledgements
Dataset is fully synthetic, generated for portfolio purposes — no real employee data is used.

## License
MIT — see [LICENSE](LICENSE).
