\# 🌧️ CivicPulse

\## Delhi Waterlogging Risk Assessment Dashboard



CivicPulse is a Data Analytics minor project developed to study rainfall patterns and analyze MCD-listed waterlogging-vulnerable locations in Delhi.



The project combines data cleaning, rainfall analysis, geospatial visualization, and a rule-based rainfall risk assessment dashboard.



\## 🎯 Project Objectives



\- Analyze daily rainfall patterns in Delhi from 2020 to 2025.

\- Study MCD-listed waterlogging-vulnerable locations.

\- Visualize available geographic coordinates on an interactive map.

\- Analyze geocoding coverage across MCD zones.

\- Demonstrate a rainfall-based risk indicator using project-defined thresholds.



\## 🛠️ Technologies Used



\- Python

\- Pandas

\- Streamlit

\- Matplotlib

\- NASA POWER Daily Rainfall Data

\- MCD waterlogging-related location records



\## 📊 Dashboard Modules



1\. Project Overview

2\. Rainfall Analysis

3\. Risk Analysis

4\. MCD Location Map

5\. Geocoding Coverage



\## 📁 Project Structure



```text

CivicPulse/

├── app.py

├── requirements.txt

├── README.md

├── .gitignore

├── data/

│   └── processed/

│       ├── delhi\_daily\_rainfall\_clean.csv

│       ├── delhi\_rainfall\_risk\_indicator.csv

│       ├── mcd\_locations\_final.csv

│       └── final\_geocoding\_coverage\_by\_zone.csv

└── outputs/

&#x20;   └── dashboard\_screenshots/

&#x20;       ├── 01\_Project\_Overview.png

&#x20;       ├── 02\_Rainfall\_Analysis.png

&#x20;       ├── 03\_Risk\_Analysis.png

&#x20;       ├── 04\_MCD\_Location\_Map.png

&#x20;       └── 05\_Geocoding\_Coverage.png

```



\## 📍 Dataset Information



\- Rainfall data: NASA POWER daily corrected precipitation estimates (`PRECTOTCORR`) for a Delhi reference coordinate, 2020–2025.

\- Location data: 76 MCD-listed waterlogging-vulnerable locations.

\- Geographic coordinates: 33 locations have coordinates available; 4 have been manually verified and 29 remain pending verification.



\## ⚠️ Risk Assessment Disclaimer



The dashboard uses initial project-defined rainfall thresholds to classify historical rainfall records into Low, Moderate, High, and Insufficient Data categories.



This is a rule-based academic prototype, not a trained machine learning model or an official flood prediction or emergency alert system.



Rainfall data represents one Delhi reference coordinate and should not be interpreted as location-specific rainfall for every MCD site.



\## 🚀 Run Locally



Clone the repository:



```bash

git clone https://github.com/KhushiGupta13/CivicPulse.git

cd CivicPulse

```



Install dependencies:



```bash

pip install -r requirements.txt

```



Run the dashboard:



```bash

streamlit run app.py

```



\## 🎓 Academic Project



\*\*Institution:\*\* Noida International University  

\*\*Course:\*\* B.Tech  

\*\*Branch:\*\* Data Science  

\*\*Project:\*\* Data Analytics Minor Project  

\*\*Project Guide:\*\* Aniket Singh



\### Project Team



\- Khushi Gupta

\- Bhumika Giri

\- Arti Kumari

\- Dipika Gupta

