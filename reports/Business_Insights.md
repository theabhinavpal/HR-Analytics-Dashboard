# Business Insights — HR Analytics Dashboard

All figures below are computed directly from `dataset/HR_Employee_Data.csv` (5,400 employees). Each insight pairs a finding with a business recommendation — not just a chart description.

## Attrition Drivers

1. **Overtime is the single strongest attrition signal in the data.** Employees who regularly work overtime leave at 28.6%, versus 13.2% for those who don't — a 15.4-point gap. *Recommendation: audit workload distribution in Sales and Customer Support, the two departments with the highest overtime incidence, before treating attrition as a compensation problem.*

2. **Attrition is heavily concentrated, not evenly spread — a Pareto pattern.** Just 5 of 27 job roles account for roughly 35% of all resignations, and 18 of 27 roles account for ~80%. *Recommendation: a company-wide retention program is inefficient — target Sales Representative, Sales Executive, Account Manager, and Data Scientist specifically.*

3. **Sales has both the highest headcount-weighted attrition (23.7%) and the highest-attrition individual role** (Sales Representative, 32.0%). *Recommendation: treat Sales retention as a distinct initiative from company-wide HR policy — likely commission structure, quota pressure, or manager span-of-control issues specific to that function.*

4. **Early-career and early-tenure employees are a flight risk.** Ages 18-25 and 26-30 both show ~28% attrition, roughly double the 31-50 age bands (15-17%). *Recommendation: strengthen onboarding, mentorship, and 90-day/1-year check-in programs — this is a retention window, not a compensation problem for this segment.*

5. **Pay matters, but it's not the dominant lever.** Attrition drops from 22.2% (lowest salary quartile) to 14.9% (highest quartile) — a real but moderate 7.3-point spread, smaller than the overtime gap. *Recommendation: compensation review helps, but overtime/workload reduction will move the needle more.*

6. **Promotions are a strong retention lever.** Employees promoted in the last 12 months leave at 9.2%, versus 19.5% for those not promoted — a 10.3-point gap. *Recommendation: departments with below-average promotion rates should be flagged as attrition risk even if pay is competitive.*

7. **Work-life balance has a clear, monotonic relationship with attrition.** WLB rating of 1 (poor) → 22.3% attrition; WLB rating of 4 (excellent) → 14.5%. *Recommendation: WLB self-reported scores are a leading indicator worth tracking quarterly, not just an annual engagement-survey afterthought.*

8. **"Better Opportunity" is the top cited reason for leaving (21.1% of exits), followed by Compensation (15.8%) and Relocation (15.3%).** *Recommendation: exit interview data suggests external market pull, not just internal dissatisfaction — competitive benchmarking against market rate should be routine, not reactive.*

9. **Gender is not a meaningful attrition driver in this dataset** (18.1% female vs 18.2% male) — ruling out gender-based retention risk as a driver here, unlike age, overtime, or role.

10. **Commute distance shows only a mild effect** — attrition rises modestly from 18.0% (0-5km) to 19.6% (21km+), suggesting hybrid/remote flexibility may already be absorbing most of the commute-related risk.

## Compensation

11. **IT is the highest-paying department ($121,057 avg), followed by R&D ($112,011) and Finance ($106,499); Customer Support is lowest ($74,015).** This roughly tracks market scarcity of technical talent.

12. **Average bonus is 11.97% of salary** company-wide — a useful benchmark when negotiating new offers or comparing to industry variable-pay norms.

13. **Salary scales meaningfully with job level** (1×-3× multiplier baked into the structure) — the pay pyramid is intact and not compressed, which supports internal promotion as a credible growth path (reinforcing insight #6).

## Workforce Composition

14. **The workforce is gender-balanced overall (50/50)** — useful as a baseline diversity metric, though role-level and job-level breakdowns should be checked separately for representation at senior levels.

15. **Sales (1,204 employees, 22.3% of headcount) and R&D (1,048, 19.4%) are the two largest departments** — together representing over 40% of the company, meaning attrition trends in these two departments dominate the company-wide attrition rate.

16. **Mexico City and São Paulo are the two largest office locations** by headcount, ahead of all North American and European sites — LATAM has become the largest regional hub, which should inform where HR business-partner capacity is allocated.

## Performance & Development

17. **59% of employees are rated "Meets Expectations" (3/4), and only 3.1% are rated "Needs Improvement" (1/4)** — a healthy, right-skewed performance distribution with no ratings-inflation red flags.

18. **Training hours are fairly evenly distributed across departments (42.5–44.1 hrs)** — no department is being systematically under-invested in, though IT receives marginally the most.

19. **Life Sciences and Medical education backgrounds show the (marginally) highest average performance ratings (~3.0/4)**, though the spread across all education fields is narrow (2.95–3.01) — education field is not a strong performance predictor in this dataset.

20. **Only 13.5% of eligible employees were promoted in the last 12 months** — combined with insight #6, this suggests promotion velocity, not promotion existence, may be the retention lever to pull.

## Wellbeing & Engagement

21. **Average job satisfaction (2.93/4), environment satisfaction (2.91/4), and work-life balance (2.99/4) all cluster just under the midpoint of a 4-point scale** — none are in "poor" territory, but none signal strong engagement either; this is a workforce that is neither disengaged nor delighted.

22. **Absenteeism rises steadily as job satisfaction falls** — from 4.05 average absence days at JobSatisfaction=4 to 7.03 days at JobSatisfaction=1, a 73% increase. *Recommendation: absenteeism data can serve as an early, low-friction proxy for satisfaction issues between annual survey cycles.*

23. **Roughly 32% of the workforce regularly works overtime** — given its outsized attrition impact (insight #1), this is a larger share of the company than the retention risk analysis alone might suggest.

24. **45% of employees work in a hybrid arrangement, 35% fully onsite, and 20% fully remote** — but attrition rates are nearly flat across all three (17.6%-18.5%), indicating work-location flexibility is not, on its own, a retention differentiator in this data.

## Seasonality & Trends

25. **Hiring is seasonal, peaking in January (11.9% of all hires) and September (13.0%)**, consistent with new fiscal-year budget cycles and post-summer recruiting pushes; June and December are the slowest hiring months (~5% each).

26. **Resignations spike in January/February (12.1% / 10.7% of all exits) and again in June (11.1%)** — the January/February spike aligns with post-bonus-payout exit timing, a well-documented industry pattern this dataset was deliberately built to reflect.

27. **Average tenure across the company is 5.59 years**, with average total experience of 9.69 years — implying the average employee joined mid-career rather than as an early-career hire, consistent with the low share of the 18-25 age band (5.2% of headcount).

## Executive-Level Takeaways

28. **Attrition is a workload and career-mobility problem more than a pay problem** — overtime (+15.4 pts) and lack of promotion (+10.3 pts) both outweigh the salary-quartile effect (+7.3 pts).

29. **A targeted intervention in 4-5 Sales and technical roles would address over a third of total attrition** — far more efficient than a blanket retention initiative.

30. **The 18-30 age band is the highest-risk retention segment and the department mix (heavy Sales/R&D weighting) means these dynamics disproportionately shape total company attrition** — any retention budget should be weighted toward these two departments and this age band first.
