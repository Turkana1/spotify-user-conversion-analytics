# Spotify User Conversion & Audio Analytics

This repository contains an end-to-end data analytics project focused on Spotify's free user base and audio track features. The main goal of this project is to analyze user engagement, explore track characteristics, and estimate revenue growth from Premium conversions.

---

## Dashboard Preview

##1. User Conversion & Revenue Analytics
![Spotify Analytics Dashboard - Page 1](./sp_analytics.png)

### 2. Audio Features & Monetization Analytics
![Spotify Analytics Dashboard - Page 2](./sp_analytics2.png)

---

## What This Project Answers

Instead of just cleaning data, I focused on addressing practical business questions:
* **Who should we target?** Grouping free listeners based on activity levels to identify high-potential conversion targets.
* **What are the key track characteristics?** Mapping track features like energy and danceability to understand library distribution.
* **What is the potential ROI?** Tracking current estimated Annual Recurring Revenue (ARR) against milestone targets using custom DAX measures.

---

## Tools & Stack

* **Python (pandas, numpy):** Data cleaning, processing missing values, and generating transformed datasets.
* **Power BI:** Data modeling, custom DAX measures, and interactive reporting.
* **UI Design:** Customized dark theme matching Spotify's native brand palette (`#000000` / `#121212` background, `#1DB954` green accents, and `#FFFFFF` text).

---

## Key Findings & Metrics

* **Revenue Projection:** Estimated ARR is currently tracked at **$6.83K** against a target milestone of **$10K** (Gauge Visual bounded at **$13.66K**).
* **Audio Sweet Spot:** Scatter plot analysis evaluates track distribution across **Energy** vs. **Danceability** to spot engagement trends.

---

## DAX Measures Used

```dax
Target ARR = 10000
Max ARR = 15000
