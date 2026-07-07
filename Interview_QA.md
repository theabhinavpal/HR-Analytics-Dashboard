# Interview Preparation — HR Analytics Dashboard

## Resume Bullets

- Designed and built an end-to-end HR Analytics dashboard in Power BI on a 5,400-employee dataset, uncovering that overtime workers churn at 2.2x the rate of non-overtime employees (28.6% vs 13.2%), directly informing a workload-reduction retention strategy.
- Engineered a star-schema data model (fact table + Date dimension) with dual active/inactive relationships (USERELATIONSHIP) to support accurate time-intelligence reporting on both hire and exit dates.
- Authored 40+ production DAX measures spanning attrition, compensation, and performance KPIs, including YoY growth, running totals, dynamic titles, and RANKX-based leaderboards.
- Applied Pareto analysis to attrition data, identifying that 5 of 27 job roles account for ~35% of company-wide resignations — reframing a company-wide retention initiative into a targeted 4-role intervention.
- Built a 6-page interactive Power BI report (Executive Overview, Attrition, Demographics, Performance, Salary, Executive Insights) using bookmarks, drill-through, sync slicers, and conditional formatting to support self-service exploration for HR leadership.

## 10 Power BI / Analytics Interview Questions & Answers

**1. Why did you choose a single fact table instead of a fully normalized star schema?**
At 5,400 rows and this column count, splitting Department/JobRole/Location into separate dimension tables adds join complexity without a real performance gain — Power BI's VertiPaq engine compresses this easily as one table. I did split out a proper Date dimension, though, because time intelligence (YoY, running totals) genuinely requires it. The lesson: match the schema to the actual query patterns and data volume, not a textbook ideal.

**2. Why use USERELATIONSHIP instead of two separate date columns?**
A table can only have one *active* relationship to a given dimension at a time. I needed both HireDate and ExitDate to drive time-based visuals (hiring trend vs. resignation trend), so HireDate is the active relationship and ExitDate is inactive, activated inside specific measures via USERELATIONSHIP() only when that measure needs to filter by exit month.

**3. Walk me through how you'd explain the Attrition Rate measure and why DIVIDE() matters.**
`Attrition Rate = DIVIDE([Attrition Count], [Total Employees], 0)`. DIVIDE returns a safe default (0 here) instead of erroring out when the denominator is 0 — which happens the moment a user filters to a department/segment with zero employees. Using the raw `/` operator would throw a division error and break the visual.

**4. How did you validate that your insights are statistically meaningful and not noise?**
I checked effect sizes, not just direction — e.g., the overtime attrition gap is 15.4 percentage points on a base rate of 18%, which is a large practical effect, not a rounding artifact. I also cross-checked that the same drivers (overtime, role, age) showed up consistently across multiple cuts of the data (department, role, quartile) rather than relying on one chart in isolation.

**5. What's the business impact of the Pareto finding on job-role attrition?**
It changes the intervention strategy. If attrition were evenly spread, you'd need a company-wide retention policy. Since ~35% of attrition comes from just 5 roles, HR can build a targeted intervention — comp review, manager coaching, workload audit — for those specific roles, which is both cheaper and faster to execute than a blanket program.

**6. How would you extend this into a predictive model?**
I'd start with a logistic regression or gradient-boosted classifier using the same features already in the model (overtime, job satisfaction, tenure, salary quartile, role) to score active employees' attrition risk, then surface a "flight risk" flag as a Power BI visual fed by a scheduled Python/R script or Azure ML endpoint — flagged in this repo's Bonus Features as an advanced enhancement.

**7. Why didn't you use pie charts for department-level attrition?**
With 8 departments, a pie chart makes it hard to compare near-equal slices accurately — human eyes are much better at comparing bar lengths than pie angles. I reserved donut/pie charts for true part-of-whole breakdowns with very few categories, like gender (2 categories) or top resignation reasons.

**8. How do you decide which measures need RANKX vs. a simple sort in the visual?**
Sorting a visual only affects that one visual. RANKX gives you a reusable numeric rank you can reference elsewhere — for example, driving a "Top 3 highest-attrition departments" card or conditionally formatting only the top-ranked row across multiple visuals on the same page.

**9. What would you tell a stakeholder who says "just tell me if pay is the problem"?**
Pay matters, but it's not the dominant lever here — the salary-quartile attrition gap (7.3 points) is smaller than both the overtime gap (15.4 points) and the promotion gap (10.3 points). I'd show all three side by side so the stakeholder can see the relative size of each effect rather than anchoring on the first one they thought of.

**10. What are the limitations of this dataset/analysis?**
It's a synthetic dataset engineered with realistic patterns for portfolio purposes — the relationships (overtime → attrition, role concentration, etc.) are deliberately built in rather than naturally occurring, so it's excellent for demonstrating analytical technique but the specific numbers aren't real company data. In a live engagement I'd also want exit-interview qualitative data, manager 1:1 notes, and a longer historical window to validate seasonality patterns beyond what a single synthetic 10-year window can show.

## Common Interview Mistakes to Avoid
- Describing charts ("this bar chart shows department attrition") instead of the insight and action it enables.
- Not being able to state *why* a specific DAX pattern (DIVIDE, USERELATIONSHIP, RANKX) was necessary versus just "that's the syntax."
- Overclaiming statistical certainty on a portfolio/synthetic dataset — be upfront it's synthetic and explain *why* that's actually a deliberate, defensible choice (reproducibility, no data privacy/copyright issues, known ground truth).

## How to Explain This Project in 60 Seconds
"I built a full HR analytics dashboard end to end — generated a realistic 5,400-employee dataset with deliberately engineered patterns, then built a Power BI star-schema model with 40+ DAX measures. The standout finding was that overtime and lack of promotion predict attrition more strongly than pay does, and that attrition itself is concentrated in a handful of roles rather than spread evenly — which changes how you'd actually design a retention program. I documented every transformation and measure so the whole thing is reproducible and defensible in a review."
