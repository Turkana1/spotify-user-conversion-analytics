# Spotify User Conversion & Audio Analytics

This repository contains an end-to-end data analytics project focused on Spotify's free user base and audio track features. The main goal here was to figure out which free users are most likely to upgrade to Premium and what kind of music keeps them engaged.
## 🖼️ Dashboard Preview

## 1. User Conversion Overview
![Overview Dashboard](SP%20ANALYTCS.png)

## 2. Cohort Engagement & Monetization
![Advanced Analytics](SP%20ANALYTC2.jpg)
---

##  What This Project Answers
Instead of just cleaning data, I wanted to answer a few practical business questions:
* **Who should we target?** Grouping free listeners based on their activity levels to find high-potential conversion targets.
* **What are they listening to?** Identifying the top genres among active free users so marketing teams know what content to push.
* **How do track features impact retention?** Checking how audio traits like energy and danceability correlate with lower skip rates.
* **What’s the potential ROI?** Calculating estimated annual revenue lift if we successfully convert a portion of these users.

---

##  Tools & Stack
* **Python (`pandas`, `numpy`):** Data cleaning, handling missing values, and building user segments.
* **Power BI:** Star Schema data modeling, DAX measures, and interactive reporting.
* **UI Design:** Customized dark theme matching Spotify's native brand palette (`#121212`, `#1DB954`).

---

## Key Findings
* **Target Audience:** Out of the free user sample, **114 users (~36.8%)** stood out as "High Potential" due to their high session frequency.
* **Genre Focus:** **Pop** and **Rock** dominate this high-potential segment, making them ideal anchors for conversion-focused ads.
* **Audio Sweet Spot:** Songs with both `danceability` and `energy` scores above 0.7 showed noticeably better engagement.
* **Revenue Projection:** Converting just 50% of this high-potential group yields a projected **~$6,830 ARR increase**.

---

##  Repository Structure
* `sp.py` - Python script used for data transformation and feature creation.
* `cleaned_spotify_users.csv` & `spotify_genre_audio_summary.csv` - Processed datasets.
* `spotify_dashboard_preview.png` & `spotify_advanced_analytics.png` - Dashboard previews.
