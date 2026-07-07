# Executive Summary — HR Analytics Dashboard

**Workforce:** 5,400 employees · 8 departments · 4 regions (North America, EMEA, APAC, LATAM)
**Overall Attrition Rate:** 18.15% (980 exits)

## The Headline
Attrition is not evenly distributed — it is concentrated in overtime-heavy roles, early-career employees, and a small number of Sales and technical job titles. Pay is a secondary factor behind workload and promotion velocity.

## Top 3 Findings
1. **Overtime employees leave at more than double the rate of non-overtime employees** (28.6% vs. 13.2%) — the single strongest driver in the dataset.
2. **Just 5 of 27 job roles drive ~35% of all attrition** (Sales Representative, Sales Executive, Account Manager, Data Scientist, Sales Manager) — retention spend should be targeted, not company-wide.
3. **Promotion is a stronger retention lever than pay**: promoted employees leave at 9.2% vs. 19.5% for those not promoted (a 10.3-point gap), compared to a 7.3-point gap between the lowest and highest salary quartiles.

## Recommended Actions
| Priority | Action | Expected Impact |
|---|---|---|
| High | Audit overtime/workload distribution in Sales and Customer Support | Directly targets the largest single attrition driver |
| High | Build a targeted retention plan for the top 5 highest-attrition roles | Addresses ~35% of attrition with focused effort |
| Medium | Increase promotion velocity, particularly for high performers with 2+ years tenure | Reduces the 10.3-point promotion/attrition gap |
| Medium | Strengthen 90-day and 1-year onboarding touchpoints for employees under 30 | Targets the highest-attrition age band (~28%) |
| Low | Use absenteeism trend as an early proxy for satisfaction issues between survey cycles | Enables earlier intervention |

## Dashboard Scope
Six report pages (Executive Overview, Attrition Analysis, Demographics, Performance, Salary, Executive Insights) built on a single fact table + Date dimension star schema, with 40+ DAX measures covering attrition, compensation, performance, and time-intelligence calculations. Full methodology and all 30 supporting insights are in `Business_Insights.md`.
